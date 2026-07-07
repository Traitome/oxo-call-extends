---
name: vcf-annotator
category: bioinformatics
description: vcf-annotator - VCF annotation tool.
tags: [vcf-annotator, vcf-annotation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/vcf-annotator/"
---

## Concepts

- **Tool Overview**: vcf-annotator - A tool for annotating VCF files.
- **Core Function**: Annotates variants with functional information.
- **Input**: VCF file.
- **Output**: Annotated VCF file.
- **Installation**: Install via pip or conda
- **Use Case**: Variant annotation, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Databases**: Requires annotation databases.

## Examples

### Annotate VCF
**Args:** `vcf-annotator -i input.vcf -o annotated.vcf`
**Explanation:** Annotate VCF file.

### With options
**Args:** `vcf-annotator -i input.vcf -o annotated.vcf -d clinvar`
**Explanation:** Use ClinVar database.
