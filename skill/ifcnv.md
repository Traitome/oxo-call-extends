---
name: ifcnv
category: variant-calling
description: ifCNV is an isolation-forest-based package to detect copy number variations from various NGS datasets without requiring a separate reference dataset.
tags: [ifcnv, variant-calling, CNV, copy number variation, machine learning]
author: oxo-call-community
source_url: "https://github.com/SimCab-CHU/ifCNV"
---

## Concepts

- **Isolation Forest Algorithm**: Uses unsupervised machine learning to identify anomalous samples with copy number variations.
- **Self-Reference Creation**: Automatically creates its own reference from the input dataset, eliminating the need for separate controls.
- **Dual Isolation Forests**: Uses two isolation forests to detect both amplifications and deletions.
- **Comprehensive Scoring**: Implements a scoring method to quantify CNV likelihood and localization.
- **Multi-platform Support**: Works with targeted NGS data from capture and amplicon sequencing, germline and somatic studies.

## Pitfalls

- **Sample Size Requirements**: Requires sufficient sample numbers to build a reliable reference distribution.
- **Targeted Sequencing**: Optimized for targeted sequencing; may not perform optimally on whole-genome data.
- **Parameter Tuning**: Detection sensitivity may require adjustment of forest parameters for specific datasets.
- **Low Coverage**: Performance may degrade with very low sequencing coverage.
- **Complex CNVs**: May have difficulty detecting complex structural variations or mosaic CNVs.

## Examples

### Basic CNV detection
**Args:** `ifcnv --input reads_matrix.tsv --output cnv_results.csv`
**Explanation:** Runs ifCNV on a matrix of read counts to detect CNVs across samples.

### With custom parameters
**Args:** `ifcnv --input data.tsv --output results.csv --n-estimators 100 --contamination 0.1`
**Explanation:** Configures isolation forest parameters for specific dataset characteristics.

### Amplicon sequencing data
**Args:** `ifcnv --input amplicon_data.tsv --output results.csv --mode amplicon`
**Explanation:** Processes amplicon sequencing data with mode optimized for this data type.

### Generate report
**Args:** `ifcnv --input data.tsv --output results.csv --report`
**Explanation:** Generates a comprehensive HTML report with CNV analysis results.

### Filter by quality
**Args:** `ifcnv --input data.tsv --output results.csv --min-quality 20`
**Explanation:** Filters low-quality reads before CNV detection analysis.