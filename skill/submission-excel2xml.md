---
name: submission-excel2xml
category: utility
description: Generate DRA metadata XML files from Excel spreadsheet
tags: [submission-excel2xml, utility, xml]
author: oxo-call-community
source_url: "https://github.com/ddbj/submission-excel2xml"
---

## Concepts

- **Tool Overview**: submission-excel2xml (v3.6.2) - Generate DRA metadata XML files from Excel spreadsheet
- **Core Function**: Generate DRA metadata XML files from Excel spreadsheet
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda submission-excel2xml`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `submission-excel2xml -i <input_file> -o <output_file>`
**Explanation:** Run submission-excel2xml with typical input and output options.
