---
name: splitp
category: qc
description: SplitP - Streaming read pre-processor for sequencing data
tags: [splitp, qc, pre-processing, streaming, quality-control]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/splitp"
---

## Concepts

- **Tool Overview**: splitp (v0.2.0) - A streaming read pre-processor
- **Core Function**: Pre-processes sequencing reads in streaming mode
- **Input/Output**: Accepts raw reads; outputs processed reads
- **Algorithm**: Streaming processing algorithms
- **Installation**: `conda install -c bioconda splitp`
- **Key Features**: Streaming processing, read pre-processing, quality control

## Pitfalls

- **Input Requirements**: Requires properly formatted sequencing reads
- **Read Quality**: Read quality affects processing results
- **Streaming Mode**: Streaming mode requires careful memory management
- **Memory Usage**: Large read sets require significant memory
- **Output Format**: Output format depends on configuration
- **Processing Accuracy**: Accuracy depends on input read quality

## Examples

### Display help
**Args:** `splitp --help`
**Explanation:** Shows available options and usage information.

### Basic read pre-processing
**Args:** `splitp -i reads.fastq -o processed.fastq`
**Explanation:** Pre-process sequencing reads.

### With quality filtering
**Args:** `splitp -i reads.fastq -o processed.fastq --quality-filter`
**Explanation:** Enable quality filtering.

### With adapter trimming
**Args:** `splitp -i reads.fastq -o processed.fastq --trim-adapters`
**Explanation:** Enable adapter trimming.

### Streaming mode
**Args:** `splitp -i reads.fastq -o processed.fastq --streaming`
**Explanation:** Use streaming processing mode.

### Output detailed results
**Args:** `splitp -i reads.fastq -o processed.fastq --detailed`
**Explanation:** Output detailed processing information.

### Output quality scores
**Args:** `splitp -i reads.fastq -o processed.fastq --quality-scores`
**Explanation:** Output quality score information.

### Output statistics
**Args:** `splitp -i reads.fastq -o processed.fastq --stats`
**Explanation:** Output processing statistics.

### Generate report
**Args:** `splitp -i reads.fastq -o processed.fastq --report`
**Explanation:** Generate processing report.

### With threads
**Args:** `splitp -i reads.fastq -o processed.fastq -p 8`
**Explanation:** Use multiple threads for processing.