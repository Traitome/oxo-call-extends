---
name: mquad
category: variant-calling
description: MQuad - Mixture Model for Mitochondrial Mutation detection in single-cell omics data.
tags: [mquad, variant-calling, mitochondrial]
author: oxo-call-community
source_url: "https://github.com/aaronkwc/MQuad"
---

## Concepts

- **Tool Overview**: MQuad v0.1.8b detects mitochondrial mutations in single-cell data.
- **Core Function**: Identifies mitochondrial variants using mixture modeling.
- **Mitochondrial DNA**: Specialized for mtDNA mutation detection.
- **Single-Cell Data**: Designed for single-cell sequencing experiments.
- **Mixture Model**: Uses statistical mixture models for variant calling.
- **Input/Output**: Accepts aligned reads; outputs mitochondrial variants.

## Pitfalls

- **Mitochondrial Specific**: Designed for mtDNA analysis.
- **Memory Requirements**: Memory usage depends on cell count.
- **Parameter Tuning**: May require parameter adjustment for calling.
- **Data Quality**: Results depend on sequencing depth and quality.
- **Heteroplasmy**: Requires careful handling of heteroplasmic variants.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Call mitochondrial variants
**Args:** `mquad -i alignments.bam -g genome.fasta -o variants.vcf`
**Explanation:** Detects mitochondrial mutations from aligned reads.

### With quality filtering
**Args:** `mquad -i alignments.bam -g genome.fasta -q -o variants.vcf`
**Explanation:** Applies quality filtering before calling.

### Heteroplasmy analysis
**Args:** `mquad -i alignments.bam -g genome.fasta -het -o variants.vcf`
**Explanation:** Performs heteroplasmy analysis.

### Batch processing
**Args:** `mquad -i bam/ -g genome.fasta -o results/`
**Explanation:** Processes multiple samples.

### Generate report
**Args:** `mquad -i alignments.bam -g genome.fasta -r report.html -o variants.vcf`
**Explanation:** Generates analysis report.