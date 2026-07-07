---
name: bamkit
category: formatting
description: bamkit - Tools for common BAM file manipulations
tags: [bamkit, formatting, BAM, manipulation, utilities]
author: oxo-call-community
source_url: "https://github.com/hall-lab/bamkit"
---

## Concepts

- **Tool Overview**: bamkit is a collection of tools for common BAM file manipulations, providing utilities for filtering, sorting, and transforming alignment data. Version 16.07.26.
- **Core Function**: Provides utilities for common BAM operations including filtering, sorting, and merging.
- **Filtering**: Filters BAM records based on various criteria (quality, read group, etc.).
- **Sorting**: Sorts BAM files by coordinate or read name.
- **Merging**: Combines multiple BAM files into single output.
- **BAM Utilities**: Various helper tools for BAM file processing.
- **Input/Output**: Accepts BAM files, outputs processed BAM files.
- **Installation**: `conda install -c bioconda bamkit`.

## Pitfalls

- **BAM Index**: Some operations require indexed BAM files.
- **Memory Usage**: Sorting large BAM files may require significant memory.
- **Coordinate Order**: Ensure input BAM is coordinate-sorted when required.
- **Version Compatibility**: Options may vary between versions. Check help for your version.

## Examples

### Filter by mapping quality
**Args:** `bamkit filter -i input.bam -o filtered.bam -q 30`
**Explanation:** Filters reads with mapping quality >= 30.

### Sort by read name
**Args:** `bamkit sort -i input.bam -o sorted.bam -n`
**Explanation:** Sorts BAM file by read name.

### Merge BAM files
**Args:** `bamkit merge -i sample1.bam sample2.bam -o merged.bam`
**Explanation:** Merges multiple BAM files into one.

### Extract reads by read group
**Args:** `bamkit filter -i input.bam -o rg_filtered.bam --rg "Sample1"`
**Explanation:** Extracts reads belonging to specific read group.

### Remove duplicates
**Args:** `bamkit dedup -i input.bam -o deduped.bam`
**Explanation:** Removes PCR duplicates from BAM file.

### Convert to SAM
**Args:** `bamkit view -i input.bam -o output.sam`
**Explanation:** Converts BAM to SAM format.

### Display help
**Args:** `bamkit --help`
**Explanation:** Shows all available command-line options and usage information.