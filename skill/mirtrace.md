---
name: mirtrace
category: alignment
description: miRTrace is a new quality control and taxonomic tracing tool developed specifically for small RNA sequencing data (sRNA-Seq). Each sample is characterized by profiling sequencing quality, read length, sequencing depth and miRNA complexity and also the amounts of miRNAs versus undesirable sequences (derived from tRNAs, rRNAs and sequencing artifacts). In addition to these routine quality control (QC) analyses, miRTrace can accurately and sensitively resolve taxonomic origins of small RNA-Seq data based on the composition of clade-specific miRNAs. This feature can be used to detect cross-clade contaminations in typical lab settings. It can also be applied for more specific applications in forensics, food quality control and clinical diagnosis, for instance tracing the origins of meat products or detecting parasitic microRNAs in host serum.
tags: [mirtrace, alignment, microrna]
author: oxo-call-community
source_url: "https://github.com/friedlanderlab/mirtrace"
---

## Concepts

- **Tool Overview**: miRTrace v1.0.1 performs quality control and taxonomic tracing for small RNA sequencing data.
- **Core Function**: Profiles sequencing quality, read length, depth, miRNA complexity, and taxonomic origins.
- **Quality Control**: Analyzes small RNA-seq data quality metrics.
- **Taxonomic Tracing**: Identifies taxonomic origins of small RNA sequences.
- **Contamination Detection**: Detects cross-clade contaminations.
- **Input/Output**: Accepts small RNA-seq data; outputs QC reports and taxonomic analysis.

## Pitfalls

- **Small RNA Specific**: Designed for small RNA sequencing data.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal analysis.
- **Data Quality**: Results depend on input data quality.
- **Reference Databases**: Requires appropriate miRNA reference databases.

## Examples

### Run quality control
**Args:** `mirtrace -i reads.fastq -o qc_report.html`
**Explanation:** Generates quality control report for small RNA-seq data.

### Taxonomic tracing
**Args:** `mirtrace -i reads.fastq -t -o taxonomy_report.html`
**Explanation:** Performs taxonomic tracing analysis.

### With reference genome
**Args:** `mirtrace -i reads.fastq -g genome.fasta -o qc_report.html`
**Explanation:** Uses reference genome for mapping.

### Batch processing
**Args:** `mirtrace -i fastq/ -o reports/`
**Explanation:** Processes multiple FASTQ files.

### Detailed output
**Args:** `mirtrace -i reads.fastq -o qc_report.html -v`
**Explanation:** Generates detailed QC report.