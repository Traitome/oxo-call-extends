---
name: bamtools
category: utility
description: BamTools - C++ API and command-line toolkit for working with BAM data
tags: [bam-processing, sam-tools, format-conversion, statistics]
author: oxo-call-community
source_url: "https://github.com/pezmaster31/bamtools"
---

## Concepts

- **Tool Overview**: BamTools provides a C++ API and command-line utilities for BAM file manipulation, including format conversion, filtering, and statistics.

- **Format Conversion**: Converts between BAM, SAM, and other formats.

- **Filtering**: Filters reads by various criteria (mapping quality, flags, region).

- **Statistics**: Generates comprehensive alignment statistics.

- **JSON Output**: Supports JSON output format for programmatic processing.

## Pitfalls

- **Index Required**: Some operations require BAM index (.bai) file.

- **Memory Usage**: Large BAM files may require substantial memory.

- **Filter Syntax**: Complex filters require proper JSON syntax. Validate filter files.

## Examples

### Convert BAM to SAM
**Args:** `bamtools convert -in alignments.bam -out alignments.sam`
**Explanation:** Converts BAM file to human-readable SAM format.

### Filter by region
**Args:** `bamtools filter -in alignments.bam -out filtered.bam -region chr1:1000-2000`
**Explanation:** Extracts reads mapping to specified genomic region.

### Filter by mapping quality
**Args:** `bamtools filter -in alignments.bam -out high_quality.bam -mapQuality ">=30"`
**Explanation:** Filters reads with mapping quality ≥30.

### Generate statistics
**Args:** `bamtools stats -in alignments.bam -out stats.txt`
**Explanation:** Computes comprehensive alignment statistics.

### JSON format output
**Args:** `bamtools stats -in alignments.bam -json -out stats.json`
**Explanation:** Outputs statistics in JSON format for parsing.

### Merge multiple BAMs
**Args:** `bamtools merge -in sample1.bam -in sample2.bam -out merged.bam`
**Explanation:** Merges multiple BAM files into single file.
