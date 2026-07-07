---
name: hts-nim-tools
category: utility
description: hts-nim-tools is a collection of command-line utilities demonstrating the hts-nim library, providing fast tools for BAM/CRAM filtering, read counting, and VCF validation.
tags: [hts-nim-tools, utility, Nim, BAM, CRAM, VCF]
author: oxo-call-community
source_url: "https://github.com/brentp/hts-nim-tools"
---

## Concepts

- **Tool Overview**: hts-nim-tools is a suite of high-performance bioinformatics utilities written in Nim, compiled to C for speed while maintaining Python-like syntax.
- **BAM Filtering**: `bam-filter` allows filtering BAM/CRAM/SAM files using a simple expression language.
- **Read Counting**: `count-reads` counts reads in genomic regions specified in BED files.
- **VCF Validation**: `vcf-check` verifies VCF files against background regions for missing chunks.
- **Copy Number Sampling**: `copy-number-sampler` samples BAM regions with probability from BED file for creating CN truth-sets.
- **Installation**: `conda install -c bioconda hts-nim-tools`

## Pitfalls

- **Nim Language**: Requires understanding of Nim syntax for advanced customization.
- **Expression Syntax**: Expression language for bam-filter has specific syntax requirements.
- **HTSlib Dependency**: Requires htslib >= 1.23.1 for full functionality.
- **Index Requirements**: BAM/CRAM files must be indexed for efficient region queries.
- **Memory Management**: While garbage collected, large files may require memory optimization.
- **Platform Support**: Primarily Linux-focused; macOS support may be limited.

## Examples

### Filter BAM by expression
**Args:** `bam-filter "mapq >= 30 and not duplicate" input.bam -o filtered.bam`
**Explanation:** Filters a BAM file to retain only reads with mapping quality >= 30 that are not marked as duplicates.

### Count reads in BED regions
**Args:** `count-reads -b regions.bed -i input.bam -o counts.tsv`
**Explanation:** Counts the number of reads overlapping each region specified in the BED file.

### Check VCF for missing regions
**Args:** `vcf-check -v variants.vcf -b background.bed -o report.txt`
**Explanation:** Validates that all regions in the background BED file are covered by variants in the VCF.

### Copy number sampling
**Args:** `copy-number-sampler -b probabilities.bed -i input.bam -o sampled.bam`
**Explanation:** Samples reads from BAM regions with probabilities specified in the BED file for creating CNV truth-sets.

### Stream filtered reads
**Args:** `bam-filter "proper_pair" input.bam | samtools view -h`
**Explanation:** Filters reads for proper pairs and pipes results to samtools for further processing.