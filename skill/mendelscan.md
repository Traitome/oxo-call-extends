---
name: mendelscan
category: utility
description: Analyze exome data for Mendelian disorders and identify causative variants.
tags: [mendelscan, mendelian-genetics, exome-analysis]
author: oxo-call-community
source_url: "https://github.com/genome/mendelscan"
---

## Concepts

- **Tool Overview**: MendelScan analyzes exome sequencing data for Mendelian disorders.
- **Core Function**: Identifies candidate causative variants.
- **Variant Prioritization**: Prioritizes variants based on inheritance patterns.
- **Mendelian Patterns**: Supports autosomal dominant, recessive, and X-linked patterns.
- **Filtering**: Filters variants based on frequency and functional impact.
- **Installation**: `conda install -c bioconda mendelscan`

## Pitfalls

- **Data Quality**: Requires high-quality exome data.
- **Reference Genome**: Must use compatible reference genome.
- **Variant Calling**: Depends on accurate variant calling.
- **False Positives**: May identify spurious variants.
- **Computation Time**: Slow for large datasets.
- **Expert Review**: Results require manual review.

## Examples

### Analyze exome data
**Args:** `mendelscan -i variants.vcf -f family.ped -o results/`
**Explanation:** Analyzes exome data for Mendelian disorders.

### Autosomal recessive mode
**Args:** `mendelscan -i variants.vcf -f family.ped -m recessive -o results/`
**Explanation:** Analyzes for autosomal recessive inheritance.

### With frequency filter
**Args:** `mendelscan -i variants.vcf -f family.ped -f 0.01 -o results/`
**Explanation:** Filters variants by population frequency.

### Verbose mode
**Args:** `mendelscan -i variants.vcf -f family.ped -v -o results/`
**Explanation:** Shows detailed analysis progress.

### Help documentation
**Args:** `mendelscan --help`
**Explanation:** Displays available options.
