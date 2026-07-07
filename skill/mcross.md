---
name: mcross
category: utility
description: Detects RNA-protein cross-linking sites from sequencing data.
tags: [mcross, RNA-protein, cross-linking]
author: oxo-call-community
source_url: "https://github.com/huijfeng/mCross"
---

## Concepts

- **Tool Overview**: mCross detects RNA-protein cross-linking sites.
- **Core Function**: Identifies cross-linking sites from sequencing data.
- **CLIP-Seq Analysis**: Analyzes CLIP-seq data for cross-links.
- **Site Detection**: Identifies precise cross-linking positions.
- **Input/Output**: Accepts BAM/SAM files, produces site annotations.
- **Installation**: `conda install -c bioconda mcross`

## Pitfalls

- **Data Quality**: Requires high-quality sequencing data.
- **Mapping Quality**: Depends on accurate read mapping.
- **False Positives**: May detect false cross-link sites.
- **Parameter Tuning**: Requires careful threshold adjustment.
- **Memory Requirements**: Large datasets require memory.
- **Output Interpretation**: Results require biological validation.

## Examples

### Detect cross-link sites
**Args:** `mcross detect -i aligned.bam -g genome.fasta -o sites.bed`
**Explanation:** Detects cross-link sites from BAM file.

### With custom parameters
**Args:** `mcross detect -i aligned.bam -q 30 -c 5 -o sites.bed`
**Explanation:** Sets quality and coverage thresholds.

### Annotate sites
**Args:** `mcross annotate -i sites.bed -g genome.fasta -o annotated.txt`
**Explanation:** Annotates detected sites with genomic features.

### Plot results
**Args:** `mcross plot -i sites.bed -o plot.pdf`
**Explanation:** Generates visualization of cross-link sites.

### Help documentation
**Args:** `mcross --help`
**Explanation:** Displays available commands and options.
