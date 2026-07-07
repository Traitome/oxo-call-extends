---
name: crumble
category: formatting
description: Lossy compression of BAM/CRAM files by replacing quality values with variant-aware binary quality based on alignment and variant calls
tags: [crumble, BAM, CRAM, compression, lossy, quality-values, variant-calling, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/jkbonfield/crumble"
---

## Concepts

- **Tool Overview**: crumble (v0.9.1) - Controllable lossy compression of BAM/CRAM files through intelligent quality value replacement.
- **Core Function**: Analyzes sequence pileup to identify sites where quality values are unnecessary for accurate variant prediction, then replaces them with compact binary values (high/low quality) based on agreement with likely variant calls. Achieves 2.2-7.4x overall CRAM file size reduction while maintaining variant calling accuracy.
- **Algorithm**: (1) Reads aligned BAM/CRAM file in coordinate order. (2) Analyzes sequence pileup at each position to determine likely variant status. (3) For bases agreeing with likely variant: assigns high quality. (4) For bases disagreeing: assigns low quality. (5) Re-encodes quality values using lossless compressor. Note: designed for single diploid samples only, not for cancer or pooled samples.
- **Input**: Coordinate-sorted BAM or CRAM file with alignments, optional BED file for regions requiring quality preservation.
- **Output**: Compressed BAM/CRAM file with reduced quality information, optional BED file of suspicious regions.
- **Application**: Large-scale sequencing projects, archival storage, population genetics where variant calling is the primary goal.
- **Installation**: `conda install -c bioconda crumble`

## Pitfalls

- **Diploid Only**: Designed specifically for single diploid samples. Does not work correctly on cancer samples (with mixed genotypes), pooled samples, or haploid regions.
- **Coordinate Sorted Required**: Input must be sorted by genomic coordinates before running crumble.
- **Lossy Compression**: Quality values are permanently modified - cannot recover original quality scores.
- **Remapping Compatibility**: Lightest compression level (-1) is designed for easier remapping, but heavier compression may introduce issues if you need to realign later.
- **Quality vs Size Tradeoff**: Higher compression levels sacrifice more quality information for smaller file sizes.
- **Auxiliary Tags**: Can optionally remove certain auxiliary tags - verify you don't need these tags before removal.

## Examples

### Basic lossy compression
**Args:** `crumble input.cram output.cram`
**Explanation:** Compress CRAM file using default compression level, reducing quality values based on variant agreement.

### Specify compression level
**Args:** `crumble -1 input.bam output.bam`
**Explanation:** Use lightest compression level (-1) which preserves more quality information for remapping scenarios.

### Highest compression
**Args:** `crumble -9 input.cram output.cram`
**Explanation:** Use maximum compression level for smallest file size when remapping is not planned.

### Keep quality in specific regions
**Args:** `crumble -b capture_regions.bed input.cram output.cram`
**Explanation:** Preserve original quality values in regions defined by BED file (e.g., target capture regions).

### Report suspicious regions
**Args:** `crumble -B input.cram output.cram`
**Explanation:** Output a BED file listing regions where quality was modified based on uncertain variant predictions.

### Compress BAM to CRAM
**Args:** `crumble input.bam output.cram`
**Explanation:** Convert BAM to CRAM while applying lossy quality compression in one step.

### Remove read names (maximum compression)
**Args:** `crumble -r input.cram output.cram`
**Explanation:** Remove read names in addition to quality compression for maximum size reduction.

### Remove auxiliary tags
**Args:** `crumble -x input.cram output.cram`
**Explanation:** Remove certain auxiliary tags (like NM, MD tags) that can be recalculated during realignment.

### Set reference genome
**Args:** `crumble -R reference.fa input.cram output.cram`
**Explanation:** Provide reference genome file for CRAM decompression verification.

### Multi-threaded compression
**Args:** `crumble -t 8 input.cram output.cram`
**Explanation:** Use 8 threads for faster processing on multi-core systems.

### Display help
**Args:** `crumble --help`
**Explanation:** Show all available options and compression levels.
