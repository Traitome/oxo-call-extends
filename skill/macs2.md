---
name: macs2
category: epigenomics
description: Model Based Analysis for ChIP-Seq data.
tags: [macs2, epigenomics, ChIP-seq, peak-calling]
author: oxo-call-community
source_url: "https://github.com/macs3-project/MACS"
---

## Concepts

- **Tool Overview**: macs2 v2.2.9.1 is a model-based analysis tool for ChIP-Seq data peak calling.
- **Core Function**: Identifies transcription factor binding sites from ChIP-seq experiments.
- **Statistical Model**: Uses a dynamic Poisson distribution to model tag distribution.
- **Input/Output**: Input: BAM/SAM files with aligned reads; Output: Peak calls in BED/GFF format.
- **Installation**: `conda install -c bioconda macs2`
- **Key Features**: Broad and narrow peak calling, supports paired-end data, incorporates control samples.

## Pitfalls

- **Data Quality**: Requires high-quality ChIP-seq data with proper controls.
- **Control Data**: Matched control samples improve peak calling accuracy.
- **Fragment Size**: Incorrect fragment size estimation affects peak detection.
- **Memory Usage**: Processing large datasets may require significant memory.
- **Computation Time**: Can be slow for deep sequencing data.
- **Parameter Tuning**: Requires careful adjustment of parameters for different datasets.

## Examples

### Call peaks with control
**Args:** `macs2 callpeak -t treatment.bam -c control.bam -f BAM -g hs -n output`
**Explanation:** Calls peaks from ChIP-seq data with matched control.

### Narrow peaks
**Args:** `macs2 callpeak -t treatment.bam -c control.bam -f BAM -g hs -n output --nomodel --shift -75 --extsize 150`
**Explanation:** Calls narrow peaks using fixed-size shifting.

### Broad peaks
**Args:** `macs2 callpeak -t treatment.bam -c control.bam -f BAM -g hs -n output --broad`
**Explanation:** Calls broad peaks for histone modifications.

### BED input
**Args:** `macs2 callpeak -t peaks.bed -c control.bed -f BED -g hs -n output`
**Explanation:** Uses BED format input files.

### Keep duplicates
**Args:** `macs2 callpeak -t treatment.bam -c control.bam -f BAM -g hs -n output --keep-dup all`
**Explanation:** Retains all duplicate reads.

### Help documentation
**Args:** `macs2 --help`
**Explanation:** Displays all available commands and options.