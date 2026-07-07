---
name: cellqc
category: single-cell
description: Standardizes quality control of single-cell RNA-Seq data to produce clean feature count matrices
tags: [cellqc, single-cell, scrna-seq, quality-control, qc]
author: oxo-call-community
source_url: "https://github.com/lijinbio/cellqc"
---

## Concepts

- **Tool Overview**: cellqc standardizes quality control of single-cell RNA-Seq data.
- **Core Function**: Filters and cleans scRNA-seq data to produce high-quality count matrices.
- **Features**: Cell filtering, gene filtering, normalization, and QC metrics calculation.
- **Input**: Raw scRNA-seq count matrix (h5ad, MTX, or CSV).
- **Output**: Cleaned count matrix and QC report.
- **Application**: Single-cell RNA-seq data preprocessing and quality assessment.
- **Installation**: Install via bioconda: `conda install -c bioconda cellqc`

## Pitfalls

- **Data Format**: Requires specific input formats (h5ad, MTX, CSV).
- **Parameter Tuning**: QC thresholds may need adjustment for different datasets.
- **Memory Usage**: Large datasets may require significant memory.
- **Batch Effects**: May need additional batch effect correction.

## Examples

### Run basic QC
**Args:** `cellqc run -i raw_data.h5ad -o clean_data.h5ad`
**Explanation:** Runs standard QC pipeline on scRNA-seq data.

### With custom thresholds
**Args:** `cellqc run -i data.h5ad -o clean.h5ad --min-genes 200 --max-genes 5000`
**Explanation:** Applies custom gene count thresholds for filtering.

### Generate QC report
**Args:** `cellqc report -i data.h5ad -o qc_report.html`
**Explanation:** Generates HTML QC report with visualization.

### Display help
**Args:** `cellqc --help`
**Explanation:** Shows all available options and usage information.