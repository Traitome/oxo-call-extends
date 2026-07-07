---
name: deltamsi
category: variant-calling
description: DeltaMSI - AI-based modeling of microsatellite instability scoring on NGS data.
tags: [deltamsi, variant-calling, msi, microsatellite, deep-learning]
author: oxo-call-community
source_url: "https://github.com/RADar-AZDelta/DeltaMSI"
---

## Concepts

- **Tool Overview**: deltamsi (v1.0.1+) is an AI-based tool for microsatellite instability (MSI) scoring from next-generation sequencing data. It uses machine learning models to detect MSI status, which is important for cancer diagnosis and treatment selection.
- **Core Function**: Detects and scores microsatellite instability by analyzing sequence reads at known microsatellite loci, providing quantitative MSI scores and categorical classifications.
- **Input/Output**: Input: BAM files with index, reference genome. Output: MSI scores, instability classifications, per-locus statistics.
- **Algorithm**: Uses artificial intelligence models trained on MSI-positive and MSI-negative samples to classify microsatellite stability based on read patterns.
- **Key Features**: AI-powered classification, high accuracy, supports multiple sequencing platforms, batch processing, clinical-grade results.
- **Installation**: `conda install -c bioconda deltamsi`

## Pitfalls

- **Input Requirements**: Requires properly aligned BAM files with adequate coverage at microsatellite loci.
- **Reference Genome**: Must use the same reference genome used for alignment.
- **Microsatellite Panel**: Performance depends on the microsatellite loci panel used.
- **Sample Quality**: Poor quality sequencing may affect results.
- **Tumor Purity**: May be affected by tumor purity in heterogeneous samples.

## Examples

### Score microsatellite instability
**Args:** `deltamsi --bam sample.bam --ref ref.fa --output msi_report.tsv`
**Explanation:** Scores microsatellite instability from NGS data.

### With custom microsatellite panel
**Args:** `deltamsi --bam sample.bam --ref ref.fa --panel custom_panel.bed --output msi_report.tsv`
**Explanation:** Use custom microsatellite loci panel for analysis.

### Batch processing
**Args:** `deltamsi --bam_dir bams/ --ref ref.fa --output_dir results/`
**Explanation:** Process multiple samples in batch.