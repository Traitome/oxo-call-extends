---
name: tbl2asn-forever
category: utility
description: tbl2asn is a program that automates the creation of sequence records for submission to GenBank
tags: [tbl2asn-forever, utility]
author: oxo-call-community
source_url: "https://www.ncbi.nlm.nih.gov/genbank/tbl2asn2"
---

## Concepts

- **Tool Overview**: tbl2asn-forever (v25.7.2f) - tbl2asn is a program that automates the creation of sequence records for submission to GenBank
- **Core Function**: tbl2asn is a program that automates the creation of sequence records for submission to GenBank
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda tbl2asn-forever`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `tbl2asn-forever -i <input_file> -o <output_file>`
**Explanation:** Run tbl2asn-forever with typical input and output options.
