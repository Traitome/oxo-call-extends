---
name: vembrane
category: bioinformatics
description: vembrane - Variant filtering tool.
tags: [vemembrane, vcf-processing, filtering, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vembrane/vembrane"
---

## Concepts

- **Tool Overview**: vembrane - Fast VCF filtering tool.
- **Core Function**: Filters VCF files using Python expressions.
- **Input**: VCF file.
- **Output**: Filtered VCF file.
- **Installation**: Install via pip or conda
- **Use Case**: VCF filtering, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Expressions**: Requires Python expression knowledge.

## Examples

### Filter VCF
**Args:** `vembrane -f "QUAL > 30" input.vcf > filtered.vcf`
**Explanation:** Filter by quality.

### With options
**Args:** `vembrane -f "INFO['DP'] > 10" input.vcf > filtered.vcf`
**Explanation:** Filter by depth.
