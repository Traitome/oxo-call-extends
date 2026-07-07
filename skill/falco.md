---
name: falco
category: qc
description: "falco is a drop-in C++ implementation of FastQC to assess the quality of sequence reads."
tags: [falco, qc, quality-control, sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/smithlabcode/falco"
---

## Concepts

- **Tool Overview**: falco is a high-performance C++ implementation of FastQC for quality control assessment of sequencing reads.
- **Core Function**: Provides quality control metrics for sequencing data, including base quality, sequence content, and adapter detection.
- **Input/Output**: Input: Sequencing reads (FASTQ). Output: HTML report, JSON metrics, quality statistics.
- **Algorithm**: Implements FastQC functionality in C++ for improved performance and parallel processing.
- **Key Features**: Drop-in FastQC replacement, high performance, parallel processing, comprehensive QC metrics, multiple output formats.
- **Installation**: `conda install -c bioconda falco`

## Pitfalls

- **Memory Usage**: Large datasets may require significant memory.
- **Format Compatibility**: Requires standard FASTQ format.
- **Report Format**: Output format may differ slightly from FastQC.
- **Version Compatibility**: Options may vary between versions.
- **Dependency**: Requires appropriate C++ runtime libraries.

## Examples

### Basic quality control
**Args:** `falco -i reads.fastq -o qc_report/`
**Explanation:** Generates quality control report for sequencing reads.

### Parallel processing
**Args:** `falco -i reads.fastq -o qc_report/ -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### JSON output
**Args:** `falco -i reads.fastq -o qc_report/ --json`
**Explanation:** Outputs metrics in JSON format.

### Paired-end reads
**Args:** `falco -1 reads_1.fastq -2 reads_2.fastq -o qc_report/`
**Explanation:** Processes paired-end sequencing data.

### Batch processing
**Args:** `falco -i reads/ -o qc_reports/ --batch`
**Explanation:** Processes multiple FASTQ files in batch mode.