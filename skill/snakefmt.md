---
name: snakefmt
category: formatting
description: snakefmt - The uncompromising Snakemake code formatter
tags: [snakefmt, formatting, snakemake, code-formatting, linting]
author: oxo-call-community
source_url: "https://github.com/snakemake/snakefmt"
---

## Concepts

- **Tool Overview**: snakefmt (v1.0.0) - A code formatter for Snakemake workflow files
- **Core Function**: Formats Snakemake files according to style guidelines
- **Input/Output**: Accepts Snakefile or Snakemake config files; outputs formatted files
- **Algorithm**: Parses Snakemake syntax and applies consistent formatting rules
- **Installation**: `conda install -c bioconda snakefmt`
- **Key Features**: Consistent formatting, syntax validation, integration with CI/CD

## Pitfalls

- **Formatting Changes**: May change existing formatting unexpectedly
- **Syntax Errors**: Will fail on invalid Snakemake syntax
- **Version Compatibility**: May not support all Snakemake syntax versions
- **Configuration**: Custom format rules require config file
- **File Overwriting**: By default overwrites original files
- **Comments**: May reformat comments in unexpected ways

## Examples

### Display help
**Args:** `snakefmt --help`
**Explanation:** Shows available options and usage information.

### Format Snakefile
**Args:** `snakefmt Snakefile`
**Explanation:** Format Snakefile in place.

### Format multiple files
**Args:** `snakefmt Snakefile rules/`
**Explanation:** Format Snakefile and all files in rules directory.

### Check formatting only
**Args:** `snakefmt --check Snakefile`
**Explanation:** Check if file needs formatting without modifying.

### Output to different file
**Args:** `snakefmt Snakefile --output formatted_Snakefile`
**Explanation:** Write formatted output to different file.

### Recursive formatting
**Args:** `snakefmt --recursive .`
**Explanation:** Format all Snakemake files recursively.

### Custom configuration
**Args:** `snakefmt --config snakefmt.toml Snakefile`
**Explanation:** Use custom formatting configuration.

### Show diff
**Args:** `snakefmt --diff Snakefile`
**Explanation:** Show diff of formatting changes.