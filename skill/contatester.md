---
name: contatester
category: formatting
description: Compute allelic balance and detect contamination from VCF files
tags: [contatester, allelic-balance, contamination, vcf, quality-control]
author: oxo-call-community
source_url: "https://github.com/CNRGH/contatester"
---

## Concepts

- **Tool Overview**: Contatester computes the allelic balance of a sample from VCF files and detects cross-human contamination using efficient algorithms.
- **Core Function**: Analyzes variant allele frequencies to calculate allelic balance and estimate contamination levels in sequencing samples.
- **Algorithm**: Uses statistical methods to analyze heterozygous variant distributions and detect contamination signatures.
- **Input**: VCF files with variant calls, optionally BAM files for additional analysis.
- **Output**: Allelic balance metrics and contamination estimates.
- **Application**: Sample quality control, contamination detection, and variant calling validation.
- **Installation**: Install via bioconda: `conda install -c bioconda contatester`

## Pitfalls

- **Variant Quality**: Results depend on accurate variant calling.
- **Coverage Requirements**: Requires sufficient coverage at heterozygous sites.
- **Population Bias**: Reference allele frequencies may not match all populations.
- **Relatedness**: May detect related samples as contaminated.
- **Low Contamination**: Very low contamination levels may be difficult to detect.

## Examples

### Compute allelic balance
**Args:** `contatester -i variants.vcf -o allelic_balance.txt`
**Explanation:** Computes allelic balance from VCF file.

### Estimate contamination
**Args:** `contatester -i variants.vcf --contamination -o contamination_estimate.txt`
**Explanation:** Estimates contamination level from variant data.

### With reference panel
**Args:** `contatester -i variants.vcf -r reference_panel.vcf -o results.txt`
**Explanation:** Uses reference panel for improved contamination estimation.

### Display help
**Args:** `contatester --help`
**Explanation:** Shows all available options and usage information.