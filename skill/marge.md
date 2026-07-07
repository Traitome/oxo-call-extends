---
name: marge
category: expression
description: Model-based Analysis of Regulation of Gene Expression
tags: [marge, expression, gene-regulation, ChIP-seq]
author: oxo-call-community
source_url: "http://cistrome.org/MARGE"
---

## Concepts

- **Tool Overview**: marge v1.0 - MARGE (Model-based Analysis of Regulation of Gene Expression) integrates ChIP-seq and gene expression data.
- **Core Function**: Identifies transcription factor targets by integrating ChIP-seq binding data with gene expression profiles.
- **Input/Output**: Input: ChIP-seq peaks, gene expression data; Output: Regulatory relationships, target genes.
- **Installation**: `conda install -c bioconda marge`
- **Multi-omics Integration**: Combines ChIP-seq and RNA-seq data for regulatory analysis.
- **Statistical Modeling**: Uses statistical models to infer regulatory relationships.

## Pitfalls

- **Data Quality**: Poor quality ChIP-seq or expression data affects results.
- **Sample Matching**: Requires properly matched samples across assays.
- **Normalization**: Data must be properly normalized before analysis.
- **Parameter Tuning**: Incorrect parameters affect target prediction.
- **False Positives**: May identify false positive regulatory relationships.
- **Computational Resources**: Large datasets require significant memory.

## Examples

### Run MARGE analysis
**Args:** `marge -p peaks.bed -e expression.csv -o results/`
**Explanation:** Integrates ChIP-seq peaks with gene expression data.

### With background regions
**Args:** `marge -p peaks.bed -e expression.csv -b background.bed -o results/`
**Explanation:** Uses custom background regions.

### Multiple factors
**Args:** `marge -p peaks/ -e expression.csv -o results/`
**Explanation:** Processes multiple ChIP-seq peak files.

### Verbose mode
**Args:** `marge -p peaks.bed -e expression.csv -o results/ -v`
**Explanation:** Provides detailed logging during analysis.

### Generate report
**Args:** `marge -p peaks.bed -e expression.csv -o results/ --report`
**Explanation:** Generates comprehensive analysis report.

### Statistical significance
**Args:** `marge -p peaks.bed -e expression.csv -o results/ -p 0.05`
**Explanation:** Sets significance threshold to 0.05.