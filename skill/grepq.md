---
name: grepq
category: bioinformatics
description: grepq quickly filters FASTQ files based on quality scores, sequence length, and other criteria for quality control.
tags: [grepq, FASTQ, quality-control, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/Rbfinch/grepq"
---

## Concepts

- **FASTQ Filtering**: grepq efficiently filters FASTQ files based on various quality criteria.

- **Quality Thresholding**: Filters reads based on minimum quality scores and average quality.

- **Sequence Length Filtering**: Removes reads that are too short or too long.

- **Pattern Matching**: Supports pattern matching for filtering specific sequences.

- **Speed Optimization**: Designed for high-speed processing of large FASTQ files.

- **Stream Processing**: Processes FASTQ data in streaming mode for memory efficiency.

## Pitfalls

- **Quality Format**: Ensure correct quality score format (Phred+33 vs Phred+64).

- **Read Truncation**: Aggressive filtering may remove useful reads. Adjust thresholds carefully.

- **Memory Usage**: Processing very large files may require significant memory.

- **Compressed Files**: Ensure proper handling of compressed FASTQ files.

- **Output Format**: Be aware of output format differences between versions.

## Examples

### Filter by minimum quality
**Args:** `grepq -q 20 -i input.fastq -o filtered.fastq`
**Explanation:** Filters reads with minimum quality score of 20.

### Filter by sequence length
**Args:** `grepq -l 50 -i input.fastq -o filtered.fastq`
**Explanation:** Filters reads with minimum length of 50 bases.

### Remove low-complexity reads
**Args:** `grepq -c 0.5 -i input.fastq -o filtered.fastq`
**Explanation:** Removes reads with complexity below 0.5.

### Filter by pattern
**Args:** `grepq -p "AAAAA" -i input.fastq -o filtered.fastq`
**Explanation:** Filters reads containing the pattern "AAAAA".

### Batch processing
**Args:** `for f in *.fastq; do grepq -q 20 -i $f -o ${f%.fastq}_filtered.fastq; done`
**Explanation:** Processes multiple FASTQ files in a directory.

### Compressed input/output
**Args:** `grepq -q 20 -i input.fastq.gz -o filtered.fastq.gz`
**Explanation:** Handles compressed FASTQ files.

### Show statistics
**Args:** `grepq -s -i input.fastq`
**Explanation:** Shows statistics about the FASTQ file without filtering.