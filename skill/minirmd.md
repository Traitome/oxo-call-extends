---
name: minirmd
category: qc
description: Remove duplicate and near-duplicate reads
tags: [minirmd, qc, deduplication]
author: oxo-call-community
source_url: "https://github.com/yuansliu/minirmd"
---

## Concepts

- **Tool Overview**: MiniRMD v1.1 removes duplicate and near-duplicate reads.
- **Core Function**: Identifies and removes redundant sequencing reads.
- **Read Deduplication**: Eliminates duplicate reads from datasets.
- **Near-duplicate Detection**: Identifies similar but not identical reads.
- **Input/Output**: Accepts FASTQ files; outputs deduplicated reads.
- **Quality Control**: Supports sequencing data preprocessing workflows.

## Pitfalls

- **Read-specific**: Designed for sequencing read data.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal deduplication.
- **Data Quality**: Results depend on input read quality.
- **Threshold Sensitivity**: Choice of similarity threshold affects results.

## Examples

### Remove duplicates
**Args:** `minirmd -i reads.fastq -o deduplicated.fastq`
**Explanation:** Removes duplicate reads from FASTQ file.

### With near-duplicate detection
**Args:** `minirmd -i reads.fastq -o deduplicated.fastq -n`
**Explanation:** Enables near-duplicate detection.

### Custom threshold
**Args:** `minirmd -i reads.fastq -o deduplicated.fastq -t 0.95`
**Explanation:** Uses 95% similarity threshold.

### Batch processing
**Args:** `minirmd -i fastq/ -o deduplicated/`
**Explanation:** Processes multiple FASTQ files.

### Generate statistics
**Args:** `minirmd -i reads.fastq -o deduplicated.fastq -s stats.txt`
**Explanation:** Generates deduplication statistics.