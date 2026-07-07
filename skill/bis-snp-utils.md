---
name: bis-snp-utils
category: epigenomics
description: Support utilities for Bis-SNP bisulfite sequencing analysis
tags: [bisulfite, methylation, utilities, epigenomics]
author: oxo-call-community
source_url: "https://github.com/dnaase/Bis-tools"
---

## Concepts

- **Tool Overview**: bis-snp-utils provides supporting utility tools for Bis-SNP, a bisulfite-seq SNP and cytosine methylation caller.
- **Data Processing**: Utilities for processing and filtering Bis-SNP output.
- **Format Conversion**: Converts between different formats for downstream analysis.
- **Quality Filtering**: Provides filtering options for methylation and SNP calls.
- **Applications**: Bisulfite sequencing data processing, methylation analysis preparation.

## Pitfalls

- **Bis-SNP Dependency**: Designed to work with Bis-SNP output files.
- **Version Compatibility**: Ensure version compatibility with Bis-SNP.

## Examples

### Filter low-quality methylation calls
**Args:** `bis-snp-utils filter-methylation -i methylation.bed -q 20 -o filtered.bed`
**Explanation:** Filters methylation calls with quality below 20.

### Convert VCF to table
**Args:** `bis-snp-utils vcf-to-table -i variants.vcf -o variants.tsv`
**Explanation:** Converts Bis-SNP VCF output to tab-delimited table.