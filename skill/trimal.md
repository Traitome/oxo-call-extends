---
name: trimal
category: analysis
description: TrimAl - Tool for automated alignment trimming.
tags: [trimal, sequence-alignment, alignment-trimming, phylogenetics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/trimAl/trimAl"
---

## Concepts

- **Tool Overview**: TrimAl - A tool for automated trimming of multiple sequence alignments.
- **Core Function**: Removes poorly aligned regions, gaps, and low-quality columns from alignments.
- **Input**: Sequence alignments (FASTA, PHYLIP, etc.).
- **Output**: Trimmed alignments, trimming statistics.
- **Installation**: `conda install -c bioconda trimal`
- **Use Case**: Phylogenetic analysis, alignment quality improvement, sequence analysis.

## Pitfalls

- **Over-trimming**: May remove important conserved regions.
- **Parameter Selection**: Requires careful parameter selection.

## Examples

### Trim alignment
**Args:** `trimal -in alignment.fasta -out trimmed.fasta -automated1`
**Explanation:** Automatically trim alignment using default parameters.

### With gap threshold
**Args:** `trimal -in align.fasta -out clean.fasta -gt 0.8`
**Explanation:** Remove columns with more than 20% gaps.
