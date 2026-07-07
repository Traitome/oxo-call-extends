---
name: stringmeup
category: metagenomics
description: A post-processing tool to reclassify Kraken 2 output based on the confidence score and/or minimum minimizer hit groups.
tags: [stringmeup, metagenomics, kraken2, classification]
author: oxo-call-community
source_url: "https://github.com/danisven/StringMeUp"
---

## Concepts

- **Tool Overview**: stringmeup (v0.1.5) is a post-processing tool for improving Kraken 2 metagenomic classification results.
- **Core Function**: Reclassifies Kraken 2 output based on confidence scores and minimizer hit groups.
- **Algorithm**: Uses statistical methods to refine taxonomic classification from Kraken 2 results.
- **Input/Output**: Input: Kraken 2 output file; Output: Reclassified taxonomic assignments.
- **Applications**: Metagenomics analysis, taxonomic profiling, microbiome research.
- **Installation**: `conda install -c bioconda stringmeup` or download from GitHub.

## Pitfalls

- **Input Format**: Requires specific Kraken 2 output format.
- **Database Quality**: Outdated databases affect classification accuracy.
- **Confidence Threshold**: Incorrect thresholds affect results.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large classification results can be slow.
- **Kraken2 Version**: Requires compatible Kraken 2 version.

## Examples

### Display help
**Args:** `stringmeup --help`
**Explanation:** Shows available options and usage information.

### Basic reclassification
**Args:** `stringmeup -i kraken_output.txt -o reclassified.txt`
**Explanation:** Reclassify Kraken 2 output.

### With custom confidence
**Args:** `stringmeup -i kraken_output.txt -o reclassified.txt -c 0.5`
**Explanation:** Use confidence threshold of 0.5.

### Verbose mode
**Args:** `stringmeup -i kraken_output.txt -o reclassified.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `stringmeup -i kraken_output.txt -o reclassified.txt --stats`
**Explanation:** Generate statistics about reclassification.

### Batch processing
**Args:** `stringmeup -i batch/ -o results/`
**Explanation:** Process multiple Kraken 2 output files together.

### Filter by hits
**Args:** `stringmeup -i kraken_output.txt -o reclassified.txt -m 3`
**Explanation:** Minimum minimizer hit groups of 3.

### Include unclassified
**Args:** `stringmeup -i kraken_output.txt -o reclassified.txt --include-unclassified`
**Explanation:** Include unclassified reads in output.

### Generate report
**Args:** `stringmeup -i kraken_output.txt -o reclassified.txt --report`
**Explanation:** Generate comprehensive HTML report.
