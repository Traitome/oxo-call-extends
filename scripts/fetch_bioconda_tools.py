#!/usr/bin/env python3
"""
Fetch and classify bioconda packages into CLI tools vs non-CLI software.

This script downloads the bioconda channel metadata and applies heuristic
filtering to identify command-line bioinformatics tools, excluding:
  - R packages (r-*)
  - Bioconductor packages (bioconductor-*)
  - Perl modules (perl-*)
  - Python library bindings (python-*)
  - Snakemake plugins (snakemake-executor-plugin-*, snakemake-storage-plugin-*, etc.)
  - Galaxy framework libraries (galaxy-*)
  - Flask web framework extensions (flask-*)
  - Pure library/API packages identified by summary keywords

Outputs:
  - data/bioconda_cli_tools.txt          : One tool name per line
  - data/bioconda_tools_metadata.jsonl   : Full metadata per tool (JSON Lines)
  - data/bioconda_excluded_packages.txt  : Excluded packages with reasons

Usage:
    python scripts/fetch_bioconda_tools.py
"""

import json
import os
import sys
import urllib.request

CHANNEL_DATA_URL = "https://conda.anaconda.org/bioconda/channeldata.json"
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")

# Prefixes that indicate language-specific library packages (not CLI tools)
LIBRARY_PREFIXES = (
    "bioconductor-",
    "r-",
    "perl-",
    "python-",
)

# Prefixes for framework plugin/extension packages (not standalone CLI tools)
FRAMEWORK_PREFIXES = (
    "snakemake-executor-plugin-",
    "snakemake-storage-plugin-",
    "snakemake-report-plugin-",
    "snakemake-interface-",
    "galaxy-",
    "flask-",
)

# Keywords in summary that strongly indicate a non-CLI library
LIBRARY_SUMMARY_KEYWORDS = [
    "python library",
    "python package",
    "python module",
    "python bindings",
    "python wrapper",
    "python interface",
    "r package",
    "r library",
    "perl module",
    "perl library",
    "java library",
    "javascript library",
    "ruby gem",
    "api client",
    "api wrapper",
    "sdk for",
]

# Known non-CLI package names (manually curated edge cases)
KNOWN_NON_CLI = {
    "snakemake-wrapper-utils",
}


def download_channel_data():
    """Download bioconda channel metadata."""
    print(f"Downloading bioconda channel data from {CHANNEL_DATA_URL} ...")
    req = urllib.request.Request(
        CHANNEL_DATA_URL,
        headers={"User-Agent": "oxo-call-extends/1.0"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        raw = resp.read()
    data = json.loads(raw)
    print(f"  Retrieved {len(data.get('packages', {}))} packages.")
    return data


def classify_package(name, meta):
    """
    Classify a package as CLI tool or non-CLI.

    Returns:
        (is_cli_tool: bool, reason: str)
    """
    # 1. Exclude by prefix
    for prefix in LIBRARY_PREFIXES:
        if name.startswith(prefix):
            return False, f"library prefix: {prefix}"

    for prefix in FRAMEWORK_PREFIXES:
        if name.startswith(prefix):
            return False, f"framework plugin prefix: {prefix}"

    # 2. Exclude known non-CLI
    if name in KNOWN_NON_CLI:
        return False, "known non-CLI package"

    # 3. Check summary for library keywords
    summary = (meta.get("summary") or "").lower()
    for kw in LIBRARY_SUMMARY_KEYWORDS:
        if kw in summary:
            return False, f"summary contains library keyword: '{kw}'"

    # All remaining packages are considered potential CLI tools
    return True, "passed all filters"


def build_tool_record(name, meta):
    """Build a structured metadata record for a CLI tool."""
    return {
        "name": name,
        "version": meta.get("version", ""),
        "summary": meta.get("summary", ""),
        "home": meta.get("home", ""),
        "doc_url": meta.get("doc_url", ""),
        "dev_url": meta.get("dev_url", ""),
        "license": meta.get("license", ""),
        "subdirs": meta.get("subdirs", []),
        "binary_prefix": meta.get("binary_prefix", False),
        "text_prefix": meta.get("text_prefix", False),
        "source_url": meta.get("source_url", ""),
        "description": meta.get("description", ""),
    }


def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    data = download_channel_data()
    packages = data.get("packages", {})

    cli_tools = []
    excluded = []

    for name in sorted(packages.keys()):
        meta = packages[name]
        is_cli, reason = classify_package(name, meta)
        if is_cli:
            cli_tools.append((name, meta))
        else:
            excluded.append((name, reason))

    # Write CLI tool names
    tools_txt = os.path.join(DATA_DIR, "bioconda_cli_tools.txt")
    with open(tools_txt, "w") as f:
        f.write(f"# Bioconda Command-Line Tools\n")
        f.write(f"# Total: {len(cli_tools)} tools\n")
        f.write(f"# Source: {CHANNEL_DATA_URL}\n")
        f.write(f"# Excluded: {len(excluded)} non-CLI packages "
                f"(R/Bioconductor/Perl/Python libraries, framework plugins, etc.)\n")
        f.write("#\n")
        for name, _ in cli_tools:
            f.write(f"{name}\n")
    print(f"Wrote {len(cli_tools)} CLI tools to {tools_txt}")

    # Write full metadata as JSON Lines
    metadata_jsonl = os.path.join(DATA_DIR, "bioconda_tools_metadata.jsonl")
    with open(metadata_jsonl, "w") as f:
        for name, meta in cli_tools:
            record = build_tool_record(name, meta)
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"Wrote metadata to {metadata_jsonl}")

    # Write excluded packages
    excluded_txt = os.path.join(DATA_DIR, "bioconda_excluded_packages.txt")
    with open(excluded_txt, "w") as f:
        f.write(f"# Excluded Bioconda Packages (non-CLI)\n")
        f.write(f"# Total: {len(excluded)} packages\n")
        f.write("#\n")
        for name, reason in excluded:
            f.write(f"{name}\t{reason}\n")
    print(f"Wrote {len(excluded)} excluded packages to {excluded_txt}")

    # Summary
    print(f"\nSummary:")
    print(f"  Total bioconda packages: {len(packages)}")
    print(f"  CLI tools identified:    {len(cli_tools)}")
    print(f"  Excluded (non-CLI):      {len(excluded)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
