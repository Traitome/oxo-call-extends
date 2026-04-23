---
name: consent
category: alignment
description: Scalable long read self-correction and assembly polishing with multiple sequence alignment.
tags: [consent, alignment]
author: oxo-call-community
source_url: "https://github.com/morispi/CONSENT/blob/v2.2.2/README.md"
---

## Concepts

- **Tool Overview**: consent (v2.2.2) - Scalable long read self-correction and assembly polishing with multiple sequence alignment.
- **Core Function**: Scalable long read self-correction and assembly polishing with multiple sequence alignment.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda consent`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Align reads to a reference genome
