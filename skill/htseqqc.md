---
name: htseqqc
category: quality-control
description: HTSeqQC is an automated quality control analysis tool for single and paired-end high-throughput sequencing data generated from Illumina sequencing platforms.
tags: [htseqqc, quality-control, Illumina, sequencing, FASTQ]
author: oxo-call-community
source_url: "https://reneshbedre.github.io/blog/htseqqc.html"
---

## Concepts

- **Tool Overview**: HTSeqQC is a comprehensive quality control toolkit designed specifically for Illumina sequencing data quality assessment.
- **Quality Metrics**: Computes key metrics including base quality scores, GC content, adapter contamination, and sequence duplication levels.
- **Fast Processing**: Optimized for rapid processing of large sequencing datasets.
- **Report Generation**: Produces both text and graphical quality reports for easy interpretation.
- **Filtering Capabilities**: Provides multiple methods for filtering low-quality reads.
- **Installation**: `conda install -c bioconda htseqqc`

## Pitfalls

- **Platform Specificity**: Designed primarily for Illumina data; may not work optimally with other sequencing platforms.
- **FastQ Format**: Requires properly formatted FASTQ files with correct quality encoding (Phred+33 or Phred+64).
- **File Size**: Very large files may require significant memory resources.
- **Paired-End Handling**: Ensure proper pairing of R1/R2 files for paired-end analysis.
- **Adapter Sequences**: Default adapter sequences may not match custom library preparation kits.
- **Quality Thresholds**: Default thresholds may need adjustment based on specific project requirements.

## Examples

### Basic quality assessment
**Args:** `htseqqc -i input.fastq -o qc_report`
**Explanation:** Runs quality control analysis on a single-end FASTQ file and generates a QC report directory.

### Paired-end quality assessment
**Args:** `htseqqc -i input_R1.fastq -j input_R2.fastq -o qc_report`
**Explanation:** Analyzes paired-end sequencing data from both R1 and R2 files together.

### Quality filtering
**Args:** `htseqqc -i input.fastq -o qc_report -f --min-quality 20`
**Explanation:** Performs quality filtering to remove reads with average quality score below 20.

### Adapter trimming
**Args:** `htseqqc -i input.fastq -o qc_report -t --adapter AGATCGGAAGAGC`
**Explanation:** Trims adapter sequences from reads using the specified adapter sequence.

### Generate summary statistics
**Args:** `htseqqc -i input.fastq -o qc_report -s`
**Explanation:** Generates comprehensive summary statistics including read counts, GC content, and quality distributions.