---
name: symbiontscreener
category: sequencing
description: Reference-free approach to identify host long reads from symbionts and contaminants.
tags: [symbiontscreener, long-reads, host-filtering, contaminants]
author: oxo-call-community
source_url: "https://github.com/BGI-Qingdao/Symbiont-Screener"
---

## Concepts

- **Tool Overview**: symbiontscreener (v1.0.0) identifies host long reads from contaminants.
- **Core Function**: Filters symbiont and contaminant reads from host data.
- **Algorithm**: Uses trio-based screening model for read classification.
- **Input/Output**: Input: Long read FASTQ; Output: Filtered host reads.
- **Applications**: Long-read sequencing, host-symbiont separation.
- **Installation**: `conda install -c bioconda symbiontscreener` or download from GitHub.

## Pitfalls

- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing long reads can be slow.
- **Parameter Tuning**: Incorrect parameters affect filtering.
- **Read Quality**: Poor quality reads affect classification.
- **Trio Data**: Requires trio sequencing data for optimal results.
- **Contaminant Diversity**: Highly diverse contaminants may be challenging.

## Examples

### Display help
**Args:** `symbiontscreener --help`
**Explanation:** Shows available options and usage information.

### Basic screening
**Args:** `symbiontscreener -i reads.fastq -o host_reads.fastq`
**Explanation:** Screen and filter host reads from contaminants.

### With trio data
**Args:** `symbiontscreener -i reads.fastq -t trio.txt -o host_reads.fastq`
**Explanation:** Use trio sequencing data for screening.

### Verbose mode
**Args:** `symbiontscreener -i reads.fastq -o host_reads.fastq -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `symbiontscreener -i reads.fastq -o host_reads.fastq --stats`
**Explanation:** Generate statistics about screening.

### Batch processing
**Args:** `for f in reads/*.fastq; do symbiontscreener -i $f -o filtered/${f%.fastq}.fastq; done`
**Explanation:** Process multiple read files.

### Filter by quality
**Args:** `symbiontscreener -i reads.fastq -o host_reads.fastq -q 20`
**Explanation:** Filter by read quality score.

### Include contaminants
**Args:** `symbiontscreener -i reads.fastq -o host_reads.fastq -c contaminants.fastq`
**Explanation:** Output separated contaminants.

### Generate report
**Args:** `symbiontscreener -i reads.fastq -o host_reads.fastq --report`
**Explanation:** Generate comprehensive screening report.
