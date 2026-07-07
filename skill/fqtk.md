---
name: fqtk
category: formatting
description: A toolkit for working with FASTQ files.
tags: [fqtk, FASTQ, sequence processing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/fulcrumgenomics/fqtk"
---

## Concepts
- **FASTQ Manipulation**: Comprehensive toolkit for FASTQ file operations.
- **Read Filtering**: Filters reads based on quality, length, and content.
- **Quality Trimming**: Trims low-quality bases from read ends.
- **Sequence Masking**: Masks or soft-masks sequences.
- **Paired-End Handling**: Specialized tools for paired-end data.

## Pitfalls
- **Memory Efficiency**: May require significant memory for large files.
- **Parameter Complexity**: Many options require careful configuration.
- **Output Size**: Filtering operations can produce large intermediate files.
- **Quality Score Encoding**: Assumes standard Phred encoding.
- **Read Order**: May change read order during processing.

## Examples
### Trim low-quality bases
**Args:** `fqtk trim -i reads.fastq -o trimmed.fastq -q 20`
**Explanation:** Trims bases with quality score below 20 from read ends.

### Filter by read length
**Args:** `fqtk filter -i reads.fastq -o filtered.fastq -m 50 -M 200`
**Explanation:** Keeps reads between 50 and 200 bases in length.

### Mask low-quality bases
**Args:** `fqtk mask -i reads.fastq -o masked.fastq -q 15 -c N`
**Explanation:** Masks bases with quality < 15 as 'N'.

### Reverse complement
**Args:** `fqtk revcomp -i reads.fastq -o revcomp.fastq`
**Explanation:** Reverse complements all reads.

### Shuffle reads
**Args:** `fqtk shuffle -i reads.fastq -o shuffled.fastq`
**Explanation:** Randomly shuffles the order of reads.