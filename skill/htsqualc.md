---
name: htsqualc
category: quality-control
description: HTSQualC is an automated quality control analysis tool for single and paired-end high-throughput sequencing data.
tags: [htsqualc, quality-control, sequencing, FASTQ]
author: oxo-call-community
source_url: "https://reneshbedre.github.io/blog/htseqqc.html"
---

## Concepts

- **Tool Overview**: HTSQualC is a comprehensive quality control tool for Illumina sequencing data quality assessment.
- **Quality Metrics**: Computes base quality scores, GC content distribution, adapter contamination, and duplication levels.
- **Fast Processing**: Optimized for rapid analysis of large sequencing datasets.
- **Report Generation**: Produces both text and graphical quality reports for easy interpretation.
- **Filtering Methods**: Supports multiple strategies for removing low-quality reads.
- **Installation**: `conda install -c bioconda htsqualc`

## Pitfalls

- **Platform Specificity**: Designed primarily for Illumina data; other platforms may not be fully supported.
- **FASTQ Format**: Requires properly formatted FASTQ files with correct quality encoding.
- **Memory Usage**: Very large files may require significant memory resources.
- **Paired-End Handling**: Ensure proper pairing of R1/R2 files for paired-end analysis.
- **Adapter Sequences**: Default adapters may not match custom library preparation kits.
- **Quality Thresholds**: Default thresholds may need adjustment for specific project requirements.

## Examples

### Basic quality assessment
**Args:** `htsqualc -i input.fastq -o qc_report`
**Explanation:** Runs quality control analysis on a single-end FASTQ file and generates a QC report.

### Paired-end quality assessment
**Args:** `htsqualc -i input_R1.fastq -j input_R2.fastq -o qc_report`
**Explanation:** Analyzes paired-end sequencing data from both R1 and R2 files together.

### Quality filtering
**Args:** `htsqualc -i input.fastq -o qc_report -f --min-quality 20`
**Explanation:** Filters reads with average quality score below 20.

### Adapter trimming
**Args:** `htsqualc -i input.fastq -o qc_report -t --adapter AGATCGGAAGAGC`
**Explanation:** Trims specified adapter sequences from reads.

### Generate summary statistics
**Args:** `htsqualc -i input.fastq -o qc_report -s`
**Explanation:** Generates comprehensive summary statistics including read counts and quality distributions.