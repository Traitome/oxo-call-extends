---
name: fastdup
category: utility
description: "A Scalable Duplicate Marking Tool using Speculation-and-Test Mechanism."
tags: [fastdup, utility, duplicate-detection, sequencing-data, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/zzhofict/FastDup"
---

## Concepts

- **Tool Overview**: FastDup is a scalable duplicate marking tool that uses a speculation-and-test mechanism for efficient duplicate detection.
- **Core Function**: Identifies and marks duplicate reads in sequencing data.
- **Input/Output**: Input: Sequencing reads (FASTQ/BAM). Output: Marked duplicates, duplicate statistics.
- **Algorithm**: Uses speculation-and-test mechanism for efficient duplicate detection.
- **Key Features**: Scalable, fast duplicate detection, memory efficient, supports multiple formats, batch processing.
- **Installation**: `conda install -c bioconda fastdup`

## Pitfalls

- **Memory Usage**: Large datasets may require significant memory.
- **Format Compatibility**: Requires standard input formats.
- **Duplicate Definition**: Depends on definition of duplicates.
- **Computation Time**: Very large datasets may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic duplicate marking
**Args:** `fastdup -i reads.fastq -o marked_reads.fastq`
**Explanation:** Marks duplicates in FASTQ file.

### From BAM file
**Args:** `fastdup -i alignment.bam -o marked.bam`
**Explanation:** Marks duplicates in BAM file.

### Generate statistics
**Args:** `fastdup -i reads.fastq -o marked_reads.fastq -s stats.txt`
**Explanation:** Generates duplicate statistics.

### Parallel processing
**Args:** `fastdup -i reads.fastq -o marked_reads.fastq -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Batch mode
**Args:** `fastdup -i fastq_files/ -o output/ --batch`
**Explanation:** Processes multiple files in batch mode.