---
name: idr
category: peak-calling
description: The IDR (Irreproducible Discovery Rate) framework measures reproducibility of findings from replicate experiments and provides stable thresholds based on reproducibility, widely used in ChIP-seq peak calling validation.
tags: [idr, peak-calling, ChIP-seq, reproducibility, ENCODE]
author: oxo-call-community
source_url: "https://github.com/kundajelab/idr"
---

## Concepts

- **Irreproducible Discovery Rate**: IDR quantifies the probability that a peak call is irreproducible across biological replicates, with lower scores indicating higher reproducibility.
- **Copula Mixture Model**: Uses statistical modeling to estimate the reproducibility of ranked peak lists from replicate experiments.
- **Threshold Determination**: Provides stable thresholds for peak calling based on reproducibility rather than arbitrary significance cutoffs.
- **Multi-experiment Integration**: Can integrate results from multiple replicates to produce a single robust peak set.
- **ENCODE Standard**: Widely adopted as the standard method for assessing ChIP-seq peak reproducibility in the ENCODE project.

## Pitfalls

- **Replicate Requirement**: Requires at least two biological replicates; cannot assess reproducibility with single experiments.
- **Input Format**: Requires properly formatted peak files (narrowPeak, broadPeak, or BED format).
- **Threshold Sensitivity**: IDR threshold choice (typically 0.01-0.05) affects the number of reproducible peaks called.
- **Peak Caller Compatibility**: Performance depends on the quality of input peak calls from tools like MACS2 or SPP.
- **Computational Time**: Can be computationally intensive for large peak sets or many replicates.

## Examples

### Basic IDR analysis with two replicates
**Args:** `idr --samples rep1_peaks.narrowPeak rep2_peaks.narrowPeak --output idr_results.txt`
**Explanation:** Compares peaks from two biological replicates and calculates IDR scores for reproducibility assessment.

### With custom threshold
**Args:** `idr --samples rep1.narrowPeak rep2.narrowPeak --output results.txt --idr-threshold 0.01`
**Explanation:** Sets IDR threshold to 0.01 for stricter reproducibility filtering.

### Multiple replicates analysis
**Args:** `idr --samples rep1.narrowPeak rep2.narrowPeak rep3.narrowPeak --output multi_rep_results.txt`
**Explanation:** Integrates three replicates to identify consistently reproducible peaks across all experiments.

### Generate visualization
**Args:** `idr --samples rep1.narrowPeak rep2.narrowPeak --output results.txt --plot`
**Explanation:** Generates diagnostic plots showing IDR score distributions and reproducibility trends.

### With BED format input
**Args:** `idr --samples peaks1.bed peaks2.bed --output results.txt --input-format bed`
**Explanation:** Processes peaks provided in BED format instead of narrowPeak format.