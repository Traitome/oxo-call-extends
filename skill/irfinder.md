---
name: irfinder
category: rna-analysis
description: Intron Retention Finder - Detection and quantification of intron retention events from RNA-seq data
tags: [irfinder, rna-analysis, alternative-splicing, intron-retention]
author: oxo-call-community
source_url: "https://github.com/williamritchie/IRFinder/wiki"
---

## Concepts

- **Tool Overview**: IRFinder is a computational tool for detecting and quantifying intron retention events from RNA sequencing data.
- **Core Function**: Uses the IR ratio metric (intronic reads / (intronic + exonic reads)) to identify retained introns across the transcriptome.
- **Input/Output**: Accepts sorted BAM files and GTF annotations. Outputs IR ratios, read counts, and statistical significance values.
- **Installation**: `conda install -c bioconda irfinder` or download from GitHub
- **IR Ratio**: Key metric representing the proportion of transcripts retaining a specific intron (IR ratio > 0.1 typically indicates retention).
- **Quality Control**: Automatically checks sample quality based on intergenic vs coding region read ratio.

## Pitfalls

- **Low Coverage**: Insufficient sequencing depth can lead to inaccurate IR ratio estimation, especially for lowly expressed genes.
- **Reference Annotation**: Outdated or incomplete GTF annotations may miss novel introns or misannotate existing ones.
- **Read Mapping**: Poorly mapped reads, especially across splice junctions, can affect intron retention calls.
- **Library Preparation**: Strand-specific vs non-strand-specific libraries require different handling.
- **Transcript Isoforms**: Alternative transcript structures can complicate intron boundary definition.
- **Normalization**: Differences in sequencing depth between samples require proper normalization for comparison.

## Examples

### Basic intron retention detection
**Args:** `IRFinder -d genome_dir/ -r reads.bam -o output_dir/ -t 16`
**Explanation:** Runs IRFinder with 16 threads to detect intron retention events from aligned reads.

### Strand-specific library
**Args:** `IRFinder -d genome_dir/ -r stranded_reads.bam -o results/ --stranded RF`
**Explanation:** Processes strand-specific RNA-seq data with RF orientation for accurate intron retention quantification.

### Multiple samples analysis
**Args:** `IRFinder -d genome_dir/ -r sample1.bam sample2.bam sample3.bam -o multi_sample/`
**Explanation:** Analyzes multiple BAM files together, enabling comparative analysis across samples.

### Custom annotation file
**Args:** `IRFinder -d genome_dir/ -r reads.bam -o output/ -a custom_annotation.gtf`
**Explanation:** Uses a custom GTF file instead of the default genome annotation for intron detection.

### Generate HTML report
**Args:** `IRFinder -d genome_dir/ -r reads.bam -o report/ --html`
**Explanation:** Generates an interactive HTML report with visualization of intron retention events.

### Filter by IR ratio threshold
**Args:** `IRFinder -d genome_dir/ -r reads.bam -o filtered/ --min-ir-ratio 0.15`
**Explanation:** Filters results to only include introns with IR ratio >= 0.15, focusing on significant retention events.