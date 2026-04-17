# oxo-call-extends

Bioconda command-line tools catalog for the [oxo-call](https://github.com/Traitome/oxo-call) project.

This repository maintains a comprehensive, regularly-updated catalog of bioconda
command-line bioinformatics tools with structured metadata for tool discovery,
index building, and integration into the oxo-call ecosystem.

## Contents

```
data/
├── bioconda_cli_tools.txt          # One tool name per line (6,000+ CLI tools)
├── bioconda_tools_metadata.jsonl   # Structured metadata per tool (JSON Lines)
├── bioconda_tools_docs.txt         # Formatted documentation archive for indexing
└── bioconda_excluded_packages.txt  # Excluded non-CLI packages with reasons

scripts/
├── fetch_bioconda_tools.py         # Fetch and classify bioconda packages
└── generate_tool_docs.py           # Generate formatted documentation archive
```

## Data Files

### `bioconda_cli_tools.txt`

Plain text list of all bioconda command-line tools, one per line. Comments at the
top provide summary statistics. This is the primary reference for which bioconda
packages are command-line tools.

### `bioconda_tools_metadata.jsonl`

[JSON Lines](https://jsonlines.org/) file where each line is a JSON object with:

| Field           | Description                                         |
| --------------- | --------------------------------------------------- |
| `name`          | Package name (e.g., `samtools`)                     |
| `version`       | Latest version                                      |
| `summary`       | One-line description                                |
| `description`   | Extended description (when available)               |
| `home`          | Project homepage URL                                |
| `doc_url`       | Official documentation URL                          |
| `dev_url`       | Development/source repository URL                   |
| `license`       | Software license                                    |
| `subdirs`       | Supported platforms (`linux-64`, `osx-arm64`, etc.) |
| `source_url`    | Source code download URL                            |
| `binary_prefix` | Whether the package installs compiled binaries      |
| `text_prefix`   | Whether the package installs scripts                |

### `bioconda_tools_docs.txt`

Human-readable, structured documentation archive optimized for full-text
indexing. Each tool entry includes version, summary, description, all URLs,
license, platforms, and installation command.

### `bioconda_excluded_packages.txt`

Tab-separated list of excluded packages with the reason for exclusion. Excluded
categories:

- **R packages** (`r-*`) — R language libraries
- **Bioconductor packages** (`bioconductor-*`) — R/Bioconductor libraries
- **Perl modules** (`perl-*`) — Perl language modules
- **Python libraries** (`python-*`) — Python language bindings
- **Framework plugins** — Snakemake plugins, Galaxy libraries, Flask extensions
- **Library packages** — Packages whose summary indicates library/API/SDK usage

## Usage

### Regenerate the catalog

Requires Python 3.7+ (no additional dependencies).

```bash
# Step 1: Fetch and classify packages from bioconda channel
python scripts/fetch_bioconda_tools.py

# Step 2: Generate formatted documentation archive
python scripts/generate_tool_docs.py
```

### Use in oxo-call

The data files can be used directly for:

- **Index building**: Parse `bioconda_tools_metadata.jsonl` for structured data
  or `bioconda_tools_docs.txt` for full-text indexing
- **Tool discovery**: Search `bioconda_cli_tools.txt` for available tools
- **Documentation lookup**: Use `doc_url` and `home` fields from the metadata to
  locate official documentation for specific tools

## Methodology

### Data Source

All data is sourced from the official bioconda conda channel metadata at:
`https://conda.anaconda.org/bioconda/channeldata.json`

### Classification

Packages are classified as CLI tools using a multi-layer heuristic:

1. **Prefix exclusion**: Packages with known library prefixes (`bioconductor-`,
   `r-`, `perl-`, `python-`) are excluded
2. **Framework exclusion**: Plugin/extension packages for workflow frameworks are
   excluded
3. **Summary analysis**: Packages whose summary contains library-indicator
   keywords (e.g., "python library", "API client") are excluded
4. **Default inclusion**: All remaining packages are included as potential CLI
   tools

This approach errs on the side of inclusion — some packages that are primarily
libraries but also provide CLI tools are retained.

## License

This project is part of the [Traitome](https://github.com/Traitome) organization.