---
name: primer3
category: qc
description: Design PCR primers from DNA sequence. From mispriming libraries to sequence quality data to the generation of internal oligos, primer3 does it.
tags: ["primer3", "qc"]
author: oxo-call-community
source_url: "https://github.com/primer3-org/primer3"
---

## Concepts

- **Tool Overview**: Design PCR primers from DNA sequence. From mispriming libraries to sequence quality data to the generation of internal oligos, primer3 does it. (version 2.6.1)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda primer3`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Quality check
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Generates quality control metrics and reports.

