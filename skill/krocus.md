---
name: krocus
category: metagenomics
description: krocus performs multi-locus sequence typing from uncorrected long reads.
tags: [krocus, metagenomics]
author: oxo-call-community
source_url: "https://github.com/andrewjpage/krocus"
---

## Concepts

- **Tool Overview**: krocus v1.0.3 - Krocus can predict a sequence type directly from uncorrected long reads, and was designed to consume read data as it is produced, providing results in minutes..
- **Core Function**: krocus performs multi-locus sequence typing from uncorrected long reads.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda krocus`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Predict MLST
**Args:** `krocus -i reads.fastq -d mlst_db`
**Explanation:** Predicts MLST from sequencing reads using k-mer approach.

