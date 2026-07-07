---
name: stemcnv-check
category: quality-control
description: CNV Based Quality Control Workflow for Stem Cell SNP Array Data.
tags: [stemcnv-check, quality-control, snp-array, stem-cells]
author: oxo-call-community
source_url: "https://stemcnv-check.readthedocs.io"
---

## Concepts

- **Tool Overview**: stemcnv-check (v1.0.0) is a quality control workflow for stem cell SNP array data based on copy number variation (CNV) analysis.
- **Core Function**: Identifies and flags low-quality stem cell lines based on CNV patterns.
- **Algorithm**: Uses Hidden Markov Model (HMM) to detect CNVs and assess genome integrity.
- **Input/Output**: Input: SNP array intensity data; Output: Quality report with CNV calls and quality metrics.
- **Applications**: Quality control for stem cell lines before downstream experiments.
- **Installation**: `conda install -c bioconda stemcnv-check` or download from GitHub.

## Pitfalls

- **Array Quality**: Poor quality SNP array data affects CNV calling.
- **Reference Data**: Incorrect reference genome affects CNV interpretation.
- **Contamination**: Sample contamination produces false CNV calls.
- **Normalization**: Improper normalization affects intensity measurements.
- **Threshold Settings**: Incorrect quality thresholds affect QC decisions.
- **Batch Effects**: Batch effects between arrays affect comparison.

## Examples

### Display help
**Args:** `stemcnv-check --help`
**Explanation:** Shows available options and usage information.

### Basic QC analysis
**Args:** `stemcnv-check -i intensity_data.txt -o qc_report/`
**Explanation:** Run CNV-based QC on SNP array data.

### With reference data
**Args:** `stemcnv-check -i intensity_data.txt -r reference.txt -o qc_report/`
**Explanation:** Use custom reference data for normalization.

### Custom thresholds
**Args:** `stemcnv-check -i intensity_data.txt -o qc_report/ -c 0.95`
**Explanation:** Set confidence threshold to 0.95 for CNV calls.

### Verbose mode
**Args:** `stemcnv-check -i intensity_data.txt -o qc_report/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output VCF
**Args:** `stemcnv-check -i intensity_data.txt -o qc_report/ --vcf`
**Explanation:** Output CNV calls in VCF format.

### Batch processing
**Args:** `stemcnv-check -i batch/ -o qc_reports/`
**Explanation:** Process multiple SNP array datasets.

### Generate HTML report
**Args:** `stemcnv-check -i intensity_data.txt -o qc_report/ --html`
**Explanation:** Generate interactive HTML QC report.

### Validate stem cell line
**Args:** `stemcnv-check -i intensity_data.txt -o qc_report/ --validate`
**Explanation:** Perform comprehensive validation of stem cell quality.
