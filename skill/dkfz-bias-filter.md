---
name: dkfz-bias-filter
category: variant-calling
description: DKFZ bias filter - Flags SNVs showing sequence context bias.
tags: [dkfz-bias-filter, variant-calling, filtering, bias, snv, quality-control]
author: oxo-call-community
source_url: "https://github.com/eilslabs/DKFZBiasFilter"
---

## Concepts

- **Tool Overview**: DKFZ Bias Filter (v1.2.3a+) filters SNVs showing sequence context bias in variant calls.
- **Core Function**: Flags and filters variant calls that show evidence of sequencing or alignment bias.
- **Input/Output**: Input: VCF files with variant calls. Output: Filtered VCF with bias annotations.
- **Algorithm**: Analyzes sequence context around variants to detect systematic biases.
- **Key Features**: Bias detection, variant filtering, context analysis, annotation, quality control.
- **Installation**: `conda install -c bioconda dkfz-bias-filter`

## Pitfalls

- **Input Requirements**: Requires VCF with variant calls and read support information.
- **Read Depth**: Requires sufficient read depth for reliable bias detection.
- **Context Analysis**: Sequence context window size affects results.
- **False Positives**: May flag true variants as biased in repetitive regions.
- **Format Requirements**: VCF must contain proper FORMAT fields.

## Examples

### Filter biased SNVs
**Args:** `dkfz-bias-filter --input variants.vcf --output filtered.vcf`
**Explanation:** Filters biased SNVs from variant calls.

### With custom thresholds
**Args:** `dkfz-bias-filter --input variants.vcf --output filtered.vcf --bias-threshold 0.1`
**Explanation:** Use custom bias threshold for filtering.

### Annotate without filtering
**Args:** `dkfz-bias-filter --input variants.vcf --output annotated.vcf --annotate-only`
**Explanation:** Add bias annotations without filtering.

### Generate bias report
**Args:** `dkfz-bias-filter --input variants.vcf --output filtered.vcf --report bias_report.tsv`
**Explanation:** Generate detailed bias statistics report.

### Filter specific variant types
**Args:** `dkfz-bias-filter --input variants.vcf --output filtered.vcf --filter-type snp`
**Explanation:** Only filter SNP variants.