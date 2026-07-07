---
name: htsinfer
category: utility
description: HTSinfer infers metadata from Illumina high throughput sequencing (HTS) data, automatically detecting sequencing parameters and library characteristics.
tags: [htsinfer, utility, metadata, Illumina, sequencing]
author: oxo-call-community
source_url: "https://github.com/zavolanlab/htsinfer"
---

## Concepts

- **Tool Overview**: HTSinfer is a tool for automatic inference of metadata from Illumina sequencing data without prior knowledge.
- **Library Type Detection**: Identifies library type (RNA-seq, DNA-seq, small RNA-seq, etc.) from raw sequencing data.
- **Strand Orientation**: Determines strand specificity and orientation of sequencing libraries.
- **Read Pairing**: Detects whether data is single-end or paired-end and identifies proper pair orientation.
- **Insert Size Estimation**: Estimates insert size distribution for paired-end libraries.
- **Installation**: `conda install -c bioconda htsinfer`

## Pitfalls

- **Illumina Specific**: Designed specifically for Illumina sequencing data; may not work with other platforms.
- **Data Requirements**: Requires sufficient sequencing depth for accurate metadata inference.
- **Quality Dependence**: Low-quality data may lead to incorrect inference results.
- **Mixed Libraries**: May have difficulty with mixed library types or contaminated samples.
- **Reference Dependence**: Some features require reference genome for accurate inference.
- **Computational Resources**: Analysis of large datasets may require significant computational resources.

## Examples

### Basic metadata inference
**Args:** `htsinfer --input input.fastq --output metadata.json`
**Explanation:** Infers metadata from a single-end FASTQ file and outputs results in JSON format.

### Paired-end analysis
**Args:** `htsinfer --input input_R1.fastq --input2 input_R2.fastq --output metadata.json`
**Explanation:** Analyzes paired-end sequencing data from both read files.

### With reference genome
**Args:** `htsinfer --input input.fastq --reference ref.fasta --output metadata.json`
**Explanation:** Uses a reference genome to improve metadata inference accuracy.

### Generate HTML report
**Args:** `htsinfer --input input.fastq --output metadata.json --report report.html`
**Explanation:** Generates both JSON output and a human-readable HTML report.

### Batch processing
**Args:** `htsinfer --input *.fastq --output-dir results/`
**Explanation:** Processes multiple FASTQ files and outputs results to a specified directory.