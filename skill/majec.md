---
name: majec
category: alignment
description: Momentum-Accelerated Junction-Enhanced Counting for RNA-seq quantification
tags: [majec, alignment, RNA-seq, quantification]
author: oxo-call-community
source_url: "https://github.com/calico/majec"
---

## Concepts

- **Tool Overview**: majec v0.1.4 - MAJEC is a unified framework for quantifying genes, transcript isoforms, and individual transposable element loci from aligned RNA-seq reads.
- **Core Function**: Uses junction-informed Expectation-Maximization algorithm for accurate quantification of genes, isoforms, and transposable elements.
- **Input/Output**: Input: BAM alignment files, annotation GTF/GFF; Output: Quantification matrices, statistics.
- **Installation**: `conda install -c bioconda majec`
- **Junction-Enhanced**: Incorporates splice junction information for better quantification.
- **Momentum Acceleration**: Uses momentum-based optimization for faster convergence.

## Pitfalls

- **Alignment Quality**: Poor alignment affects quantification accuracy.
- **Annotation Quality**: Incomplete or incorrect annotations cause errors.
- **Memory Usage**: Large datasets require significant memory.
- **Computational Time**: EM algorithm can be slow for complex transcriptomes.
- **Strand Specificity**: Requires proper handling of strand-specific libraries.
- **Transposable Elements**: May require custom annotations for TE quantification.

## Examples

### Quantify genes and isoforms
**Args:** `majec quant -b alignments.bam -g genes.gtf -o quant_results/`
**Explanation:** Quantifies genes and transcript isoforms from BAM file.

### With TE quantification
**Args:** `majec quant -b alignments.bam -g genes.gtf -t te_annotations.gtf -o quant_results/`
**Explanation:** Quantifies genes, isoforms, and transposable elements.

### Strand-specific data
**Args:** `majec quant -b alignments.bam -g genes.gtf -o quant_results/ --strand reverse`
**Explanation:** Handles reverse-strand-specific RNA-seq libraries.

### Custom convergence threshold
**Args:** `majec quant -b alignments.bam -g genes.gtf -o quant_results/ --epsilon 1e-6`
**Explanation:** Sets custom convergence threshold for EM algorithm.

### Verbose mode
**Args:** `majec quant -b alignments.bam -g genes.gtf -o quant_results/ -v`
**Explanation:** Provides detailed logging during quantification.

### Generate QC report
**Args:** `majec qc -b alignments.bam -g genes.gtf -o qc_report.html`
**Explanation:** Generates quality control report.