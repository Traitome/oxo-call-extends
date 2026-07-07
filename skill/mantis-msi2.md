---
name: mantis-msi2
category: alignment
description: MANTIS2 is a program developed for detecting microsatellite instability from paired-end BAM files.
tags: [mantis-msi2, alignment, microsatellite, instability]
author: oxo-call-community
source_url: "https://github.com/nh13/MANTIS2"
---

## Concepts

- **Tool Overview**: mantis-msi2 v2.0.0 - MANTIS2 (Microsatellite Analysis for Normal-Tumor InStability) detects microsatellite instability from paired-end BAM files.
- **Core Function**: Identifies microsatellite instability (MSI) by comparing tumor and normal BAM files at microsatellite loci.
- **Input/Output**: Input: Tumor and normal BAM files; Output: MSI scores, instability calls.
- **Installation**: `conda install -c bioconda mantis-msi2`
- **Paired Analysis**: Requires matched tumor-normal sample pairs.
- **Read Length**: Optimized for reads of 100bp or longer.

## Pitfalls

- **Read Length**: Short reads (<100bp) may fail quality filters.
- **Alignment Quality**: Poor alignments affect MSI detection.
- **Sample Matching**: Requires properly matched tumor-normal pairs.
- **Microsatellite Database**: Depends on comprehensive microsatellite loci database.
- **Contamination**: Contaminated samples produce unreliable results.
- **Memory Usage**: Large BAM files require significant memory.

## Examples

### Run MSI analysis
**Args:** `mantis-msi2 -t tumor.bam -n normal.bam -r ref.fa -o results/`
**Explanation:** Performs MSI analysis on paired samples.

### With custom microsatellite database
**Args:** `mantis-msi2 -t tumor.bam -n normal.bam -r ref.fa -m microsatellites.bed -o results/`
**Explanation:** Uses custom microsatellite loci database.

### Quick mode
**Args:** `mantis-msi2 -t tumor.bam -n normal.bam -r ref.fa -o results/ --quick`
**Explanation:** Runs in quick mode for faster analysis.

### Verbose mode
**Args:** `mantis-msi2 -t tumor.bam -n normal.bam -r ref.fa -o results/ -v`
**Explanation:** Provides detailed logging during analysis.

### Generate report
**Args:** `mantis-msi2 -t tumor.bam -n normal.bam -r ref.fa -o results/ --report`
**Explanation:** Generates HTML report of MSI results.

### Filter by quality
**Args:** `mantis-msi2 -t tumor.bam -n normal.bam -r ref.fa -o results/ -q 30`
**Explanation:** Filters reads with mapping quality >= 30.