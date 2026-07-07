---
name: vulcan
category: bioinformatics
description: Vulcan - Variant prioritization tool.
tags: [vulcan, variant-analysis, prioritization, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vulcan/"
---

## Concepts

- **Tool Overview**: Vulcan - Variant prioritization tool.
- **Core Function**: Prioritizes variants based on multiple criteria.
- **Input**: VCF file.
- **Output**: Prioritized variants.
- **Installation**: Install via pip or conda
- **Use Case**: Variant analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Parameters**: Threshold selection affects results.

## Examples

### Prioritize variants
**Args:** `vulcan -i input.vcf -o prioritized.txt`
**Explanation:** Prioritize variants.

### With options
**Args:** `vulcan -i input.vcf -o prioritized.txt -m pathogenicity`
**Explanation:** Prioritize by pathogenicity.
