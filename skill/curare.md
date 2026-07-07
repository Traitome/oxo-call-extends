---
name: curare
category: expression
description: A Customizable and Reproducible Analysis Pipeline for RNA-Seq Experiments.
tags: [curare, expression, RNA-seq, pipeline, reproducible, bacterial]
author: oxo-call-community
source_url: "https://github.com/pblumenkamp/Curare"
---

## Concepts

- **Tool Overview**: curare (v0.6.0+) is a customizable and reproducible analysis pipeline for bacterial RNA-Seq experiments.
- **Core Function**: Provides standardized workflows for RNA-Seq analysis, from raw reads to differential expression analysis.
- **Input/Output**: Input: FASTQ reads, reference genome/transcriptome. Output: Expression matrices, differential expression results, quality reports.
- **Workflow**: Supports trimming, alignment, quantification, and differential expression analysis with multiple tools.
- **Key Features**: Highly customizable, reproducible via configuration files, supports multiple alignment and quantification methods.
- **Installation**: `conda install -c bioconda curare`

## Pitfalls

- **Configuration File**: Requires YAML configuration file; complex for first-time users.
- **Reference Preparation**: Reference genome must be properly indexed for alignment tools.
- **Bacterial Specific**: Optimized for bacterial RNA-Seq; may need adjustment for eukaryotic data.
- **Dependency Management**: Requires careful management of tool versions for reproducibility.
- **Output Organization**: Generates many output files; use dedicated output directory.

## Examples

### Run RNA-Seq pipeline
**Args:** `curare --config config.yaml --output results/`
**Explanation:** Run the complete RNA-Seq analysis pipeline using a configuration file.

### Generate configuration template
**Args:** `curare --init config.yaml`
**Explanation:** Generate a template configuration file for customization.

### Run quality control only
**Args:** `curare --config config.yaml --step qc --output qc_results/`
**Explanation:** Run only the QC step of the pipeline.
