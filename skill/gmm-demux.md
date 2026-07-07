---
name: gmm-demux
category: demultiplexing
description: gmm-demux - Gaussian Mixture Model-based demultiplexing for cell hashing and MULTI-seq.
tags: [gmm-demux, demultiplexing, single-cell, cell-hashing]
author: oxo-call-community
source_url: "https://github.com/CHPGenetics/GMM-demux"
---

## Concepts
- **Demultiplexing**: Demultiplexes sample barcodes.
- **Gaussian Mixture Models**: Uses GMM for classification.
- **Cell Hashing**: Processes cell hashing data.
- **MULTI-seq**: Supports MULTI-seq protocols.
- **Single-cell Analysis**: Enables single-cell analysis.

## Pitfalls
- **Barcode Quality**: Requires high-quality barcodes.
- **Sample Mixing**: Complex samples may affect accuracy.
- **Threshold Selection**: Requires threshold selection.
- **Data Quality**: Requires high-quality data.
- **Result Validation**: Results require validation.

## Examples
### Demultiplex samples
**Args:** `GMM-demux -i counts.h5ad -o demux.h5ad`
**Explanation:** Demultiplexes single-cell data.

### With parameters
**Args:** `GMM-demux -i counts.h5ad -o demux.h5ad -t 0.5 -n 1000`
**Explanation:** Uses specific thresholds.

### Generate report
**Args:** `GMM-demux -i counts.h5ad -o demux.h5ad -r -report`
**Explanation:** Generates demux report.

### Validate results
**Args:** `GMM-demux -i counts.h5ad -v -o validation.txt`
**Explanation:** Validates demux results.

### Batch processing
**Args:** `GMM-demux -l samples.txt -o ./demux/`
**Explanation:** Processes multiple samples.