---
name: manormfast
category: utility
description: MAnorm version, Fast but more memory
tags: [manormfast, utility, ChIP-seq, normalization]
author: oxo-call-community
source_url: "https://github.com/semal/MAnormFast"
---

## Concepts

- **Tool Overview**: manormfast v0.1.2 - A faster implementation of MAnorm for quantitative comparison of ChIP-seq data, optimized for speed at the cost of increased memory usage.
- **Core Function**: Performs normalization and comparison of ChIP-seq signal intensities between samples.
- **Input/Output**: Input: Peak files (BED), signal files; Output: Normalized signal values, differential binding results.
- **Installation**: `conda install -c bioconda manormfast`
- **Speed Optimization**: Uses optimized algorithms for faster processing.
- **Memory Trade-off**: Achieves speed by using more memory for caching.

## Pitfalls

- **Memory Usage**: Requires significant memory for large datasets.
- **Input Format**: Requires properly formatted peak and signal files.
- **Normalization Sensitivity**: Sensitive to input data quality.
- **Peak Overlap**: Requires sufficient peak overlap between samples.
- **Parameter Tuning**: Incorrect parameters affect normalization.
- **Output Files**: Multiple output files require careful organization.

## Examples

### Run MAnormFast
**Args:** `manormfast -p peaks.bed -s signal.txt -o results/`
**Explanation:** Performs normalization on ChIP-seq data.

### With control sample
**Args:** `manormfast -p peaks.bed -s signal.txt -c control_signal.txt -o results/`
**Explanation:** Uses control sample for normalization.

### Custom bin size
**Args:** `manormfast -p peaks.bed -s signal.txt -o results/ -b 50`
**Explanation:** Sets custom bin size to 50 bp.

### Verbose mode
**Args:** `manormfast -p peaks.bed -s signal.txt -o results/ -v`
**Explanation:** Provides detailed logging during processing.

### Differential binding analysis
**Args:** `manormfast -p peaks.bed -s signal.txt -c control.txt -o results/ --diff`
**Explanation:** Performs differential binding analysis.

### Generate report
**Args:** `manormfast -p peaks.bed -s signal.txt -o results/ --report`
**Explanation:** Generates HTML report of results.