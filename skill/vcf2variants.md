---
name: vcf2variants
category: bioinformatics
description: vcf2variants - VCF variant extraction tool.
tags: [vcf2variants, vcf-processing, variant-extraction, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vcf2variants/"
---

## Concepts

- **Tool Overview**: vcf2variants - A tool for extracting variants from VCF.
- **Core Function**: Extracts specific variant types from VCF files.
- **Input**: VCF file.
- **Output**: Extracted variants.
- **Installation**: Install via pip or conda
- **Use Case**: Variant extraction, filtering, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Filter Criteria**: Requires well-defined filter criteria.

## Examples

### Extract variants
**Args:** `vcf2variants -i input.vcf -o output.vcf -t snp`
**Explanation:** Extract SNPs.

### With options
**Args:** `vcf2variants -i input.vcf -o output.vcf -t indel -q 30`
**Explanation:** Extract indels with quality > 30.
