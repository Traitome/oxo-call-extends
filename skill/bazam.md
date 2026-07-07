---
name: bazam
category: formatting
description: Bazam - Extract paired reads in FASTQ format from coordinate-sorted BAM files
tags: [bazam, formatting, FASTQ, BAM, paired-end]
author: oxo-call-community
source_url: "https://github.com/ssadedin/bazam"
---

## Concepts

- **Tool Overview**: Bazam (v1.0.1) extracts paired reads in FASTQ format from coordinate-sorted BAM files, enabling conversion of aligned reads back to FASTQ format for downstream analysis.
- **Core Function**: Converts aligned BAM files back to FASTQ format, preserving read pairs.
- **Coordinate-Sorted BAM**: Works specifically with coordinate-sorted BAM files.
- **Paired-End Support**: Maintains pairing information when extracting reads.
- **Region Extraction**: Supports extraction of reads from specific genomic regions.
- **Input/Output**: Accepts BAM files; outputs paired-end FASTQ files.
- **Installation**: `conda install -c bioconda bazam`.

## Pitfalls

- **BAM Index**: Requires indexed BAM file for region-specific extraction.
- **Coordinate Sorted**: Only works with coordinate-sorted BAM files.
- **Read Pairing**: Assumes proper read pairing in input BAM.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Extract all reads
**Args:** `bazam -b alignments.bam -o output.fastq`
**Explanation:** Extracts all reads from BAM file to FASTQ format.

### Extract paired-end reads
**Args:** `bazam -b alignments.bam -o output_R1.fastq -o2 output_R2.fastq`
**Explanation:** Extracts paired-end reads to separate R1 and R2 FASTQ files.

### Extract specific region
**Args:** `bazam -b alignments.bam -r chr1:1000-2000 -o output.fastq`
**Explanation:** Extracts reads overlapping specified genomic region.

### Multiple regions
**Args:** `bazam -b alignments.bam -R regions.bed -o output.fastq`
**Explanation:** Extracts reads overlapping regions in BED file.

### Filter by mapping quality
**Args:** `bazam -b alignments.bam -q 30 -o output.fastq`
**Explanation:** Extracts only reads with mapping quality ≥30.

### Include unmapped reads
**Args:** `bazam -b alignments.bam -u -o output.fastq`
**Explanation:** Includes unmapped reads in output.

### Display help
**Args:** `bazam --help`
**Explanation:** Shows all available command-line options and usage information.