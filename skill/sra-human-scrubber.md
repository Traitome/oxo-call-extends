---
name: sra-human-scrubber
category: qc
description: An SRA tool identifies and removes any significant human read, and outputs the edited (cleaned) fastq file for SRA submission.
tags: [sra-human-scrubber, qc, fastq]
author: oxo-call-community
source_url: "https://github.com/ncbi/sra-human-scrubber"
---

## Concepts

- **Tool Overview**: sra-human-scrubber (v2.2.1) - An SRA tool identifies and removes any significant human read, and outputs the edited (cleaned) fastq file for SRA submission.
- **Core Function**: An SRA tool identifies and removes any significant human read, and outputs the edited (cleaned) fastq file for SRA submission.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda sra-human-scrubber`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `sra-human-scrubber -i <input.fastq> -o <output_dir>`
**Explanation:** Run sra-human-scrubber with typical input and output options.
