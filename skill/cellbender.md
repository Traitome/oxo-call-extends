---
name: cellbender
category: qc
description: Remove background RNA and technical artifacts from scRNA-seq data
tags: [cellbender, single-cell, scrna-seq, background-removal, ambient-rna, qc]
author: oxo-call-community
source_url: "https://github.com/broadinstitute/CellBender"
---

## Concepts

- **Tool Overview**: CellBender is a software package for eliminating technical artifacts from high-throughput single-cell RNA sequencing data. The main command `remove-background` removes ambient/background RNA contamination.
- **Core Function**: Uses a deep generative model to estimate and remove ambient RNA contamination from count matrices, producing a "cleaned" matrix for downstream analysis.
- **Input/Output**: Input: Raw feature-barcode matrix from CellRanger (.h5 format). Output: Cleaned .h5 matrix, filtered matrix, cell barcode list, and diagnostic reports.
- **GPU Acceleration**: Strongly recommended to use `--cuda` for GPU acceleration. CPU-only mode is much slower.
- **Checkpoint System**: Saves model checkpoint (ckpt.tar.gz) that can be reused to generate outputs with different FPR settings without retraining.
- **Output Files**: Produces 9 files including cleaned .h5, filtered .h5, cell barcodes CSV, HTML report, PDF summary, and checkpoint.

## Pitfalls

- **GPU Recommended**: Running without `--cuda` is extremely slow for large datasets. Always use GPU if available.
- **Epochs Selection**: 150 epochs is typically sufficient. Do not exceed 300 to avoid overfitting.
- **Large Checkpoint File**: The ckpt.tar.gz checkpoint file can be very large. Delete it after final analysis if not needed for re-running.
- **Input Format**: Only accepts .h5 format from CellRanger. For other formats, convert first.
- **FPR Setting**: Default FPR of 0.01 is conservative. Can try multiple FPR values (0.0, 0.01, 0.05, 0.1) using checkpoint to avoid retraining.
- **Learning Rate**: If ELBO curve shows large drops, reduce learning rate (e.g., from 1e-4 to 5e-5).

## Examples

### Basic usage with GPU
**Args:** `remove-background --cuda --input raw_feature_bc_matrix.h5 --output output.h5`
**Explanation:** Removes background RNA using GPU acceleration, auto-determines expected cells and droplet count.

### Specify expected cells
**Args:** `remove-background --cuda --input raw.h5 --output output.h5 --expected-cells 5000 --total-droplets-included 25000`
**Explanation:** Manually sets expected cell count and total droplets, useful when auto-detection fails.

### Run without GPU
**Args:** `remove-background --input raw.h5 --output output.h5 --epochs 150`
**Explanation:** CPU-only mode, omit --cuda flag. Will be significantly slower but produces same results.

### Generate outputs with multiple FPR values
**Args:** `remove-background --cuda --input raw.h5 --output output.h5 --fpr 0.0 0.01 0.05 0.1`
**Explanation:** Generates multiple output matrices with different false positive rates in a single run.

### Re-run with different FPR using checkpoint
**Args:** `remove-background --checkpoint ckpt.tar.gz --fpr 0.05 --input raw.h5 --output output_fpr005.h5`
**Explanation:** Uses existing checkpoint to generate output with different FPR without retraining the model.

### Adjust learning rate for unstable training
**Args:** `remove-background --cuda --input raw.h5 --output output.h5 --learning-rate 5e-5`
**Explanation:** Reduces learning rate from default 1e-4 to 5e-5 for more stable training when ELBO curve is noisy.

### Limit training epochs
**Args:** `remove-background --cuda --input raw.h5 --output output.h5 --epochs 100`
**Explanation:** Uses fewer epochs for faster results on well-behaved datasets where convergence is quick.
