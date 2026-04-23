---
name: bamscale
category: utility
description: BAMscale - One-step tool for quantifying and normalizing peak coverage
tags: [peak-quantification, coverage-normalization, bigwig, chip-seq]
author: oxo-call-community
source_url: "https://github.com/ncbi/BAMscale"
---

## Concepts

- **Tool Overview**: BAMscale is a one-step tool for quantifying and normalizing peak coverage or generating scaled BigWig files for DNA-seq capture methods.

- **Peak Quantification**: Quantifies coverage in peak regions from ChIP-seq, ATAC-seq, or similar experiments.

- **Normalization**: Provides multiple normalization methods including RPKM, CPM, and spike-in normalization.

- **BigWig Generation**: Creates scaled BigWig files for genome browser visualization.

## Pitfalls

- **Peak File Required**: Requires peak/region file in BED format for quantification mode.

- **Normalization Choice**: Different normalization methods suit different applications. Choose appropriately.

- **Spike-In Normalization**: Requires spike-in control for accurate spike-in based normalization.

## Examples

### Quantify peak coverage
**Args:** `BAMscale -b alignments.bam -p peaks.bed -o quantification.tsv`
**Explanation:** Quantifies coverage in peak regions from BAM file.

### Generate scaled BigWig
**Args:** `BAMscale -b alignments.bam -o coverage.bigWig`
**Explanation:** Creates scaled BigWig coverage track for visualization.

### RPKM normalization
**Args:** `BAMscale -b alignments.bam -p peaks.bed --normalize RPKM -o rpkm_quant.tsv`
**Explanation:** Quantifies peaks with RPKM normalization.

### Multiple BAM files
**Args:** `BAMscale -b sample1.bam sample2.bam -p peaks.bed -o multi_quant.tsv`
**Explanation:** Quantifies same peaks across multiple BAM files.
