---
name: fithic
category: utility
description: "Fit-Hi-C is a tool for assigning statistical confidence estimates to chromosomal contact maps from Hi-C experiments, identifying significant chromatin interactions."
tags: [fithic, utility, hi-c, chromatin, interaction, 3d-genome, genomics, contacts, statistics]
author: oxo-call-community
source_url: "https://github.com/ay-lab/fithic/tree/master"
---

## Concepts
- **Tool Overview**: Fit-Hi-C (Fitness test for Hi-C) assigns statistical confidence estimates to chromosomal contact maps from Hi-C experiments. It identifies significant chromatin interactions while accounting for genomic distance biases.
- **Core Function**: Fits a non-parametric spline model relating contact probability to genomic distance, then uses binomial tests to identify contact pairs with significantly higher counts than expected under the distance model.
- **Algorithm**: Uses monotonically non-increasing spline fitting without parametric assumptions. Applies bias corrections for locus-specific and bin-specific factors to account for experimental biases.
- **Resolution Range**: Originally designed for mid-range contacts (20kb-2Mb). FitHiC2 extension supports genome-wide analysis at all distances including inter-chromosomal contacts.
- **Statistical Output**: Computes p-values via binomial test, then applies Benjamini-Hochberg FDR correction to generate Q-values for each contact.
- **Filtering Options**: Includes merging filter module to remove indirect/bystander interactions, reducing false positives from transitive contacts.
- **Installation**: `conda install -c bioconda fithic` or `pip install fithic`. Requires R version >=3.0 for the R package implementation.

## Pitfalls
- **Resolution Selection**: Resolution must match Hi-C data preprocessing. Using wrong bin size (e.g., 10kb on 40kb data) produces meaningless results.
- **ICE/KR Normalization**: Strongly recommended to use bias values from matrix balancing (ICE or KR normalization). Unnormalized data may have significant technical bias.
- **Interaction Distance Range**: Fit-Hi-C is optimized for intra-chromosomal mid-range contacts. Very short-range (<10kb) and long-range (>5Mb) estimates are less reliable.
- **Memory Usage**: High-resolution Hi-C matrices (5-10kb) are extremely large. Process chromosome-by-chromosome or use chunked processing to avoid memory exhaustion.
- **Statistical Threshold**: Q-value threshold selection significantly affects results. Stringent thresholds (Q<0.01) reduce false positives but may miss true weak interactions.
- **Replicates vs Merged**: For multiple replicates, analyze each separately then intersect significant contacts rather than merging raw counts before analysis.

## Examples
### Basic FitHiC run with R
**Args:** `Rscript fithic.r --interactions input.bedGraph --resolution 10000 --outdir results/`
**Explanation:** Standard Rscript invocation for FitHiC. Takes Hi-C interaction matrix in BEDGraph format at specified resolution.

### Python command-line usage
**Args:** `fithic -i input.interactions -r 10000 -o results/`
**Explanation:** Python implementation of FitHiC. Uses same parameters as R version with simpler syntax for pipeline integration.

### With bias correction
**Args:** `fithic -i contacts.bedgraph -b bias_values.txt -r 25000 -o results/`
**Explanation:** Provides explicit bias values file from ICE/KR normalization. Improves accuracy by accounting for experimental biases.

### Specify distance range
**Args:** `fithic -i contacts.bedgraph -r 50000 --min-dist 200000 --max-dist 2000000 -o results/`
**Explanation:** Filters analysis to contacts between 200kb-2Mb. Useful for focusing on specific interaction ranges relevant to research question.

### FitHiC2 with merging filter
**Args:** `fithic2 -i contacts.bedgraph -b bias.txt -r 10000 --apply-merge-filter -o results/`
**Explanation:** FitHiC2 version with merging filter to remove indirect interactions. Significantly reduces false positives from bystander effects.

### Generate Q-Q plot
**Args:** `fithic -i contacts.bedgraph -r 25000 --generate-qq -o results/`
**Explanation:** Produces Q-Q plot comparing observed vs expected p-value distributions. Diagnostic for detecting systematic biases in data.

### Extract significant contacts
**Args:** `awk '$7 < 0.01' fithic_output.bedgraph > significant_contacts.bed`
**Explanation:** Filters FitHiC output to contacts with Q-value < 0.01 (1% FDR). Column 7 typically contains the Q-value.

### Process specific chromosome
**Args:** `fithic -i contacts.bedgraph -r 50000 --chrom chr5 -o results_chr5/`
**Explanation:** Runs FitHiC only on chromosome 5. Useful for debugging or focusing on specific genomic regions before full analysis.

### Set number of spline knots
**Args:** `fithic -i contacts.bedgraph -r 25000 --num-knots 20 -o results/`
**Explanation:** Controls spline flexibility. More knots = more flexible distance curve but risk overfitting. Default is usually sufficient but may need adjustment for unusual data.
