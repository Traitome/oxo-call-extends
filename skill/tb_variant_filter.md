---
name: tb_variant_filter
category: analysis
description: TB Variant Filter - Galaxy tool for filtering variants in Mycobacterium tuberculosis WGS data.
tags: [tb-variant-filter, tuberculosis, variant-filtering, galaxy, vcf, mycobacterium]
author: oxo-call-community
source_url: "https://github.com/COMBAT-TB/tb_variant_filter"
---

## Concepts

- **Tool Overview**: tb_variant_filter - A Galaxy workflow tool for filtering genetic variants in M. tuberculosis whole genome sequencing data.
- **Core Function**: Applies various filters to VCF files from TB sequencing projects to remove low-quality variants, common false positives, or intergenic regions.
- **Input**: VCF files from M. tuberculosis WGS analysis, typically from Galaxy pipelines.
- **Output**: Filtered VCF files retaining only high-confidence variants.
- **Installation**: Available through Galaxy Tool Shed, not typically installed via conda directly.
- **Use Case**: Part of the COMBAT-TB Workbench for standardized TB bioinformatics analysis.

## Pitfalls

- **Galaxy Dependency**: Designed for Galaxy workflows - command-line usage requires Galaxy installation.
- **Filter Parameters**: Default filter thresholds may not suit all populations - adjust based on sequencing platform.
- **VCF Format**: Requires properly formatted VCF files with quality scores.

## Examples

### Filter variants in Galaxy
**Args:** Select "TB Variant Filter" tool in Galaxy, upload VCF file, configure filter parameters.
**Explanation:** Standard Galaxy interface usage - select input VCF and set filter criteria through web interface.
