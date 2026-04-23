---
name: ucsc-bedjointaboffset
category: utility
description: given a bed file and tab file where each have a column with matching values: first get the value of column0, the offset and line length from inTabFile. Then go over the bed file, use the name field and append its offset and length to the bed file as two separate fields. Write the new bed file to outBed.
tags: [ucsc-bedjointaboffset, utility]
author: oxo-call-community
source_url: "http://hgdownload.cse.ucsc.edu/admin/exe/"
---

## Concepts

- **Tool Overview**: ucsc-bedjointaboffset (v377) - given a bed file and tab file where each have a column with matching values: first get the value of column0, the offset and line length from inTabFile. Then go over the bed file, use the name field and append its offset and length to the bed file as two separate fields. Write the new bed file to outBed.
- **Core Function**: given a bed file and tab file where each have a column with matching values: first get the value of column0, the offset and line length from inTabFile. Then go over the bed file, use the name field and append its offset and length to the bed file as two separate fields. Write the new bed file to outBed.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda ucsc-bedjointaboffset`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
