---
name: vase
category: bioinformatics
description: VASE - Variant Annotation and Selection Engine.
tags: [vase, variant-annotation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/vase/"
---

## Concepts

- **Tool Overview**: VASE - A tool for variant annotation and selection.
- **Core Function**: Annotates and selects variants based on criteria.
- **Input**: VCF file.
- **Output**: Annotated and selected variants.
- **Installation**: Install via pip or conda
- **Use Case**: Variant annotation, filtering, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Database Requirements**: Requires annotation databases.

## Examples

### Annotate and select
**Args:** `vase -i variants.vcf -o selected.vcf`
**Explanation:** Annotate and select variants.

### With options
**Args:** `vase -i variants.vcf -o selected.vcf -f "AF>0.01"`
**Explanation:** Filter by allele frequency.
