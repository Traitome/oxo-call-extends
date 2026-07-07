---
name: macs3
category: epigenomics
description: Model Based Analysis for ChIP-Seq data.
tags: [macs3, epigenomics, ChIP-seq, peak-calling]
author: oxo-call-community
source_url: "https://github.com/macs3-project/MACS"
---

## Concepts

- **Tool Overview**: macs3 v3.0.4 is the latest version of the Model-based Analysis of ChIP-Seq data.
- **Core Function**: Identifies enriched regions (peaks) from ChIP-seq experiments.
- **Improvements**: Enhanced peak calling algorithm, better handling of paired-end data.
- **Input/Output**: Input: BAM/SAM/FASTQ files; Output: Peak calls in multiple formats.
- **Installation**: `conda install -c bioconda macs3`
- **Key Features**: Improved statistical model, better sensitivity, supports ATAC-seq data.

## Pitfalls

- **Version Differences**: Command syntax differs from macs2.
- **Data Quality**: Requires high-quality sequencing data.
- **Control Data**: Controls are essential for accurate peak calling.
- **Memory Usage**: Processing large datasets requires significant memory.
- **Computation Time**: Deep sequencing data can be slow to process.
- **Parameter Tuning**: Different experiments may require different parameters.

## Examples

### Call peaks with control
**Args:** `macs3 callpeak -t treatment.bam -c control.bam -g hs -n output`
**Explanation:** Calls peaks from ChIP-seq data.

### With paired-end data
**Args:** `macs3 callpeak -t treatment_pe.bam -c control_pe.bam --format BAMPE -g hs -n output`
**Explanation:** Handles paired-end sequencing data.

### Broad peaks
**Args:** `macs3 callpeak -t treatment.bam -c control.bam -g hs -n output --broad`
**Explanation:** Calls broad peaks.

### ATAC-seq data
**Args:** `macs3 callpeak -t atac.bam -g hs -n output --nomodel --shift -100 --extsize 200`
**Explanation:** Processes ATAC-seq data with open chromatin.

### Track output
**Args:** `macs3 callpeak -t treatment.bam -c control.bam -g hs -n output --trackline`
**Explanation:** Generates UCSC Genome Browser track files.

### Help documentation
**Args:** `macs3 --help`
**Explanation:** Displays all available commands and options.