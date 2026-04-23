---
name: binny
category: metagenomics
description: Automated binning algorithm to recover high-quality genomes from complex metagenomes
tags: [mag, binning, metagenomics, automated]
author: oxo-call-community
source_url: "https://github.com/a-h-b/binny"
---

## Concepts
- **Tool Overview**: binny is an automated binning algorithm designed to recover high-quality MAGs from complex metagenomic datasets. It uses coverage and composition information for binning.
- **Automated Binning**: Requires minimal parameter tuning; automatically determines optimal binning parameters.
- **Quality Focus**: Prioritizes recovery of high-quality, low-contamination genomes.
- **Applications**: Metagenome-assembled genome recovery from environmental and clinical samples.

## Pitfalls
- **Coverage Requirement**: Requires multiple coverage profiles from different samples for optimal performance.
- **Complex Communities**: Very complex communities may still yield fragmented bins.

## Examples
### Run automated binning
**Args:** `binny --assembly contigs.fa --coverage coverage.tsv --output bins/`
**Explanation:** Performs automated binning with coverage and composition profiles.

### Specify minimum bin size
**Args:** `binny --assembly contigs.fa --coverage coverage.tsv --min-size 500000 --output bins/`
**Explanation:** Only outputs bins larger than 500kb.
