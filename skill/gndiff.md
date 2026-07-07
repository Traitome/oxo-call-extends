---
name: gndiff
category: utility
description: GNdiff compares scientific names from two files, supporting plain text lists, CSV, and TSV formats with scientificName field.
tags: [gndiff, utility, scientific-names, taxonomy, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/gnames/gndiff"
---

## Concepts

- **Scientific Name Comparison**: GNdiff is a tool for comparing scientific names between two files - a source file containing names to be matched and a reference file containing authoritative names. It supports batch comparison of taxonomic names for biodiversity and bioinformatics workflows.

- **Input Format Support**: GNdiff accepts three input formats: (1) plain text files with one scientific name per line, (2) CSV files with a `scientificName` field, and (3) TSV files with a `scientificName` field. The tool automatically detects the format based on file extension.

- **Output Formats**: Results can be output in multiple formats including CSV (default), TSV, compact JSON (single line), and pretty JSON (human-readable with indentation). Use the --format flag to specify the desired output format.

- **Quiet Mode**: The --quiet flag suppresses warning logs, showing only matching results on STDOUT. This is useful when redirecting output to a file or when integrating GNdiff into automated pipelines.

- **POSIX Compliance**: According to POSIX standards, flags and options can be given either before or after name strings or file names, providing flexibility in command construction.

## Pitfalls

- **File Format Detection**: The tool relies on file extensions (.csv, .tsv, .txt) to determine input format. Files with non-standard extensions may not be parsed correctly. Ensure your input files have appropriate extensions.

- **scientificName Field Case Sensitivity**: The `scientificName` field name must be exact (case-sensitive). If your CSV/TSV uses a different field name (e.g., `scientific_name` or `ScientificName`), GNdiff will not recognize it.

- **STDOUT vs STDERR**: Matching results are written to STDOUT while warnings go to STDERR. When redirecting output to a file, remember that warnings will still appear in the terminal unless you redirect STDERR to /dev/null.

- **Missing Values**: Empty cells or lines in the input files may cause unexpected behavior. Pre-clean your data to remove empty entries before running GNdiff.

- **Encoding Issues**: Scientific names with special characters or Unicode characters may cause matching issues. Ensure your input files use consistent encoding (UTF-8 recommended).

## Examples

### Compare two simple name lists
**Args:** `source.txt reference.txt`
**Explanation:** The simplest usage compares two plain text files, each containing one scientific name per line. The first file (source.txt) contains names to be matched against the reference names in the second file (reference.txt). Output is in CSV format by default.

### Output results in pretty JSON format
**Args:** `source.txt reference.txt --format=pretty`
**Explanation:** The --format flag controls output format. Using "pretty" produces human-readable JSON with proper indentation and line breaks, making it easier to inspect detailed matching results and metadata.

### Suppress warnings with quiet mode
**Args:** `source.csv reference.csv -q`
**Explanation:** The -q (or --quiet) flag suppresses all warning messages, displaying only the matching results. This is essential when running GNdiff in scripts where warning messages would interfere with parsing or when you only need the matched names.

### Redirect stderr to suppress warnings
**Args:** `source.txt reference.txt 2> /dev/null`
**Explanation:** An alternative to quiet mode is redirecting STDERR to /dev/null. This achieves similar results but at the shell level. Use this approach when you want to keep the original output format but hide warnings.

### Use tab-separated input with scientificName field
**Args:** `source.tsv reference.tsv -f compact`
**Explanation:** For TSV files containing a `scientificName` column, GNdiff extracts and compares those values. The -f compact outputs results as single-line JSON, which is useful for high-throughput processing.

### Get version information
**Args:** `-V`
**Explanation:** The -V or --version flag displays GNdiff version information. This is useful for checking installation and for reporting issues or citing the tool in publications.
