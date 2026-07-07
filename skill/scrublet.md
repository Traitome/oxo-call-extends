---
name: scrublet
category: single-cell
description: scrublet - Doublet prediction in single-cell RNA-sequencing data
tags: ["scrublet", "single-cell", "doublet-detection", "quality-control"]
author: oxo-call-community
source_url: "https://github.com/allonkleinlab/scrubby"
---

## Concepts

- **Tool Overview**: scrublet (v0.2.3) performs doublet prediction in single-cell RNA-sequencing data.
- **Core Function**: Identifies doublet cells in single-cell RNA-seq datasets.
- **Algorithm**: Uses similarity-based approach to detect potential doublets.
- **Input/Output**: Accepts gene expression matrices and produces doublet scores.
- **Single-Cell Focus**: Specifically designed for single-cell RNA-seq data.
- **Applications**: Single-cell RNA-seq quality control, doublet detection, and data cleaning.

## Pitfalls

- **Data Quality**: Results depend on input data quality and sequencing depth.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **False Positives**: May incorrectly flag cells as doublets.
- **False Negatives**: May miss true doublets.

## Examples

### Basic doublet detection
**Args:** `import scrublet; scr = scrublet.Scrublet(counts_matrix)`
**Explanation:** Initializes Scrublet object with count matrix.

### Run doublet detection
**Args:** `doublet_scores, predicted_doublets = scr.scrub_doublets()`
**Explanation:** Detects doublets and returns scores.

### Plot results
**Args:** `scr.plot_histogram()`
**Explanation:** Plots doublet score histogram.

### Set threshold
**Args:** `doublet_scores, predicted_doublets = scr.scrub_doublets(min_counts=2)`
**Explanation:** Sets minimum count threshold.

### Verbose mode
**Args:** `doublet_scores, predicted_doublets = scr.scrub_doublets(verbose=True)`
**Explanation:** Enables verbose output for debugging.

### Get statistics
**Args:** `stats = scr.get_doublet_statistics()`
**Explanation:** Gets doublet detection statistics.

### Save results
**Args:** `scr.save_results('doublet_results.h5ad')`
**Explanation:** Saves results to H5AD file.