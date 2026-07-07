---
name: conifer
category: utility
description: Calculate confidence scores from Kraken2 metagenomic classification
tags: [conifer, kraken2, metagenomics, confidence-scores, taxonomic-classification]
author: oxo-call-community
source_url: "https://github.com/Ivarz/Conifer"
---

## Concepts

- **Tool Overview**: Conifer is a tool for calculating confidence scores from Kraken2 metagenomic taxonomic classification output, improving the reliability of species identification.
- **Core Function**: Processes Kraken2 output to compute statistical confidence scores for taxonomic assignments, filtering false positives.
- **Algorithm**: Uses statistical models to evaluate the reliability of k-mer based taxonomic assignments.
- **Input**: Kraken2 classification output files.
- **Output**: Confidence-scored taxonomic assignments with filtered results.
- **Application**: Metagenomic analysis validation, pathogen detection, and microbiome studies.
- **Installation**: Install via bioconda: `conda install -c bioconda conifer`

## Pitfalls

- **Kraken2 Dependency**: Requires Kraken2 output as input.
- **Threshold Selection**: Confidence thresholds affect sensitivity and specificity.
- **Database Bias**: Confidence scores depend on Kraken2 database completeness.
- **Low Abundance**: Low-abundance taxa may have lower confidence scores.
- **Novel Organisms**: May assign low confidence to novel or underrepresented taxa.

## Examples

### Calculate confidence scores
**Args:** `conifer -i kraken2_output.txt -o confidence_scores.txt`
**Explanation:** Calculates confidence scores from Kraken2 classification results.

### With confidence threshold
**Args:** `conifer -i kraken2_output.txt -t 0.9 -o filtered_results.txt`
**Explanation:** Filters results to include only assignments with >=90% confidence.

### Generate summary report
**Args:** `conifer -i kraken2_output.txt -s -o summary_report.txt`
**Explanation:** Generates summary report of confidence score distributions.

### Display help
**Args:** `conifer --help`
**Explanation:** Shows all available options and usage information.