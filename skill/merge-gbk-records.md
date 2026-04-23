---
name: merge-gbk-records
category: utility
description: Turn multiple GenBank records (either in multiple files or a single multi-record file) into a single record
tags: [merge-gbk-records, utility]
author: oxo-call-community
source_url: "http://github.com/kblin/merge-gbk-records"
---

## Concepts

- **Tool Overview**: merge-gbk-records v0.2.0 - A small script to turn multiple GenBank records (either in multiple files or a single multi-record file) into a single record. Sequences are merged by concatenating them in order, and putting a spacer sequence between them. Spacer sequence length can be given in kbp. It is possible to pick an all-N spacer, or using a spacer consisting of all-frame stop codons..
- **Core Function**: Turn multiple GenBank records (either in multiple files or a single multi-record file) into a single record
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda merge-gbk-records`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
