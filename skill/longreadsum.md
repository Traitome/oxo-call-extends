---
name: longreadsum
category: qc
description: LongReadSum - Quality control tool for long-read sequencing data
tags: [longreadsum, qc, quality-control, long-reads, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/WGLab/LongReadSum"
---

## Concepts

- **Quality Control**: Quality assessment of long-read sequencing data
- **Read Statistics**: Read quality statistics generation
- **Long-read Data**: Analysis of long-read sequencing data
- **Data Summary**: Comprehensive data summary generation
- **Visualization**: Quality metrics visualization
- **Report Generation**: Detailed QC report generation

## Pitfalls

- **Read Quality**: Poor quality reads affect analysis
- **Data Format**: Strict format requirements
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Metrics**: May produce inaccurate quality metrics

## Examples

### Run QC
**Args:** `longreadsum -i reads.fastq -o qc_report/`
**Explanation:** Runs quality control on long reads.

### Multiple files
**Args:** `longreadsum -i reads1.fastq reads2.fastq -o qc_report/`
**Explanation:** Processes multiple FASTQ files.

### Output format
**Args:** `longreadsum -i reads.fastq -o qc_report.json -f json`
**Explanation:** Outputs results in JSON format.

### Threads
**Args:** `longreadsum -i reads.fastq -o qc_report/ -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum length
**Args:** `longreadsum -i reads.fastq -o qc_report/ -l 1000`
**Explanation:** Filters reads shorter than 1000bp.

### Verbose output
**Args:** `longreadsum -i reads.fastq -o qc_report/ -v`
**Explanation:** Provides detailed output.