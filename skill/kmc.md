---
name: kmc
category: utility
description: Tools for efficient k-mer counting and filtering of reads based on k-mer content.
tags: [kmc, utility]
author: oxo-call-community
source_url: "https://github.com/refresh-bio/kmc"
---

## Concepts

- **Tool Overview**: kmc v3.2.4 - KMC is a utility designed for counting k-mers (sequences of consecutive k symbols) in a set of DNA sequences. KMC tools allow performing various operations on k-mers sets..
- **Core Function**: Tools for efficient k-mer counting and filtering of reads based on k-mer content.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kmc`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Count k-mers
**Args:** `kmc -k21 -t4 input.fastq output kmc_tmp`
**Explanation:** Counts 21-mers from FASTQ using 4 threads.

