---
name: pardre
category: hpc
description: ParDRe is a parallel tool to remove duplicate reads from sequencing data.
tags: [pardre, hpc, duplicate-removal, parallel]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/pardre/"
---

## Concepts

- **Tool Overview**: ParDRe removes duplicate sequencing reads in parallel.
- **Core Function**: Identifies and removes duplicate reads.
- **Algorithm**: Uses parallel processing for efficient deduplication.
- **Input Format**: Accepts FASTQ files.
- **Output**: Produces deduplicated FASTQ files.
- **Use Case**: Read preprocessing, quality control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Duplicate Definition**: Different definitions of duplicates.
- **Read Order**: Output order may differ from input.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pardre --help`
**Explanation:** Shows available options and usage instructions.

### Remove duplicates
**Args:** `pardre -i input.fastq -o output.fastq`
**Explanation:** Removes duplicate reads.

### Paired-end data
**Args:** `pardre -1 reads_1.fastq -2 reads_2.fastq -o output/`
**Explanation:** Processes paired-end reads.

### Verbose mode
**Args:** `pardre -v -i input.fastq -o output.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pardre -t 8 -i input.fastq -o output.fastq`
**Explanation:** Uses 8 threads for parallel processing.

### Compressed output
**Args:** `pardre -i input.fastq -o output.fastq.gz --gzip`
**Explanation:** Outputs compressed FASTQ.

### Hash size
**Args:** `pardre -s 1000000 -i input.fastq -o output.fastq`
**Explanation:** Sets hash table size.