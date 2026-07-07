---
name: msisensor-rna
category: utility
description: MSI detection using RNA sequencing data for transcriptome-based MSI analysis.
tags: [msisensor-rna, utility, oncology]
author: oxo-call-community
source_url: "https://github.com/xjtu-omics/msisensor-rna"
---

## Concepts

- **Tool Overview**: MSIsensor-RNA v0.1.6 detects MSI from RNA-seq data.
- **Core Function**: Identifies microsatellite instability using transcriptome sequencing.
- **RNA-seq Based**: Works with RNA sequencing data instead of DNA.
- **Transcriptome Analysis**: Analyzes expressed microsatellite regions.
- **Cancer Research**: Supports cancer genomics studies.
- **Input/Output**: Accepts BAM files; outputs MSI status and scores.

## Pitfalls

- **RNA-seq Specific**: Designed for RNA sequencing data.
- **Memory Requirements**: Memory usage depends on data size.
- **Parameter Tuning**: May require parameter adjustment for detection.
- **Data Quality**: Results depend on RNA-seq quality.
- **Computational Resources**: Large datasets may require significant resources.
- **Reference Quality**: Depends on reference genome quality.

## Examples

### Detect MSI from RNA-seq
**Args:** `msisensor_rna msi -t tumor.bam -n normal.bam -o results.txt`
**Explanation:** Detects MSI from tumor-normal RNA-seq pairs.

### Scan for repeat regions
**Args:** `msisensor_rna scan -d reference.fa -o repeats.txt`
**Explanation:** Identifies microsatellite repeat regions.

### System evaluation
**Args:** `msisensor_rna system -d reference.fa -t tumor.bam -n normal.bam -o results.txt`
**Explanation:** Evaluates microsatellite sites in RNA.

### Generate report
**Args:** `msisensor_rna msi -t tumor.bam -n normal.bam -r report.txt -o results.txt`
**Explanation:** Generates detailed detection report.

### Batch processing
**Args:** `msisensor_rna msi -d reference.fa -i bam/ -o results/`
**Explanation:** Processes multiple RNA-seq samples.