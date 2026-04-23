---
name: bcl2fastq-nextseq
category: qc
description: NextSeq .bcl Conversion
tags: [bcl2fastq-nextseq, qc, FASTQ]
author: oxo-call-community
source_url: "https://github.com/brwnj/bcl2fastq"
---

## Concepts

- **Tool Overview**: bcl2fastq-nextseq (v1.3.0) - NextSeq .bcl Conversion
- **Core Function**: NextSeq .bcl Conversion
- **Input/Output**: FASTQ input; processed output
- **Installation**: `conda install -c bioconda bcl2fastq-nextseq`

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
