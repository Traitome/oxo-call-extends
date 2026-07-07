---
name: msisensor-pro
category: variant-calling
description: Microsatellite Instability detection using high-throughput sequencing data.
tags: [msisensor-pro, variant-calling, oncology]
author: oxo-call-community
source_url: "https://github.com/xjtu-omics/msisensor-pro"
---

## Concepts

- **Tool Overview**: MSIsensor-Pro v1.3.0 detects MSI from sequencing data.
- **Core Function**: Identifies microsatellite instability in cancer samples.
- **Comprehensive Detection**: Supports various sequencing platforms.
- **High-Throughput**: Optimized for large-scale sequencing data.
- **Improved Algorithm**: Enhanced detection algorithms.
- **Input/Output**: Accepts BAM files; outputs MSI status and scores.

## Pitfalls

- **Cancer Samples**: Designed for cancer genomics data.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for detection.
- **Data Quality**: Results depend on sequencing quality.
- **Computational Resources**: Large datasets may require significant resources.
- **Reference Quality**: Depends on reference genome quality.

## Examples

### Detect MSI
**Args:** `msisensor-pro msi -d reference.fa -t tumor.bam -n normal.bam -o results.txt`
**Explanation:** Detects MSI from tumor-normal pairs.

### Scan reference
**Args:** `msisensor-pro scan -d reference.fa -o repeats.txt`
**Explanation:** Identifies microsatellite repeat regions.

### System evaluation
**Args:** `msisensor-pro system -d reference.fa -t tumor.bam -n normal.bam -o results.txt`
**Explanation:** Evaluates microsatellite sites.

### With germline mode
**Args:** `msisensor-pro msi -d reference.fa -t tumor.bam -n normal.bam -m germline -o results.txt`
**Explanation:** Performs germline variant detection.

### Batch processing
**Args:** `msisensor-pro msi -d reference.fa -i bam/ -o results/`
**Explanation:** Processes multiple sample pairs.