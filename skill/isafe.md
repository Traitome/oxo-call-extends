---
name: isafe
category: population-genomics
description: A program for identifying a favored mutation in positive selective sweep
tags: [isafe, population-genomics, selective-sweep, natural-selection]
author: oxo-call-community
source_url: "https://github.com/alek0991/iSAFE"
---

## Concepts

- **Tool Overview**: iSAFE (Integrated Selection of Alleles by Fitness) - Identifies the favored mutation in positive selective sweep regions
- **Core Algorithm**: Two-step procedure analyzing small recombination windows then combining evidence across ~5Mb regions
- **Population Genetics**: Uses population genetic signals to pinpoint beneficial mutations under selection
- **Output**: Non-negative iSAFE-score for each mutation; higher scores indicate stronger selection evidence
- **Dependencies**: Requires bcftools, numpy, pandas for processing VCF files and statistical calculations
- **Multi-population**: Supports analysis across multiple populations for comparative selection studies

## Pitfalls

- **Region Size**: Optimized for ~5Mb regions; smaller regions may lack statistical power
- **Population Size**: Requires sufficient sample size for reliable allele frequency estimation
- **Recombination Rate**: Performance affected by varying recombination rates across genomic regions
- **Reference Bias**: Results may be influenced by reference genome choice and variant calling quality
- **Computational Requirements**: Memory-intensive for large datasets; may require parallel processing
- **False Positives**: Neutral variants in high LD with selected sites may show elevated scores

## Examples

### Basic iSAFE analysis
**Args:** `isafe --vcf input.vcf --output isafe_scores.txt --region chr1:1-5000000`
**Explanation:** Runs iSAFE on a 5Mb region to identify favored mutations under positive selection.

### Multi-population analysis
**Args:** `isafe --vcf populations.vcf --output multi_pop_scores.txt --populations pop1 pop2 pop3`
**Explanation:** Compares selection signals across multiple populations simultaneously.

### With recombination map
**Args:** `isafe --vcf data.vcf --output results.txt --recomb-map recombination_map.txt`
**Explanation:** Incorporates recombination rate information for improved window-based analysis.

### Sliding window mode
**Args:** `isafe --vcf variants.vcf --output window_results.txt --window-size 100000 --step-size 50000`
**Explanation:** Processes genome in sliding windows of 100kb with 50kb step size.

### High-resolution mode
**Args:** `isafe --vcf high_coverage.vcf --output high_res.txt --high-res`
**Explanation:** Enables high-resolution mode for fine-scale selection detection.

### Filtered analysis
**Args:** `isafe --vcf all.vcf --output filtered.txt --min-allele-count 5 --min-af 0.01`
**Explanation:** Filters variants by minimum allele count and frequency before analysis.