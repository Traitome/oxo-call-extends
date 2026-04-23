---
name: nanofilt
category: qc
description: Filtering and trimming of Oxford Nanopore Sequencing data
tags: [nanofilt, qc, nanopore, filtering, trimming]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanofilt"
---

## Concepts

- **Tool Overview**: NanoFilt v2.8.0 - filtering and trimming tool for Oxford Nanopore sequencing data.
- **Core Function**: Filters and trims Nanopore reads based on quality, length, and other criteria.
- **Input/Output**: Takes FASTQ (stdin); outputs filtered FASTQ (stdout).
- **Installation**: `conda install -c bioconda nanofilt`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Reads from stdin; outputs to stdout.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Filter by quality
**Args:** `-q 10 < input.fastq > filtered.fastq`
**Explanation:** Filters reads with average quality below Q10.

### Filter by length
**Args:** `-l 1000 --max_length 50000 < input.fastq > filtered.fastq`
**Explanation:** Filters reads between 1kb and 50kb.

### Combined filtering
**Args:** `-q 10 -l 500 --headcrop 50 --tailcrop 50 < input.fastq > filtered.fastq`
**Explanation:** Filters by quality, length, and trims 50bp from both ends.
