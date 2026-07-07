---
name: dropkick
category: expression
description: "Automated scRNA-seq filtering"
tags: [dropkick, expression, single-cell, RNA-seq, quality-control]
author: oxo-call-community
source_url: "https://github.com/KenLauLab/dropkick"
---

## Concepts

- **Tool Overview**: dropkick is an automated tool for quality filtering of single-cell RNA sequencing data.
- **Core Function**: Identifies and removes low-quality cells from scRNA-seq datasets.
- **Input/Output**: Input: Gene expression matrix (CSV/loom/AnnData). Output: Filtered matrix, QC metrics.
- **Algorithm**: Uses machine learning to predict cell quality based on multiple QC features.
- **Key Features**: Automated quality filtering, interpretable QC metrics, visualization tools, batch-aware processing.
- **Installation**: `conda install -c bioconda dropkick`

## Pitfalls

- **Training Data**: Model performance depends on training data quality and representativeness.
- **Threshold Selection**: Default thresholds may need adjustment for specific datasets.
- **Low Complexity**: Very low complexity datasets may produce unreliable predictions.
- **Batch Effects**: Batch-specific quality patterns may require batch-aware filtering.
- **Cell Type Effects**: Cell type-specific QC patterns can affect filtering decisions.

## Examples

### Basic filtering
**Args:** `--input counts.csv --output filtered_counts.csv`
**Explanation:** Filters low-quality cells from scRNA-seq expression matrix.

### Custom threshold
**Args:** `--input counts.csv --output filtered_counts.csv --threshold 0.9`
**Explanation:** Uses higher confidence threshold (0.9) for cell filtering.

### Generate QC report
**Args:** `--input counts.csv --output filtered_counts.csv --report qc_report.html`
**Explanation:** Generates HTML QC report with filtering statistics.

### Batch-aware filtering
**Args:** `--input counts.csv --output filtered_counts.csv --batch batch_labels.txt`
**Explanation:** Performs batch-aware filtering to account for technical variation.

### Visualize results
**Args:** `--input counts.csv --output filtered_counts.csv --plot qc_plot.png`
**Explanation:** Creates visualization of QC metrics and filtering results.