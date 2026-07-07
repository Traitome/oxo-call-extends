---
name: nanofilt
category: qc
description: NanoFilt - Filtering and trimming of Oxford Nanopore sequencing data
tags: [nanofilt, qc, nanopore, filtering, trimming, quality-control]
author: oxo-call-community
source_url: "https://github.com/wdecoster/nanofilt"
---

## Concepts

- **Tool Overview**: NanoFilt v2.8.0 is a command-line tool for filtering and trimming Oxford Nanopore sequencing reads. It provides flexible filtering options based on quality scores, read length, and trimming parameters.
- **Core Function**: Filters reads by quality thresholds, length constraints, and performs head/tail trimming. Designed for use in Unix pipelines with stdin/stdout streaming.
- **Algorithm**: Processes reads sequentially, applying user-defined filters and trimming operations. Supports phred quality scores and can handle gzipped input.
- **Input Format**: Accepts FASTQ format reads from stdin (can be gzipped). Works with both single-end and paired-end Nanopore data.
- **Output**: Produces filtered FASTQ reads to stdout for seamless integration into bioinformatics pipelines.
- **Use Case**: Quality control for Nanopore sequencing data, preprocessing reads before assembly or alignment, and removing low-quality reads.

## Pitfalls

- **Streaming Requirement**: Designed for stdin/stdout streaming. May require shell redirection for file-based operations.
- **Quality Score Format**: Assumes standard phred quality scores. Non-standard encodings may produce unexpected results.
- **Length Filtering**: Aggressive length filtering may remove biologically important sequences. Use appropriate thresholds.
- **Trimming Parameters**: Head/tail trimming removes bases without quality assessment. Consider quality-based trimming alternatives.
- **Compression**: Ensure consistent compression when piping between tools. Mixed compression states may cause issues.
- **Batch Processing**: For large datasets, consider parallel processing or splitting files to improve performance.

## Examples

### Filter by minimum quality
**Args:** `-q 10 < input.fastq > filtered.fastq`
**Explanation:** Filters out reads with average quality score below Q10.

### Filter by length range
**Args:** `-l 1000 --max_length 50000 < input.fastq > filtered.fastq`
**Explanation:** Keeps reads between 1kb and 50kb in length.

### Trim and filter combined
**Args:** `-q 10 -l 500 --headcrop 50 --tailcrop 50 < input.fastq > filtered.fastq`
**Explanation:** Filters by quality and length, then trims 50bp from both ends.

### Process gzipped input
**Args:** `gunzip -c input.fastq.gz | nanofilt -q 15 | gzip > filtered.fastq.gz`
**Explanation:** Processes gzipped FASTQ through NanoFilt and re-compresses output.

### Display help
**Args:** `nanofilt --help`
**Explanation:** Shows all available filtering and trimming options.
