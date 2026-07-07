---
name: noise2read
category: expression
description: noise2read corrects erroneous reads in sequencing data by leveraging neighboring high-abundance reads.
tags: [noise2read, expression, error-correction, sequencing]
author: oxo-call-community
source_url: "https://github.com/Jappy0/noise2read"
---

## Concepts

- **Tool Overview**: noise2read corrects sequencing errors by converting erroneous reads to their original state.
- **Core Function**: Identifies and corrects erroneous reads using neighboring high-abundance sequences.
- **Algorithm**: Uses PCR error mechanism rules to detect and correct errors.
- **Input Format**: Accepts FASTQ files from DNA/RNA-seq, small RNA, UMI, and amplicon sequencing.
- **Output**: Produces corrected FASTQ files.
- **Use Case**: Error correction, improving data quality, and variant calling accuracy.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Read Length**: Optimized for short reads (<300bp).
- **Abundance Threshold**: Requires sufficient coverage for correction.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Correction can be computationally intensive.
- **False Corrections**: May introduce incorrect corrections.

## Examples

### Display help
**Args:** `noise2read --help`
**Explanation:** Shows available options and usage instructions.

### Correct reads
**Args:** `noise2read -i reads.fastq -o corrected.fastq`
**Explanation:** Corrects erroneous reads in FASTQ file.

### With UMI
**Args:** `noise2read -i reads.fastq -o corrected.fastq --umi`
**Explanation:** Handles UMI-based sequencing data.

### RNA-seq mode
**Args:** `noise2read -i reads.fastq -o corrected.fastq --rna`
**Explanation:** Optimizes for RNA sequencing data.

### Threads
**Args:** `noise2read -i reads.fastq -o corrected.fastq -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum abundance
**Args:** `noise2read -i reads.fastq -o corrected.fastq -m 10`
**Explanation:** Sets minimum abundance threshold for correction.

### Verbose mode
**Args:** `noise2read -i reads.fastq -o corrected.fastq -v`
**Explanation:** Runs with verbose output.