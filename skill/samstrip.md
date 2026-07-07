---
name: samstrip
category: alignment
description: Strip SAM files of data not needed for alignment computations.
tags: ["samstrip", "alignment", "sam", "bam", "filtering", "data-reduction"]
author: oxo-call-community
source_url: "https://github.com/jakobnissen/samstrip"
---

## Concepts
- **Tool Overview**: samstrip (v0.2.1) is a lightweight tool for stripping SAM files of unnecessary data to reduce file size and improve processing speed.
- **Core Function**: Removes non-essential fields from SAM alignments while preserving alignment information needed for downstream analysis.
- **Algorithm**: Parses SAM format and selectively removes fields based on user configuration or default settings.
- **Input Format**: SAM/BAM alignment files.
- **Output Format**: Stripped SAM/BAM files with reduced data content.
- **Use Case**: File size reduction for storage/transfer, preparing files for specific downstream tools that don't need full SAM data.

## Pitfalls
- **Data Loss**: Stripping fields may remove information needed for certain analyses.
- **Downstream Compatibility**: Some tools require specific SAM fields.
- **BAM Index**: Stripped BAM files need to be re-indexed after processing.
- **Paired Reads**: May affect proper pairing information if not handled correctly.
- **Quality Scores**: Stripping quality scores affects variant calling accuracy.
- **Tag Information**: Optional tags may contain important metadata.

## Examples
### Basic stripping
**Args:** `samstrip input.sam > stripped.sam`
**Explanation:** Strips unnecessary fields from SAM file and writes to stdout.

### Strip BAM file
**Args:** `samstrip -i input.bam -o stripped.bam`
**Explanation:** `-i` input BAM; `-o` output stripped BAM.

### Keep specific fields
**Args:** `samstrip --keep FLAG,POS,CIGAR input.sam`
**Explanation:** Keeps only specified fields, removes all others.

### Remove quality scores
**Args:** `samstrip --remove QUAL input.sam`
**Explanation:** Removes only the quality score field.

### Remove optional tags
**Args:** `samstrip --remove-tags input.bam`
**Explanation:** Removes all optional SAM tags from alignments.

### Compress output
**Args:** `samstrip input.sam | gzip > stripped.sam.gz`
**Explanation:** Pipes output to gzip for compression.

### Strip and sort
**Args:** `samstrip input.bam | samtools sort -o sorted_stripped.bam`
**Explanation:** Combines stripping with sorting using samtools.