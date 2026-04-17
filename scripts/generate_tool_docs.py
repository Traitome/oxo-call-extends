#!/usr/bin/env python3
"""
Generate formatted documentation archive for bioconda CLI tools.

Reads the metadata from data/bioconda_tools_metadata.jsonl and produces
a structured plain-text documentation file optimized for index building
and use in the oxo-call project.

Each tool entry includes:
  - Tool name and version
  - One-line summary
  - Detailed description (if available)
  - Homepage, documentation, and development URLs
  - License information
  - Supported platforms
  - Source URL

Outputs:
  - data/bioconda_tools_docs.txt : Formatted documentation archive

Usage:
    python scripts/generate_tool_docs.py
"""

import json
import os
import sys
from datetime import datetime, timezone

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
METADATA_FILE = os.path.join(DATA_DIR, "bioconda_tools_metadata.jsonl")
OUTPUT_FILE = os.path.join(DATA_DIR, "bioconda_tools_docs.txt")

PLATFORM_LABELS = {
    "linux-64": "Linux (x86_64)",
    "linux-aarch64": "Linux (ARM64)",
    "osx-64": "macOS (x86_64)",
    "osx-arm64": "macOS (ARM64/Apple Silicon)",
    "noarch": "Platform-independent",
}

BIOCONDA_PACKAGE_URL = "https://bioconda.github.io/recipes/{name}/README.html"


def format_tool_entry(record):
    """Format a single tool record into documentation text."""
    lines = []

    name = record["name"]
    version = record.get("version", "")
    summary = record.get("summary", "").strip()
    description = record.get("description", "").strip()
    home = record.get("home", "").strip()
    doc_url = record.get("doc_url", "").strip()
    dev_url = record.get("dev_url", "").strip()
    license_info = record.get("license", "").strip()
    subdirs = record.get("subdirs", [])
    source_url_raw = record.get("source_url", "")
    if isinstance(source_url_raw, list):
        source_url = ", ".join(str(u).strip() for u in source_url_raw)
    else:
        source_url = str(source_url_raw).strip()

    # Header
    lines.append(f"{'=' * 78}")
    lines.append(f"TOOL: {name}")
    lines.append(f"{'=' * 78}")

    # Version
    if version:
        lines.append(f"Version: {version}")

    # Summary
    if summary:
        lines.append(f"Summary: {summary}")

    # Detailed description
    if description:
        lines.append(f"")
        lines.append(f"Description:")
        # Word-wrap description at ~76 chars
        words = description.split()
        current_line = "  "
        for word in words:
            if len(current_line) + len(word) + 1 > 76:
                lines.append(current_line)
                current_line = "  " + word
            else:
                current_line += " " + word if current_line.strip() else "  " + word
        if current_line.strip():
            lines.append(current_line)

    # URLs
    lines.append("")
    bioconda_url = BIOCONDA_PACKAGE_URL.format(name=name)
    lines.append(f"Bioconda page: {bioconda_url}")
    if home:
        lines.append(f"Homepage:      {home}")
    if doc_url:
        lines.append(f"Documentation: {doc_url}")
    if dev_url:
        lines.append(f"Development:   {dev_url}")
    if source_url:
        lines.append(f"Source:        {source_url}")

    # License
    if license_info:
        lines.append(f"License:       {license_info}")

    # Platforms
    if subdirs:
        platforms = [PLATFORM_LABELS.get(s, s) for s in subdirs]
        lines.append(f"Platforms:     {', '.join(platforms)}")

    # Installation
    lines.append("")
    lines.append(f"Installation:")
    lines.append(f"  conda install -c bioconda {name}")

    lines.append("")
    return "\n".join(lines)


def main():
    if not os.path.exists(METADATA_FILE):
        print(f"Error: {METADATA_FILE} not found.")
        print("Run scripts/fetch_bioconda_tools.py first.")
        return 1

    # Read metadata
    tools = []
    with open(METADATA_FILE) as f:
        for line in f:
            line = line.strip()
            if line:
                tools.append(json.loads(line))

    print(f"Read {len(tools)} tool records from {METADATA_FILE}")

    # Generate documentation
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(OUTPUT_FILE, "w") as f:
        # File header
        f.write("#" * 78 + "\n")
        f.write("# Bioconda Command-Line Tools Documentation Archive\n")
        f.write("#\n")
        f.write(f"# Generated: {now}\n")
        f.write(f"# Total tools: {len(tools)}\n")
        f.write("# Source: https://conda.anaconda.org/bioconda/channeldata.json\n")
        f.write("#\n")
        f.write("# This file contains structured metadata for bioconda CLI tools,\n")
        f.write("# optimized for full-text indexing and use in the oxo-call project.\n")
        f.write("# Each entry includes tool name, version, summary, description,\n")
        f.write("# homepage, documentation URLs, license, and platform support.\n")
        f.write("#\n")
        f.write("# For detailed command-line options and usage, consult the\n")
        f.write("# documentation URL or homepage listed for each tool.\n")
        f.write("#" * 78 + "\n\n")

        # Tool entries
        for tool in tools:
            f.write(format_tool_entry(tool))

        # Footer
        f.write("=" * 78 + "\n")
        f.write(f"END OF DOCUMENTATION — {len(tools)} tools cataloged\n")
        f.write("=" * 78 + "\n")

    file_size = os.path.getsize(OUTPUT_FILE)
    print(f"Wrote documentation to {OUTPUT_FILE}")
    print(f"  File size: {file_size / 1024:.1f} KB")
    print(f"  Tools documented: {len(tools)}")

    # Stats
    with_home = sum(1 for t in tools if t.get("home"))
    with_doc = sum(1 for t in tools if t.get("doc_url"))
    with_dev = sum(1 for t in tools if t.get("dev_url"))
    with_desc = sum(1 for t in tools if t.get("description"))
    with_summary = sum(1 for t in tools if t.get("summary"))

    print(f"\nCoverage statistics:")
    print(f"  With summary:       {with_summary:>5} ({100*with_summary/len(tools):.1f}%)")
    print(f"  With description:   {with_desc:>5} ({100*with_desc/len(tools):.1f}%)")
    print(f"  With homepage:      {with_home:>5} ({100*with_home/len(tools):.1f}%)")
    print(f"  With doc URL:       {with_doc:>5} ({100*with_doc/len(tools):.1f}%)")
    print(f"  With dev URL:       {with_dev:>5} ({100*with_dev/len(tools):.1f}%)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
