---
name: tcomet
category: statistics
description: T-COMET - statistical analysis tool for comparing transcriptomic data across conditions.
tags: [tcomet, transcriptomics, differential-expression, statistics, microarray, rna-seq]
author: oxo-call-community
source_url: "https://github.com/gingold-lab/tcomet"
---

## Concepts

- **Tool Overview**: T-COMET (Transcriptome COMparative Expression Tool) - A statistical framework for comparative analysis of transcriptomic data, detecting differential gene expression patterns across experimental conditions.
- **Core Function**: Performs statistical tests to identify significantly differentially expressed genes between conditions, with multiple testing correction.
- **Input**: Expression matrix (counts, FPKM, TPM) with sample annotations indicating conditions.
- **Output**: Lists of significantly differentially expressed genes with p-values, fold changes, and correction statistics.
- **Installation**: `pip install tcomet` or `conda install -c bioconda tcomet`
- **Key Feature**: Supports both RNA-seq count data and microarray expression data.

## Pitfalls

- **Data Format**: Expression matrix must be properly formatted with genes as rows and samples as columns.
- **Replicates Required**: Statistical power requires biological replicates within each condition (minimum 2-3 recommended).
- **Normalization**: Raw counts require normalization (DESeq2 size factors, TMM) before analysis - tcomet may include or expect pre-normalized data.
- **Multiple Testing**: Large numbers of genes require appropriate multiple testing correction (FDR, Bonferroni).
- **Batch Effects**: Does not automatically correct for batch effects - preprocess data if needed.

## Examples

### Basic differential expression
**Args:** `tcomet --expression matrix.tsv --conditions conditions.txt --output results/`
**Explanation:** Standard differential expression analysis comparing conditions specified in conditions file.

### With replicates
**Args:** `tcomet -e counts.tsv -c conditions.txt -o output/ -n norm`
**Explanation:** Analysis with multiple biological replicates per condition, specifying normalization method.

### Custom contrast
**Args:** `tcomet -e matrix.tsv -c conditions.txt --contrast "treated_vs_control" -o results/`
**Explanation:** Define specific contrast for pairwise comparison between two conditions.

### Volcano plot output
**Args:** `tcomet -e matrix.tsv -c conditions.txt --volcano -o results/`
**Explanation:** Generate volcano plot visualization of differential expression results.
