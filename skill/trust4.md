---
name: trust4
category: analysis
description: TRUST4 - Tool for T-cell receptor and B-cell receptor repertoire analysis.
tags: [trust4, tcr, bcr, immune-repertoire, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/liulab-dfci/TRUST4"
---

## Concepts

- **Tool Overview**: TRUST4 - A tool for analyzing T-cell receptor (TCR) and B-cell receptor (BCR) repertoires from sequencing data.
- **Core Function**: Reconstructs TCR/BCR sequences and analyzes repertoire diversity.
- **Input**: FASTQ reads, reference germline sequences.
- **Output**: Reconstructed sequences, clonotype frequencies, diversity metrics.
- **Installation**: `conda install -c bioconda trust4`
- **Use Case**: Immunology research, cancer immunotherapy, vaccine development.

## Pitfalls

- **Reads Quality**: Requires high-quality sequencing data.
- **Reference Database**: Results depend on germline reference quality.

## Examples

### Analyze TCR repertoire
**Args:** `run-trust4.py -f reads.fastq -o tcr_repertoire/`
**Explanation:** Analyze T-cell receptor repertoire from sequencing data.

### BCR analysis
**Args:** `run-trust4.py -f bcr_reads.fastq -b -o bcr_results/`
**Explanation:** Analyze B-cell receptor repertoire.
