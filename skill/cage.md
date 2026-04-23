---
name: cage
category: variant-calling
description: Changepoint Analysis for Efficient Variant Calling
tags: [cage, variant-calling, changepoint, snp]
author: oxo-call-community
source_url: "https://github.com/adambloniarz/CAGe"
---

## Concepts

- **Tool Overview**: CAGe uses changepoint analysis for efficient variant calling.
- **Core Function**: Detects variants by identifying changepoints in aligned read data.
- **Algorithm**: Statistical changepoint detection for variant boundaries.
- **Input**: Aligned BAM file and reference genome.
- **Output**: Variant calls with statistical confidence.
- **Installation**: Install via bioconda: `conda install -c bioconda cage`

## Pitfalls

- **BAM Required**: Requires properly aligned BAM file.
- **Coverage**: Requires sufficient coverage for changepoint detection.
- **Statistical Model**: Results depend on changepoint model parameters.

## Examples

### Call variants with CAGe
**Args:** `cage -b aligned.bam -r reference.fa -o variants.vcf`
**Explanation:** Detects variants using changepoint analysis.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
