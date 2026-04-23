---
name: fastq-fix-i5
category: formatting
description: Rewrite FASTQ headers by reverse-complementing the i5 (Index2/P5) barcode in :i7+i5
tags: [fastq-fix-i5, formatting]
author: oxo-call-community
source_url: "https://github.com/ssciwr/fastq-fix-i5"
---

## Concepts
- **Tool Overview**: A fast, streaming tool to rewrite FASTQ headers by reverse-complementing the i5 (Index2 / P5) barcode, without modifying read sequences or quality scores. Headers are expected to end with the standard Illumina `:<i7>+<i5>` format.
- **Core Function**: Rewrite FASTQ headers by reverse-complementing the i5 (Index2/P5) barcode in :i7+i5
- **Input/Output**: Depends on tool configuration and data formats.
- **Installation**: `conda install -c bioconda fastq-fix-i5`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
