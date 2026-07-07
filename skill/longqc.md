---
name: longqc
category: qc
description: LongQC - Quality control tool for PacBio and ONT long reads
tags: [longqc, qc, quality-control, PacBio, ONT, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/yfukasawa/LongQC"
---

## Concepts

- **Quality Control**: Quality assessment of sequencing data
- **PacBio Data**: Analysis of PacBio sequencing data
- **ONT Data**: Analysis of Oxford Nanopore sequencing data
- **Read Statistics**: Read quality statistics generation
- **Visualization**: Quality metrics visualization
- **Data Filtering**: Filtering low-quality reads

## Pitfalls

- **Read Quality**: Poor quality reads affect analysis
- **Data Format**: Strict format requirements
- **Memory Usage**: Memory-intensive for large datasets
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Metrics**: May produce inaccurate quality metrics

## Examples

### Run QC
**Args:** `longqc sampleqc -i reads.fastq -o qc_report/`
**Explanation:** Runs quality control on long reads.

### PacBio mode
**Args:** `longqc sampleqc -i reads.fastq -o qc_report/ -p pacbio`
**Explanation:** Optimized for PacBio data.

### ONT mode
**Args:** `longqc sampleqc -i reads.fastq -o qc_report/ -p ont`
**Explanation:** Optimized for ONT data.

### Minimum length
**Args:** `longqc sampleqc -i reads.fastq -o qc_report/ -l 1000`
**Explanation:** Filters reads shorter than 1000bp.

### Output format
**Args:** `longqc sampleqc -i reads.fastq -o qc_report/ -f html`
**Explanation:** Generates HTML report.

### Verbose output
**Args:** `longqc sampleqc -i reads.fastq -o qc_report/ -v`
**Explanation:** Provides detailed output.