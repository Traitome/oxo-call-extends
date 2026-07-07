---
name: mir-prefer
category: expression
description: microRNA PREdiction From small RNA-seq data
tags: [mir-prefer, expression, microrna]
author: oxo-call-community
source_url: "https://github.com/hangelwen/miR-PREFeR"
---

## Concepts

- **Tool Overview**: miR-PREFeR v0.24 predicts miRNAs from small RNA-seq data.
- **Core Function**: Identifies novel miRNAs from sequencing data.
- **De novo Prediction**: Predicts miRNAs without relying on known sequences.
- **Small RNA Analysis**: Processes small RNA sequencing data.
- **Input/Output**: Accepts small RNA-seq data; outputs miRNA predictions.
- **miRNA Discovery**: Supports novel miRNA identification workflows.

## Pitfalls

- **Small RNA Specific**: Designed for small RNA sequencing data.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal prediction.
- **Data Quality**: Results depend on input data quality.
- **False Positives**: May produce false positive predictions.

## Examples

### Predict miRNAs
**Args:** `mir-prefer -i reads.fastq -o results/`
**Explanation:** Predicts miRNAs from small RNA-seq data.

### With genome
**Args:** `mir-prefer -i reads.fastq -g genome.fasta -o results/`
**Explanation:** Uses reference genome for mapping.

### Quantify expression
**Args:** `mir-prefer -i reads.fastq -o results/ -q`
**Explanation:** Quantifies miRNA expression levels.

### Batch processing
**Args:** `mir-prefer -i fastq/ -o results/`
**Explanation:** Processes multiple FASTQ files.

### Generate report
**Args:** `mir-prefer -i reads.fastq -o results/ -r report.html`
**Explanation:** Generates HTML analysis report.