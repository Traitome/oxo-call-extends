---
name: table2asn
category: utility
description: table2asn is a command-line program that creates sequence records for submission to GenBank - replaces tbl2asn.
tags: [table2asn, utility]
author: oxo-call-community
source_url: "https://ftp.ncbi.nlm.nih.gov/asn1-converters/by_program/table2asn/DOCUMENTATION/table2asn_readme.txt"
---

## Concepts

- **Tool Overview**: table2asn (v1.28.1179) - table2asn is a command-line program that creates sequence records for submission to GenBank - replaces tbl2asn.
- **Core Function**: table2asn is a command-line program that creates sequence records for submission to GenBank - replaces tbl2asn.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda table2asn`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `table2asn -i <input_file> -o <output_file>`
**Explanation:** Run table2asn with typical input and output options.
