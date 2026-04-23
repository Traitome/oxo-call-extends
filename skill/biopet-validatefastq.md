---
name: biopet-validatefastq
category: qc
description: This tool validates a FASTQ file.
tags: [biopet-validatefastq, qc, FASTQ, SAM]
author: oxo-call-community
source_url: "https://github.com/biopet/validatefastq"
---

## Concepts

- **Tool Overview**: biopet-validatefastq (v0.1.1) - This tool validates a FASTQ file.
- **Core Function**: This tool validates a FASTQ file. When data is paired it can also validate a pair of FASTQ files. ValidateFastq will check if the FASTQ is in valid FASTQ format. This includes checking for duplicate r...
- **Input/Output**: FASTQ input; processed output
- **Installation**: `conda install -c bioconda biopet-validatefastq`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Perform quality control analysis
