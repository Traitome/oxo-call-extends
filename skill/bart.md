---
name: bart
category: qc
description: BART - Bacterial Read Type classification tool for sequencing data
tags: [bart, qc, bacterial-reads, sequencing-classification]
author: oxo-call-community
source_url: "https://github.com/tomdstanton/bart"
---

## Concepts

- **Tool Overview**: BART (v0.1.2) is a tool for classifying bacterial read types from sequencing data, helping identify different types of sequencing reads in metagenomic or bacterial sequencing experiments.
- **Core Function**: Classifies sequencing reads into different bacterial read types.
- **Read Classification**: Identifies read types based on sequence characteristics.
- **Metagenomic Analysis**: Helps analyze mixed bacterial populations from sequencing data.
- **Quality Control**: Provides quality assessment metrics for bacterial sequencing data.
- **Input/Output**: Accepts FASTQ files; outputs read type classifications.
- **Installation**: `conda install -c bioconda bart`.

## Pitfalls

- **Reference Database**: Requires appropriate reference database for classification.
- **Mixed Samples**: May have difficulty with highly mixed metagenomic samples.
- **Sequence Quality**: Low-quality reads may affect classification accuracy.
- **Version Differences**: Options may vary between versions. Check help for your version.

## Examples

### Classify reads
**Args:** `bart classify -i reads.fastq -o read_types.txt`
**Explanation:** Classifies sequencing reads into different bacterial types.

### Paired-end reads
**Args:** `bart classify -i r1.fastq -i r2.fastq -o read_types.txt`
**Explanation:** Processes paired-end reads for classification.

### Specify database
**Args:** `bart classify -i reads.fastq -d database.fasta -o read_types.txt`
**Explanation:** Uses custom reference database for classification.

### Confidence threshold
**Args:** `bart classify -i reads.fastq -c 0.8 -o read_types.txt`
**Explanation:** Sets minimum confidence threshold of 0.8 for classification.

### Generate report
**Args:** `bart classify -i reads.fastq -o read_types.txt --report`
**Explanation:** Generates detailed classification report.

### Batch processing
**Args:** `bart batch -i samples.txt -o results/`
**Explanation:** Processes multiple samples in batch mode.

### Display help
**Args:** `bart --help`
**Explanation:** Shows all available command-line options and usage information.