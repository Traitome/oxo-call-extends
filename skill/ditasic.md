---
name: ditasic
category: metagenomics
description: DiTASiC - Abundance estimation and differential abundance assessment in metagenomics.
tags: [ditasic, metagenomics, abundance, differential, taxa]
author: oxo-call-community
source_url: "https://rki_bioinformatics.gitlab.io/ditasic/"
---

## Concepts

- **Tool Overview**: DiTASiC (v0.2+) is a comprehensive approach for abundance estimation and differential analysis in metagenomics.
- **Core Function**: Estimates taxon abundances and performs differential abundance testing between samples.
- **Input/Output**: Input: Mapped reads (BAM), reference genomes. Output: Abundance estimates, differential results, visualization.
- **Algorithm**: Uses statistical methods for abundance estimation and differential testing.
- **Key Features**: Abundance estimation, differential abundance testing, multiple testing correction, visualization, supports multiple samples.
- **Installation**: `conda install -c bioconda ditasic`

## Pitfalls

- **Input Requirements**: Requires read mappings and reference database.
- **Reference Quality**: Reference database completeness affects results.
- **Mapping Quality**: Poor mapping affects abundance estimation.
- **Sample Size**: Requires sufficient biological replicates.
- **Normalization**: Appropriate normalization method selection is critical.

## Examples

### Estimate abundances
**Args:** `ditasic --mappings sample1.bam sample2.bam --reference refs.fa --output abundances.tsv`
**Explanation:** Estimates taxon abundances from metagenomic data.

### Differential abundance analysis
**Args:** `ditasic --mappings sample1.bam sample2.bam --reference refs.fa --output results/ --groups groups.tsv`
**Explanation:** Perform differential abundance testing between groups.

### With normalization
**Args:** `ditasic --mappings sample1.bam sample2.bam --reference refs.fa --output abundances.tsv --normalize tmm`
**Explanation:** Use TMM normalization for abundance data.

### Filter low abundance taxa
**Args:** `ditasic --mappings sample1.bam sample2.bam --reference refs.fa --output abundances.tsv --min-abundance 0.01`
**Explanation:** Filter taxa with low abundance.

### Generate visualization
**Args:** `ditasic --mappings sample1.bam sample2.bam --reference refs.fa --output results/ --plot`
**Explanation:** Generate visualizations of abundance results.