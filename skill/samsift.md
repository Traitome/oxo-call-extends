---
name: samsift
category: alignment
description: Advanced filtering and tagging of SAM/BAM alignments using Python expressions.
tags: ["samsift", "alignment", "bam", "sam", "filtering", "tagging"]
author: oxo-call-community
source_url: "https://github.com/karel-brinda/samsift"
---

## Concepts
- **Tool Overview**: samsift (v0.3.1) is a Python-based tool for advanced filtering and tagging of SAM/BAM alignments using Python expressions, allowing flexible and powerful filtering operations.
- **Core Function**: Enables filtering alignments based on arbitrary Python expressions, adding custom tags, and modifying alignment records programmatically.
- **Algorithm**: Uses pysam library to parse SAM/BAM files and evaluates Python expressions for each alignment record.
- **Input Format**: SAM/BAM/CRAM alignment files.
- **Output Format**: Filtered SAM/BAM files with optional custom tags added.
- **Use Case**: Quality control filtering, targeted alignment extraction, custom annotation of alignments, batch processing of sequencing data.

## Pitfalls
- **Python Expression Errors**: Invalid Python expressions will cause runtime errors; test expressions carefully.
- **Performance**: Complex expressions may reduce processing speed on large files.
- **Memory Usage**: Processing very large BAM files may require significant memory.
- **Flag Interpretation**: Understanding SAM FLAG bits is essential for correct filtering.
- **Tag Naming**: Custom tags must follow SAM specification (2-character type code).
- **Random Sampling**: Using random functions without seed may produce non-reproducible results.

## Examples
### Filter by alignment score
**Args:** `samsift -i input.bam -o filtered.bam -f 'AS>94'`
**Explanation:** `-i` input BAM; `-o` output BAM; `-f` filter expression keeping only alignments with score >94.

### Keep unaligned reads
**Args:** `samsift -i input.bam -f 'FLAG & 0x04'`
**Explanation:** Filters to keep only reads with the unaligned FLAG bit set.

### Keep aligned reads
**Args:** `samsift -i input.bam -f 'not(FLAG & 0x04)'`
**Explanation:** Keeps only aligned reads by negating the unaligned flag.

### Filter by sequence pattern
**Args:** `samsift -i input.bam -f 'SEQ.find("ACCAGAGGAT")!=-1'`
**Explanation:** Keeps reads containing the specific sequence pattern.

### Add custom tags
**Args:** `samsift -i input.bam -c 'ln=len(SEQ);ab=1.0*sum(QUALa)/ln'`
**Explanation:** Adds tags 'ln' (sequence length) and 'ab' (average base quality).

### Random sampling
**Args:** `samsift -i input.bam -f 'random.random()<0.25' -0 'random.seed(42)'`
**Explanation:** Samples 25% of alignments with a fixed random seed for reproducibility.

### Filter by read names from file
**Args:** `samsift -i input.bam -0 'q=open("qnames.txt").read().splitlines()' -f 'QNAME in q'`
**Explanation:** Loads read names from file and keeps only those alignments.