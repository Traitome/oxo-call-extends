---
name: fastq-filter
category: qc
description: "A fast FASTQ filter program."
tags: [fastq-filter, qc, FASTQ, filtering, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/LUMC/fastq-filter"
---

## Concepts

- **Tool Overview**: fastq-filter is a fast program for filtering and processing FASTQ files based on various criteria.
- **Core Function**: Filters sequencing reads based on quality, length, and other criteria.
- **Input/Output**: Input: FASTQ files. Output: Filtered FASTQ files.
- **Algorithm**: Implements efficient filtering algorithms for FASTQ data.
- **Key Features**: Fast filtering, quality-based filtering, length filtering, paired-end support, batch processing.
- **Installation**: `conda install -c bioconda fastq-filter`

## Pitfalls

- **Memory Usage**: Large files may require significant memory.
- **Format Compatibility**: Requires standard FASTQ format.
- **Filtering Criteria**: Incorrect parameters may filter out valuable data.
- **Processing Time**: Very large files may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic quality filter
**Args:** `fastq-filter -i reads.fastq -o filtered.fastq -q 20`
**Explanation:** Filters reads with minimum quality score of 20.

### Length filter
**Args:** `fastq-filter -i reads.fastq -o filtered.fastq -l 100`
**Explanation:** Filters reads with minimum length of 100.

### Paired-end filtering
**Args:** `fastq-filter -i reads_1.fastq -I reads_2.fastq -o filtered_1.fastq -O filtered_2.fastq -q 20`
**Explanation:** Filters paired-end reads.

### Quality and length filter
**Args:** `fastq-filter -i reads.fastq -o filtered.fastq -q 20 -l 100`
**Explanation:** Filters by both quality and length.

### Batch processing
**Args:** `fastq-filter -i input/ -o output/ -q 20`
**Explanation:** Processes all FASTQ files in directory.