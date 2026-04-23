---
name: ddrage
category: formatting
description: Simulator for ddRADseq (double digest restriction site associated DNA sequencing) datasets. Generates reads (FASTQ format) that can be analyzed and validated using a ground truth file (YAML).
tags: [ddrage, formatting, FASTQ]
author: oxo-call-community
source_url: "https://bitbucket.org/genomeinformatics/rage"
---

## Concepts

- **Tool Overview**: ddrage (v1.8.1) - Simulator for ddRADseq (double digest restriction site associated DNA sequencing) datasets. Generates reads (FASTQ format) that can be analyzed and validated using a ground truth file (YAML).
- **Core Function**: Simulator for ddRADseq (double digest restriction site associated DNA sequencing) datasets. Generates reads (FASTQ format) that can be analyzed and validated using a ground truth file (YAML).
- **Input/Output**: FASTQ input; processed output
- **Installation**: `conda install -c bioconda ddrage`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i input.gff -o output.gtf`
**Explanation:** Convert between file formats
