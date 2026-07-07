---
name: fasten
category: formatting
description: "Perform random operations on fastq files, using unix streaming. Secure your analysis with Fasten!"
tags: [fasten, formatting, FASTQ, streaming, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/lskatz/fasten"
---

## Concepts

- **Tool Overview**: fasten is a suite of tools for performing various operations on FASTQ files using Unix streaming, designed for efficient pipeline integration.
- **Core Function**: Provides multiple utilities for FASTQ processing including filtering, trimming, and transformation.
- **Input/Output**: Input: FASTQ files. Output: Processed FASTQ files, statistics.
- **Algorithm**: Uses Unix streaming for efficient processing and pipeline integration.
- **Key Features**: Unix streaming, multiple FASTQ operations, pipeline integration, efficient processing, batch support.
- **Installation**: `conda install -c bioconda fasten`

## Pitfalls

- **Stream Compatibility**: Requires proper streaming setup.
- **Memory Usage**: Large datasets may require significant memory.
- **Format Compatibility**: Requires standard FASTQ format.
- **Processing Order**: Streaming operations may affect output order.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic filtering
**Args:** `fasten_filter -i reads.fastq -o filtered.fastq -q 20`
**Explanation:** Filters reads by quality score.

### Trim reads
**Args:** `fasten_trim -i reads.fastq -o trimmed.fastq -l 50`
**Explanation:** Trims reads to specified length.

### Subsample reads
**Args:** `fasten_subsample -i reads.fastq -o subsampled.fastq -p 0.1`
**Explanation:** Subsamples 10% of reads.

### Reverse complement
**Args:** `fasten_revcomp -i reads.fastq -o revcomp.fastq`
**Explanation:** Reverse complements reads.

### Pipeline usage
**Args:** `cat reads.fastq | fasten_filter -q 20 | fasten_trim -l 50 > output.fastq`
**Explanation:** Chains multiple operations in pipeline.