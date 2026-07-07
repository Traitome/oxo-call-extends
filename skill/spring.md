---
name: spring
category: qc
description: Spring - Compression tool for FASTQ files
tags: [spring, qc, compression, fastq, storage]
author: oxo-call-community
source_url: "https://github.com/shubhamchandak94/Spring"
---

## Concepts

- **Tool Overview**: spring (v1.1.1) - A FASTQ compression tool
- **Core Function**: Compresses FASTQ files with high compression ratio
- **Input/Output**: Accepts FASTQ files; outputs compressed files
- **Algorithm**: Reference-based compression algorithms
- **Installation**: `conda install -c bioconda spring`
- **Key Features**: FASTQ compression, high compression ratio, lossless

## Pitfalls

- **Input Requirements**: Requires properly formatted FASTQ files
- **File Size**: Large files require significant memory and time
- **Compression Ratio**: Ratio depends on data characteristics
- **Decompression**: Requires Spring for decompression
- **Output Format**: Output format depends on configuration
- **Compression Speed**: Speed depends on file size and settings

## Examples

### Display help
**Args:** `spring --help`
**Explanation:** Shows available options and usage information.

### Basic compression
**Args:** `spring -c -i reads.fastq -o reads.spr`
**Explanation:** Compress FASTQ file.

### Decompression
**Args:** `spring -d -i reads.spr -o reads.fastq`
**Explanation:** Decompress Spring file.

### With quality preservation
**Args:** `spring -c -i reads.fastq -o reads.spr --preserve-quality`
**Explanation:** Preserve quality scores in compression.

### With reference genome
**Args:** `spring -c -i reads.fastq -r reference.fasta -o reads.spr`
**Explanation:** Use reference genome for compression.

### Multiple files
**Args:** `spring -c -i reads1.fastq reads2.fastq -o reads.spr`
**Explanation:** Compress multiple FASTQ files.

### Output detailed results
**Args:** `spring -c -i reads.fastq -o reads.spr --detailed`
**Explanation:** Output detailed compression information.

### Output statistics
**Args:** `spring -c -i reads.fastq -o reads.spr --stats`
**Explanation:** Output compression statistics.

### Generate report
**Args:** `spring -c -i reads.fastq -o reads.spr --report`
**Explanation:** Generate compression report.

### With threads
**Args:** `spring -c -i reads.fastq -o reads.spr -p 8`
**Explanation:** Use multiple threads for compression.