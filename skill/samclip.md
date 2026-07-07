---
name: samclip
category: alignment
description: Filter SAM/BAM for soft and hard clipped alignments
tags: ["samclip", "clipping", "alignment", "filtering", "SAM"]
author: oxo-call-community
source_url: "https://github.com/tseemann/samclip"
---

## Concepts

- **Tool Overview**: samclip (v0.4.0) is a tool for filtering SAM/BAM files based on soft and hard clipping, useful for removing poorly aligned reads and potential adapter sequences.
- **Core Function**: Filters alignments based on clipping thresholds, removing reads with excessive soft or hard clipping that may indicate poor mapping or contamination.
- **Algorithm**: Parses CIGAR strings to identify clipping operations, applies user-defined thresholds to filter reads.
- **Input Format**: SAM/BAM alignment files.
- **Output Format**: Filtered SAM/BAM files, statistics report.
- **Use Case**: Quality control, adapter trimming, removing low-quality alignments.

## Pitfalls

- **Threshold selection**: Incorrect thresholds may remove valid reads.
- **CIGAR parsing**: Complex CIGAR strings may cause parsing issues.
- **Soft vs hard**: Soft-clipped bases are still part of the read, hard-clipped are removed.
- **Performance**: Processing large BAM files can be time-consuming.
- **Memory usage**: Requires loading alignment data into memory.
- **Format compatibility**: Requires properly formatted SAM/BAM files.

## Examples

### Basic filtering
**Args:** `samclip -i input.sam -o filtered.sam`
**Explanation:** `-i` input SAM; `-o` filtered output.

### Soft clip threshold
**Args:** `samclip -i input.sam -o filtered.sam -s 0.2`
**Explanation:** `-s` maximum fraction of soft-clipped bases (default: 0.2).

### Hard clip threshold
**Args:** `samclip -i input.sam -o filtered.sam -H 0.1`
**Explanation:** `-H` maximum fraction of hard-clipped bases (default: 0.1).

### Combined thresholds
**Args:** `samclip -i input.sam -o filtered.sam -s 0.15 -H 0.05`
**Explanation:** Applies both soft and hard clip thresholds.

### BAM input/output
**Args:** `samclip -i input.bam -o filtered.bam`
**Explanation:** Automatically handles BAM format.

### Output statistics
**Args:** `samclip -i input.sam -o filtered.sam -t stats.txt`
**Explanation:** `-t` outputs filtering statistics.

### Invert filter
**Args:** `samclip -i input.sam -o clipped.sam --invert`
**Explanation:** `--invert` keeps only clipped reads instead of removing them.