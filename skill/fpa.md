---
name: fpa
category: alignment
description: Filter Pairwise Alignment - filter long read mapping information to save disk space.
tags: [fpa, alignment, long reads, filtering]
author: oxo-call-community
source_url: "https://github.com/natir/yacrd"
---

## Concepts
- **Pairwise Alignment Filtering**: Filters and reduces long-read mapping information.
- **Disk Space Optimization**: Reduces storage requirements for alignment data.
- **Mapping Quality**: Filters alignments based on quality scores.
- **Alignment Length**: Removes short or low-quality alignments.
- **Overlap Detection**: Identifies and filters overlapping alignments.

## Pitfalls
- **Quality Thresholds**: Stringent filtering may remove valid alignments.
- **Data Loss**: Over-filtering can result in lost biological information.
- **Format Compatibility**: Requires specific input format (SAM/BAM).
- **Memory Usage**: Processing large alignment files requires significant memory.
- **Parameter Tuning**: Requires careful adjustment of filtering parameters.

## Examples
### Filter alignments by quality
**Args:** `fpa -i alignments.sam -o filtered.sam -q 20`
**Explanation:** Filters alignments with mapping quality >= 20.

### Remove short alignments
**Args:** `fpa -i alignments.sam -o filtered.sam -l 1000`
**Explanation:** Removes alignments shorter than 1000 bases.

### Filter overlapping reads
**Args:** `fpa -i alignments.sam -o filtered.sam --remove-overlaps`
**Explanation:** Removes overlapping alignments to reduce redundancy.

### Keep primary alignments only
**Args:** `fpa -i alignments.sam -o filtered.sam --primary-only`
**Explanation:** Keeps only primary alignments, removing secondary/supplementary.

### Compress output
**Args:** `fpa -i alignments.sam -o filtered.bam --compress`
**Explanation:** Outputs filtered alignments in compressed BAM format.