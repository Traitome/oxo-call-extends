---
name: ccne
category: variant-analysis
description: Carbapenemase-encoding gene copy number estimator
tags: [ccne, copy-number, carbapenemase, antimicrobial-resistance, amr]
author: oxo-call-community
source_url: "https://github.com/biojiang/ccne"
---

## Concepts

- **Tool Overview**: ccne estimates carbapenemase-encoding gene copy numbers from sequencing data.
- **Core Function**: Quantifies copy number variations of carbapenemase resistance genes.
- **Algorithm**: Uses read depth analysis to estimate gene copy numbers.
- **Input**: Aligned BAM file and reference gene sequences.
- **Output**: Copy number estimates for carbapenemase genes.
- **Application**: Antimicrobial resistance research and clinical diagnostics.
- **Installation**: Install via bioconda: `conda install -c bioconda ccne`

## Pitfalls

- **BAM Required**: Requires sorted and indexed BAM file.
- **Reference Genes**: Needs reference sequences for target genes.
- **Depth Variation**: Coverage variations affect accuracy.
- **Multiple Copies**: Complex rearrangements may affect estimation.

## Examples

### Estimate copy numbers
**Args:** `ccne -i aligned.bam -g carbapenemase_genes.fa -o copy_numbers.tsv`
**Explanation:** Estimates carbapenemase gene copy numbers from BAM file.

### With quality filter
**Args:** `ccne -i aligned.bam -g genes.fa -q 30 -o results.tsv`
**Explanation:** Uses quality threshold of 30 for read filtering.

### Display help
**Args:** `ccne --help`
**Explanation:** Shows all available options and usage information.