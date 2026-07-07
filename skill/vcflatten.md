---
name: vcflatten
category: bioinformatics
description: vcflatten - VCF flattening tool.
tags: [vcflatten, vcf-processing, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/vcflatten/"
---

## Concepts

- **Tool Overview**: vcflatten - A tool for flattening multi-allelic VCF records.
- **Core Function**: Converts multi-allelic variants to bi-allelic records.
- **Input**: VCF file.
- **Output**: Flattened VCF file.
- **Installation**: Install via pip or conda
- **Use Case**: VCF normalization, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Info Fields**: May lose some INFO field information.

## Examples

### Flatten VCF
**Args:** `vcflatten -i input.vcf -o flattened.vcf`
**Explanation:** Flatten multi-allelic variants.

### With options
**Args:** `vcflatten -i input.vcf -o flattened.vcf -m`
**Explanation:** Keep original multi-allelic info.
