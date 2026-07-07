---
name: vambcore
category: bioinformatics
description: VAMBcore - Core module for VAMB metagenomic binning.
tags: [vambcore, metagenomics, binning, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/RasmussenLab/vamb"
---

## Concepts

- **Tool Overview**: VAMBcore - Core module for metagenomic binning.
- **Core Function**: Provides utilities for metagenomic binning.
- **Input**: Metagenomic data.
- **Output**: Binned contigs.
- **Installation**: Install via pip
- **Use Case**: Metagenomics, binning, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Computation Time**: May be slow for complex datasets.

## Examples

### Run binning
**Args:** `vambcore -i contigs.fasta -o bins/`
**Explanation:** Perform metagenomic binning.

### With options
**Args:** `vambcore -i contigs.fasta -o bins/ -t 8`
**Explanation:** Use 8 threads.
