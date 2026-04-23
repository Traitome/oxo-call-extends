---
name: bamutil
category: utility
description: BamUtil - Programs for performing operations on SAM/BAM files
tags: [bam-processing, sam-tools, format-manipulation, validation]
author: oxo-call-community
source_url: "https://genome.sph.umich.edu/wiki/BamUtil"
---

## Concepts

- **Tool Overview**: BamUtil provides a collection of programs for performing various operations on SAM/BAM files, all built into a single executable.

- **Validation**: Validates SAM/BAM files for format compliance and integrity.

- **Format Conversion**: Converts between SAM, BAM, and CRAM formats.

- **Read Operations**: Performs read filtering, clipping, and other manipulations.

- **Statistics**: Generates alignment statistics and quality metrics.

## Pitfalls

- **Reference Required**: Some operations require reference genome FASTA.

- **Index Dependency**: Many operations require BAM index file.

- **Memory Usage**: Large BAM files require substantial memory for processing.

## Examples

### Validate BAM file
**Args:** `bam validate --in alignments.bam`
**Explanation:** Validates BAM file format and integrity.

### Convert BAM to SAM
**Args:** `bam convert --in alignments.bam --out alignments.sam`
**Explanation:** Converts BAM file to SAM format.

### Clip overlapping read pairs
**Args:** `bam clipOverlap --in alignments.bam --out clipped.bam`
**Explanation:** Clips overlapping portions of read pairs.

### Dump BAM statistics
**Args:** `bam stats --in alignments.bam`
**Explanation:** Generates alignment statistics from BAM file.

### Split BAM by read group
**Args:** `bam splitByReadGroup --in alignments.bam --out output_dir/`
**Explanation:** Splits BAM file into separate files by read group.
