---
name: align_trim
category: qc
description: ARTIC network tool for trimming amplicon sequencing primers from aligned reads
tags: [amplicon, primer-trimming, artic, amplicon-sequencing, covid]
author: oxo-call-community
source_url: "https://github.com/artic-network/align_trim"
---

## Concepts

- **Tool Overview**: align_trim is an ARTIC network tool for trimming amplicon primers from aligned sequencing reads, essential for amplicon-based pathogen sequencing.
- **Core Function**: Removes primer sequences from aligned BAM files based on primer BED file, ensuring accurate downstream variant calling.
- **Input/Output**: Input: Sorted BAM file, primer BED file. Output: Primer-trimmed BAM file.
- **Amplicon Protocols**: Designed for ARTIC, Midnight, and similar amplicon sequencing protocols.
- **Installation**: Install via bioconda: `conda install -c bioconda align_trim`

## Pitfalls

- **Sorted BAM Required**: Input BAM must be coordinate-sorted - use samtools sort first.
- **Primer BED Format**: Requires specific BED format with primer coordinates - use ARTIC primer schemes.
- **Soft Clipping**: Uses soft clipping by default - verify compatibility with downstream tools.
- **Primer Scheme Version**: Ensure primer BED matches the primer scheme version used for sequencing.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options for align_trim.

### Basic primer trimming
**Args:** `--bam aligned.bam --bed primers.bed --output trimmed.bam`
**Explanation:** Trims primers from aligned reads using primer coordinates.

### Trim with report output
**Args:** `--bam aligned.bam --bed primers.bed --output trimmed.bam --report report.txt`
**Explanation:** Outputs trimming statistics report alongside trimmed BAM.

### Trim with hard clipping
**Args:** `--bam aligned.bam --bed primers.bed --output trimmed.bam --hard-clip`
**Explanation:** Uses hard clipping instead of soft clipping for primer removal.

### Trim with minimum amplicon size
**Args:** `--bam aligned.bam --bed primers.bed --output trimmed.bam --min-length 50`
**Explanation:** Filters out reads shorter than 50bp after trimming.

### Trim and sort output
**Args:** `--bam aligned.bam --bed primers.bed --output trimmed.bam --sort`
**Explanation:** Sorts output BAM file after trimming.

### Trim with specific read group
**Args:** `--bam aligned.bam --bed primers.bed --output trimmed.bam --read-group RG1`
**Explanation:** Only trims reads belonging to specified read group.

### Verbose output
**Args:** `--bam aligned.bam --bed primers.bed --output trimmed.bam --verbose`
**Explanation:** Outputs detailed progress information during trimming.
