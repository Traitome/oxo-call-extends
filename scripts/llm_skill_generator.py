#!/usr/bin/env python3
"""
LLM-based skill generator for bioconda tools.

Uses an LLM (via OpenAI or Anthropic API) with the check-skill methodology
to generate accurate, comprehensive skill files for bioconda CLI tools.
Each tool is individually processed by the LLM — this is NOT a template script.

Usage:
    # Single tool
    python scripts/llm_skill_generator.py samtools

    # Multiple tools
    python scripts/llm_skill_generator.py samtools bwa gatk

    # All tools needing improvement (< 5 examples)
    python scripts/llm_skill_generator.py --all

    # Dry-run: list tools that need improvement
    python scripts/llm_skill_generator.py --list

    # Process a range (for distributed runs)
    python scripts/llm_skill_generator.py --all --start 0 --count 100

Environment variables:
    OPENAI_API_KEY      OpenAI API key (preferred)
    ANTHROPIC_API_KEY   Anthropic API key (alternative)
    LLM_MODEL           Model to use (default: gpt-4o for OpenAI, claude-opus-4-5 for Anthropic)
    LLM_MIN_EXAMPLES    Minimum examples threshold; skip files above this (default: 5)
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, Optional, Tuple


# ─────────────────────────────────────────────────────────────────────────────
# Data loading helpers
# ─────────────────────────────────────────────────────────────────────────────

BASE_DIR = Path(__file__).parent.parent
METADATA_PATH = BASE_DIR / "data" / "bioconda_tools_metadata.jsonl"
DOCS_PATH = BASE_DIR / "data" / "bioconda_tools_docs.txt"
SKILL_DIR = BASE_DIR / "skill"
CHECK_SKILL_PATH = BASE_DIR / "check-skill" / "skill.md"


def load_metadata() -> Dict[str, Dict]:
    """Load all tool metadata from JSONL file."""
    meta = {}
    with open(METADATA_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                d = json.loads(line)
                meta[d["name"]] = d
    return meta


def load_docs() -> Dict[str, str]:
    """Load tool documentation from docs file, keyed by tool name."""
    docs = {}
    current_tool = None
    current_lines = []

    with open(DOCS_PATH, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("TOOL: "):
                if current_tool:
                    docs[current_tool] = "\n".join(current_lines)
                current_tool = line.split("TOOL: ", 1)[1].strip()
                current_lines = []
            elif current_tool:
                current_lines.append(line)
        if current_tool:
            docs[current_tool] = "\n".join(current_lines)

    return docs


def load_check_skill_methodology() -> str:
    """Load the check-skill methodology from the skill.md file."""
    if CHECK_SKILL_PATH.exists():
        return CHECK_SKILL_PATH.read_text(encoding="utf-8")
    return ""


def count_examples(skill_path: Path) -> int:
    """Count the number of examples in a skill file."""
    if not skill_path.exists():
        return 0
    content = skill_path.read_text(encoding="utf-8")
    return len(re.findall(r"^### ", content, re.MULTILINE))


def get_tools_needing_improvement(min_examples: int = 5) -> list:
    """Return list of tool names with fewer than min_examples examples."""
    needs_improvement = []
    for f in sorted(SKILL_DIR.glob("*.md")):
        if count_examples(f) < min_examples:
            needs_improvement.append(f.stem)
    return needs_improvement


# ─────────────────────────────────────────────────────────────────────────────
# Prompt construction
# ─────────────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are a bioinformatics expert and technical writer. Your task is to generate or improve oxo-call skill files for bioconda command-line tools.

A skill.md file is oxo-call's domain-expert knowledge injection unit with this structure:
1. YAML front-matter: name, category, description, tags, author, source_url
2. ## Concepts section (minimum 5 bullet points covering tool overview, I/O formats, key workflows, threading, important options)
3. ## Pitfalls section (minimum 3-5 bullet points covering common mistakes, argument ordering, version differences, gotchas)
4. ## Examples section (minimum 5 examples in this EXACT format):

### <description of what to do>
**Args:** `<command arguments without the tool name>`
**Explanation:** <why these flags were chosen, what the output will be>

CRITICAL RULES:
- The **Args:** value must start with the subcommand (for tools with subcommands) or the first flag/positional
- NEVER prefix Args with the tool name itself — just the arguments
- For tools with subcommands (samtools, bcftools, etc.): Args starts with the subcommand name
- Examples must be realistic and directly usable with real file extensions (.fastq, .bam, .vcf, etc.)
- The Explanation must explain WHY each flag was chosen, not just WHAT it does
- Standard categories: alignment, qc, variant-calling, expression, assembly, annotation, population-genomics, epigenomics, metagenomics, genome-editing, formatting, programming, containerization, hpc, utility
- Tags must include the tool name, file formats, and domain keywords
- source_url should be the best documentation URL (official docs, GitHub README, or bioconda page)

Write accurate, scientifically correct content based on your knowledge of the tool. The skill must reliably cover ≥99% of real-world usage.
"""


def build_prompt(tool_name: str, metadata: Dict, doc_text: str, existing_skill: str = "") -> str:
    """Build the LLM prompt for skill generation."""
    prompt_parts = []

    prompt_parts.append(f"Generate a comprehensive, accurate skill.md for the bioinformatics tool: **{tool_name}**\n")

    # Add metadata context
    if metadata:
        prompt_parts.append("## Available Metadata\n")
        prompt_parts.append(f"- **Name**: {metadata.get('name', tool_name)}")
        prompt_parts.append(f"- **Version**: {metadata.get('version', 'unknown')}")
        prompt_parts.append(f"- **Summary**: {metadata.get('summary', 'N/A')}")
        if metadata.get('description'):
            prompt_parts.append(f"- **Description**: {metadata['description'][:500]}")
        if metadata.get('home'):
            prompt_parts.append(f"- **Homepage**: {metadata['home']}")
        if metadata.get('doc_url'):
            prompt_parts.append(f"- **Documentation**: {metadata['doc_url']}")
        if metadata.get('dev_url'):
            prompt_parts.append(f"- **Development**: {metadata['dev_url']}")
        if metadata.get('license'):
            prompt_parts.append(f"- **License**: {metadata['license']}")
        if metadata.get('subdirs'):
            prompt_parts.append(f"- **Platforms**: {', '.join(metadata['subdirs'])}")
        prompt_parts.append("")

    # Add documentation context
    if doc_text:
        prompt_parts.append("## Tool Documentation\n")
        prompt_parts.append(doc_text[:2000])  # Limit to avoid token overflow
        prompt_parts.append("")

    # Add existing skill for reference
    if existing_skill and count_examples(Path("/dev/null")) == 0:
        # Just check if existing skill has content worth preserving
        existing_examples = len(re.findall(r"^### ", existing_skill, re.MULTILINE))
        if existing_examples > 0:
            prompt_parts.append("## Existing Skill File (improve this)\n")
            prompt_parts.append(existing_skill[:3000])
            prompt_parts.append("")

    prompt_parts.append(
        "Generate a complete, accurate skill.md file for this tool. "
        "Include at least 5 Concepts, 4 Pitfalls, and 6 Examples. "
        "Make the Examples realistic and directly usable. "
        "Output ONLY the skill.md content, starting with ---"
    )

    return "\n".join(prompt_parts)


# ─────────────────────────────────────────────────────────────────────────────
# LLM API callers
# ─────────────────────────────────────────────────────────────────────────────

def call_openai(prompt: str, model: str = "gpt-4o") -> Optional[str]:
    """Call OpenAI API to generate skill content."""
    try:
        import openai
    except ImportError:
        print("ERROR: openai package not installed. Run: pip install openai", file=sys.stderr)
        return None

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable not set", file=sys.stderr)
        return None

    client = openai.OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,  # Lower temperature for more consistent output
            max_tokens=4096,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"ERROR calling OpenAI API: {e}", file=sys.stderr)
        return None


def call_anthropic(prompt: str, model: str = "claude-opus-4-5") -> Optional[str]:
    """Call Anthropic API to generate skill content."""
    try:
        import anthropic
    except ImportError:
        print("ERROR: anthropic package not installed. Run: pip install anthropic", file=sys.stderr)
        return None

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY environment variable not set", file=sys.stderr)
        return None

    client = anthropic.Anthropic(api_key=api_key)

    try:
        message = client.messages.create(
            model=model,
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
        )
        return message.content[0].text
    except Exception as e:
        print(f"ERROR calling Anthropic API: {e}", file=sys.stderr)
        return None


def call_llm(prompt: str) -> Optional[str]:
    """Call the best available LLM API."""
    model = os.environ.get("LLM_MODEL", "")

    # Try OpenAI first
    if os.environ.get("OPENAI_API_KEY"):
        openai_model = model or "gpt-4o"
        print(f"  Using OpenAI ({openai_model})")
        return call_openai(prompt, model=openai_model)

    # Try Anthropic as fallback
    if os.environ.get("ANTHROPIC_API_KEY"):
        anthropic_model = model or "claude-opus-4-5"
        print(f"  Using Anthropic ({anthropic_model})")
        return call_anthropic(prompt, model=anthropic_model)

    print("ERROR: No LLM API key found. Set OPENAI_API_KEY or ANTHROPIC_API_KEY", file=sys.stderr)
    return None


# ─────────────────────────────────────────────────────────────────────────────
# Skill file writing and validation
# ─────────────────────────────────────────────────────────────────────────────

def validate_skill_content(content: str) -> Tuple[bool, str]:
    """Validate that the generated skill content has the required structure."""
    if not content.startswith("---"):
        return False, "Missing YAML front-matter (doesn't start with ---)"

    if "## Concepts" not in content:
        return False, "Missing ## Concepts section"

    if "## Pitfalls" not in content:
        return False, "Missing ## Pitfalls section"

    if "## Examples" not in content:
        return False, "Missing ## Examples section"

    examples = re.findall(r"^### ", content, re.MULTILINE)
    if len(examples) < 3:
        return False, f"Too few examples: {len(examples)} (need at least 3)"

    if "**Args:**" not in content:
        return False, "Examples missing **Args:** format"

    return True, "OK"


def write_skill(tool_name: str, content: str, backup: bool = True) -> bool:
    """Write skill content to file, optionally backing up existing file."""
    skill_path = SKILL_DIR / f"{tool_name}.md"

    # Clean up LLM output (remove markdown code blocks if present)
    content = content.strip()
    if content.startswith("```markdown\n"):
        content = content[len("```markdown\n"):]
    if content.startswith("```\n"):
        content = content[4:]
    if content.endswith("\n```"):
        content = content[:-4]
    if content.endswith("```"):
        content = content[:-3]
    content = content.strip()

    # Validate
    valid, message = validate_skill_content(content)
    if not valid:
        print(f"  WARNING: Validation failed for {tool_name}: {message}", file=sys.stderr)
        # Still write it but warn
        with open(SKILL_DIR / f"{tool_name}.validation_error.txt", "w") as f:
            f.write(f"Validation error: {message}\n\nContent:\n{content}")

    # Write the skill file
    skill_path.write_text(content + "\n", encoding="utf-8")
    return valid


# ─────────────────────────────────────────────────────────────────────────────
# Main processing
# ─────────────────────────────────────────────────────────────────────────────

def process_tool(
    tool_name: str,
    metadata_db: Dict,
    docs_db: Dict,
    min_examples: int = 5,
    force: bool = False,
) -> bool:
    """
    Process a single tool: generate or improve its skill file using the LLM.
    Returns True if the skill was updated, False if skipped.
    """
    skill_path = SKILL_DIR / f"{tool_name}.md"
    current_examples = count_examples(skill_path)

    # Skip if already good enough
    if not force and current_examples >= min_examples:
        print(f"  SKIP {tool_name}: already has {current_examples} examples (≥{min_examples})")
        return False

    print(f"  Processing {tool_name} (currently {current_examples} examples)...")

    # Get tool data
    metadata = metadata_db.get(tool_name, {})
    doc_text = docs_db.get(tool_name, "")
    existing_skill = skill_path.read_text(encoding="utf-8") if skill_path.exists() else ""

    # Build prompt
    prompt = build_prompt(tool_name, metadata, doc_text, existing_skill)

    # Call LLM
    result = call_llm(prompt)
    if not result:
        print(f"  FAILED {tool_name}: LLM returned no content")
        return False

    # Write skill
    valid = write_skill(tool_name, result)
    new_examples = count_examples(SKILL_DIR / f"{tool_name}.md")

    status = "✓" if valid else "⚠"
    print(f"  {status} {tool_name}: {current_examples} → {new_examples} examples")

    # Rate limit: avoid hitting API rate limits
    time.sleep(0.5)

    return True


def main():
    parser = argparse.ArgumentParser(
        description="LLM-based bioconda skill generator using check-skill methodology"
    )
    parser.add_argument(
        "tools",
        nargs="*",
        help="Tool name(s) to process. If none, use --all or --list",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Process all tools needing improvement",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List tools needing improvement without processing",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force regeneration even if the skill file already has enough examples",
    )
    parser.add_argument(
        "--min-examples",
        type=int,
        default=int(os.environ.get("LLM_MIN_EXAMPLES", "5")),
        help="Minimum examples threshold (default: 5)",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=0,
        help="Start index when using --all (for distributed processing)",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=0,
        help="Number of tools to process when using --all (0 = all)",
    )
    args = parser.parse_args()

    SKILL_DIR.mkdir(exist_ok=True)

    if args.list or (not args.tools and not args.all):
        tools = get_tools_needing_improvement(args.min_examples)
        print(f"Tools needing improvement (< {args.min_examples} examples): {len(tools)}")
        for t in tools:
            examples = count_examples(SKILL_DIR / f"{t}.md")
            print(f"  {t} ({examples} examples)")
        return

    # Load data
    print("Loading metadata and documentation...")
    metadata_db = load_metadata()
    docs_db = load_docs()
    print(f"  Loaded {len(metadata_db)} tools from metadata")
    print(f"  Loaded {len(docs_db)} tools from docs")

    # Determine tools to process
    if args.all:
        tools = get_tools_needing_improvement(args.min_examples)
        if args.start > 0:
            tools = tools[args.start:]
        if args.count > 0:
            tools = tools[: args.count]
        print(f"Processing {len(tools)} tools...")
    else:
        tools = args.tools

    # Process tools
    updated = 0
    skipped = 0
    failed = 0

    for i, tool_name in enumerate(tools, 1):
        print(f"\n[{i}/{len(tools)}] {tool_name}")
        try:
            result = process_tool(
                tool_name,
                metadata_db,
                docs_db,
                min_examples=args.min_examples,
                force=args.force,
            )
            if result:
                updated += 1
            else:
                skipped += 1
        except KeyboardInterrupt:
            print("\nInterrupted by user")
            break
        except Exception as e:
            print(f"  ERROR processing {tool_name}: {e}", file=sys.stderr)
            failed += 1

    print(f"\n{'='*60}")
    print(f"Completed: {updated} updated, {skipped} skipped, {failed} failed")
    print(f"Skill files are in: {SKILL_DIR}")


if __name__ == "__main__":
    main()
