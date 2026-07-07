---
name: mamotif
category: utility
description: An integrative toolkit for detecting cell type-specific regulators
tags: [mamotif, utility, single-cell, regulators]
author: oxo-call-community
source_url: "https://github.com/shao-lab/MAmotif"
---

## Concepts

- **Tool Overview**: mamotif v1.1.0 - An integrative toolkit for detecting cell type-specific regulators using single-cell ATAC-seq and RNA-seq data.
- **Core Function**: Identifies transcription factors and regulatory elements specific to cell types from multi-omics data.
- **Input/Output**: Input: ATAC-seq peaks, gene expression data, motif databases; Output: Cell type-specific regulators, enrichment scores.
- **Installation**: `conda install -c bioconda mamotif`
- **Multi-omics Integration**: Combines chromatin accessibility and gene expression data.
- **Motif Analysis**: Uses motif scanning to identify potential regulatory elements.

## Pitfalls

- **Data Quality**: Poor quality sequencing data affects results.
- **Motif Database**: Outdated motif databases miss novel regulators.
- **Cell Type Annotation**: Requires accurate cell type labels.
- **Computational Resources**: Large datasets require significant memory.
- **False Positives**: May identify non-functional motifs.
- **Parameter Tuning**: Incorrect thresholds affect regulator detection.

## Examples

### Detect cell type-specific regulators
**Args:** `mamotif detect -a atac_peaks.bed -e expression.csv -m motifs.jaspar -o regulators.txt`
**Explanation:** Identifies cell type-specific regulators.

### With custom background
**Args:** `mamotif detect -a atac_peaks.bed -e expression.csv -m motifs.jaspar -b background.bed -o regulators.txt`
**Explanation:** Uses custom background regions.

### Enrichment analysis
**Args:** `mamotif enrich -a atac_peaks.bed -m motifs.jaspar -o enrichment.txt`
**Explanation:** Performs motif enrichment analysis.

### Visualize results
**Args:** `mamotif plot -i regulators.txt -o plot.pdf`
**Explanation:** Creates visualization of regulator scores.

### Batch processing
**Args:** `mamotif batch -i data/ -o results/`
**Explanation:** Processes multiple datasets in batch.

### Verbose mode
**Args:** `mamotif detect -a atac_peaks.bed -e expression.csv -m motifs.jaspar -o regulators.txt -v`
**Explanation:** Provides detailed logging during analysis.