---
name: monopogen
category: variant-calling
description: Monopogen is an analysis package for SNV calling from single-cell sequencing datasets.
tags: [monopogen, variant-calling, single-cell]
author: oxo-call-community
source_url: "https://github.com/KChen-lab/Monopogen"
---

## Concepts

- **Tool Overview**: Monopogen v1.6.0 performs SNV calling from single-cell sequencing data.
- **Core Function**: Calls single-nucleotide variants from various single-cell sequencing technologies.
- **Single-Cell RNA-seq**: Supports 10x 5' and 3' scRNA-seq data.
- **ATAC-seq Support**: Works with single-cell ATAC-seq data.
- **scDNA-seq**: Supports single-cell DNA sequencing data.
- **Input/Output**: Accepts aligned reads; outputs variant calls.

## Pitfalls

- **Single-Cell Specific**: Designed for single-cell sequencing data.
- **Memory Requirements**: Memory usage depends on cell count.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Results depend on sequencing quality and depth.
- **Allele Dropout**: Single-cell data may have allele dropout issues.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Call SNVs from scRNA-seq
**Args:** `monopogen -i alignments.bam -g genome.fasta -o snvs.vcf`
**Explanation:** Calls SNVs from single-cell RNA-seq data.

### For ATAC-seq data
**Args:** `monopogen -i alignments.bam -g genome.fasta -t atac -o snvs.vcf`
**Explanation:** Processes single-cell ATAC-seq data.

### With quality filtering
**Args:** `monopogen -i alignments.bam -g genome.fasta -q -o snvs.vcf`
**Explanation:** Applies quality filtering before calling.

### Batch processing
**Args:** `monopogen -i bam/ -g genome.fasta -o results/`
**Explanation:** Processes multiple samples.

### Generate report
**Args:** `monopogen -i alignments.bam -g genome.fasta -r report.html -o snvs.vcf`
**Explanation:** Generates analysis report.