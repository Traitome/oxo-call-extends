---
name: ontime
category: utility
description: ontime extracts subsets of ONT Nanopore reads based on sequencing time.
tags: [ontime, utility, nanopore, time-filtering]
author: oxo-call-community
source_url: "https://github.com/mbhall88/ontime"
---

## Concepts

- **Tool Overview**: ontime filters nanopore reads by sequencing time.
- **Core Function**: Extracts reads within specific time windows.
- **Algorithm**: Uses timestamps from sequencing metadata.
- **Input Format**: Accepts FASTQ/FASTA reads with timing information.
- **Output**: Produces filtered reads based on time criteria.
- **Use Case**: Time-series analysis, quality control, and sequencing optimization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Time Accuracy**: Depends on sequencing timing precision.
- **Input Requirements**: Requires timing metadata.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Filtering can be computationally intensive.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `ontime --help`
**Explanation:** Shows available options and usage instructions.

### Filter by time
**Args:** `ontime -i reads.fastq -s 10 -e 30 -o filtered.fastq`
**Explanation:** Extracts reads between 10-30 minutes.

### Start time only
**Args:** `ontime -i reads.fastq -s 10 -o filtered.fastq`
**Explanation:** Extracts reads after 10 minutes.

### End time only
**Args:** `ontime -i reads.fastq -e 30 -o filtered.fastq`
**Explanation:** Extracts reads before 30 minutes.

### Output format
**Args:** `ontime -i reads.fastq -s 10 -e 30 -o filtered.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Verbose mode
**Args:** `ontime -i reads.fastq -s 10 -e 30 -v -o filtered.fastq`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `ontime batch -d fastqs/ -s 10 -e 30 -o filtered/`
**Explanation:** Processes multiple FASTQ files.