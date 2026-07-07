---
name: srprism
category: alignment
description: SRPRISM - Short Read Alignment Tool for high-performance sequence mapping.
tags: [srprism, alignment, short-read, mapping]
author: oxo-call-community
source_url: "ftp://ftp.ncbi.nlm.nih.gov/pub/agarwala/srprism/"
---

## Concepts

- **Tool Overview**: srprism (v2.4.24) is a fast and memory-efficient short read aligner developed by NCBI for mapping sequencing reads to reference genomes.
- **Core Function**: Uses spaced seed indexing and bit-parallel algorithms for rapid read mapping with high sensitivity.
- **Alignment Strategy**: Implements a two-phase approach - seed finding followed by dynamic programming for extension.
- **Input/Output**: Input: FASTQ/FASTA reads; Output: SAM/BAM alignment files with mapping quality scores.
- **Supported Technologies**: Illumina, Ion Torrent, and other short-read sequencing platforms.
- **Installation**: Download from NCBI FTP site or compile from source; pre-built binaries available for major platforms.

## Pitfalls

- **Memory Usage**: Building index for large genomes requires significant RAM (8GB+ recommended).
- **Index Building Time**: Index construction can be time-consuming for large reference sequences.
- **Read Length Limitations**: Optimal performance with reads ≤ 150bp; longer reads may need parameter adjustment.
- **SNP Sensitivity**: Default settings may miss variants; adjust seed parameters for variant calling.
- **Paired-End Handling**: Requires proper orientation and insert size parameters for paired reads.
- **Output Format**: Default output may require conversion for downstream tools like SAMtools.

## Examples

### Display help
**Args:** `srprism --help`
**Explanation:** Shows available options and usage information.

### Build index
**Args:** `srprism index -i reference.fasta -o ref_index`
**Explanation:** Build index for reference genome.

### Basic alignment
**Args:** `srprism align -i reads.fastq -r ref_index -o alignment.sam`
**Explanation:** Align reads to indexed reference genome.

### Paired-end alignment
**Args:** `srprism align -i read1.fastq -i2 read2.fastq -r ref_index -o pe_alignment.sam --paired`
**Explanation:** Align paired-end reads to reference genome.

### With quality filtering
**Args:** `srprism align -i reads.fastq -r ref_index -o alignment.sam -q 20`
**Explanation:** Filter reads by minimum quality score before alignment.

### Output BAM format
**Args:** `srprism align -i reads.fastq -r ref_index -o alignment.bam --bam`
**Explanation:** Output alignment directly in BAM format.

### Multiple read files
**Args:** `srprism align -i batch1.fastq -i batch2.fastq -r ref_index -o combined.sam`
**Explanation:** Align multiple read files to the same reference.
