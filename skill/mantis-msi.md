---
name: mantis-msi
category: alignment
description: MANTIS is a program developed for detecting microsatellite instability from paired-end BAM files
tags: [mantis-msi, alignment, microsatellite, instability]
author: oxo-call-community
source_url: "https://github.com/OSU-SRLab/MANTIS/"
---

## Concepts

- **Tool Overview**: mantis-msi v1.0.5 - MANTIS (Microsatellite Analysis for Normal-Tumor InStability) detects microsatellite instability from paired-end BAM files.
- **Core Function**: Identifies microsatellite instability by comparing tumor and normal BAM files at microsatellite loci.
- **Input/Output**: Input: Tumor and normal BAM files; Output: MSI scores, instability calls.
- **Installation**: `conda install -c bioconda mantis-msi`
- **Paired Analysis**: Requires matched tumor-normal sample pairs processed with the same pipeline.
- **Read Length**: Optimized for reads of 100bp or longer; shorter reads may fail quality filters.

## Pitfalls

- **Read Length**: Short reads (<100bp) may fail quality control filters.
- **Alignment Quality**: Poor alignments affect MSI detection accuracy.
- **Sample Matching**: Requires properly matched tumor-normal pairs.
- **Microsatellite Database**: Depends on comprehensive microsatellite loci database.
- **Contamination**: Contaminated samples produce unreliable results.
- **Memory Usage**: Large BAM files require significant memory.

## Examples

### Run MSI analysis
**Args:** `mantis -t tumor.bam -n normal.bam -r ref.fa -o results/`
**Explanation:** Performs MSI analysis on paired tumor-normal samples.

### With custom microsatellite database
**Args:** `mantis -t tumor.bam -n normal.bam -r ref.fa -m microsatellites.bed -o results/`
**Explanation:** Uses custom microsatellite loci database.

### Quick mode
**Args:** `mantis -t tumor.bam -n normal.bam -r ref.fa -o results/ --quick`
**Explanation:** Runs in quick mode for faster analysis.

### Verbose mode
**Args:** `mantis -t tumor.bam -n normal.bam -r ref.fa -o results/ -v`
**Explanation:** Provides detailed logging during analysis.

### Generate report
**Args:** `mantis -t tumor.bam -n normal.bam -r ref.fa -o results/ --report`
**Explanation:** Generates HTML report of MSI results.

### Filter by quality
**Args:** `mantis -t tumor.bam -n normal.bam -r ref.fa -o results/ -q 30`
**Explanation:** Filters reads with mapping quality >= 30.