---
name: mace
category: utility
description: Model Based Analysis for ChIP-exo data
tags: [mace, utility, ChIP-exo, peak-calling]
author: oxo-call-community
source_url: "http://chipexo.sourceforge.net"
---

## Concepts

- **Tool Overview**: mace v1.2 is a model-based analysis tool for ChIP-exo sequencing data.
- **Core Function**: Identifies transcription factor binding sites from ChIP-exo data.
- **Statistical Model**: Uses probabilistic modeling to detect binding events with high precision.
- **Input/Output**: Input: BAM file with aligned reads; Output: Peak calls with confidence scores.
- **Installation**: `conda install -c bioconda mace`
- **Key Features**: High-resolution peak calling, handles ChIP-exo specific data characteristics.

## Pitfalls

- **Data Quality**: Requires high-quality ChIP-exo data with proper controls.
- **Control Data**: Needs matched control samples for accurate peak calling.
- **Memory Usage**: Processing large datasets may require significant memory.
- **Computation Time**: Can be slow for large genomes or deep sequencing data.
- **Parameter Tuning**: May require adjustment for different transcription factors.
- **Alignment Quality**: Depends on properly aligned reads.

## Examples

### Call peaks from ChIP-exo data
**Args:** `mace -i chip.bam -c control.bam -o peaks.bed`
**Explanation:** Calls peaks using ChIP-exo data and control.

### With reference genome
**Args:** `mace -i chip.bam -c control.bam -r reference.fasta -o peaks.bed`
**Explanation:** Uses reference genome for better peak calling.

### Threads
**Args:** `mace -i chip.bam -c control.bam -t 8 -o peaks.bed`
**Explanation:** Uses 8 threads for parallel processing.

### Peak threshold
**Args:** `mace -i chip.bam -c control.bam -p 0.001 -o peaks.bed`
**Explanation:** Sets p-value threshold to 0.001.

### Verbose mode
**Args:** `mace -i chip.bam -c control.bam -v -o peaks.bed`
**Explanation:** Outputs detailed peak calling information.

### Help documentation
**Args:** `mace --help`
**Explanation:** Displays all available options and parameters.