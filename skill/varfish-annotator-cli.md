---
name: varfish-annotator-cli
category: bioinformatics
description: VarFish Annotator CLI - Variant annotation tool.
tags: [varfish-annotator-cli, variant-annotation, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/varfish-org/varfish-annotator-cli"
---

## Concepts

- **Tool Overview**: VarFish Annotator CLI - Command line tool for variant annotation.
- **Core Function**: Annotates variants with functional and clinical information.
- **Input**: VCF file.
- **Output**: Annotated VCF file.
- **Installation**: Install via pip or conda
- **Use Case**: Variant annotation, clinical genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Databases**: Requires annotation databases.

## Examples

### Annotate variants
**Args:** `varfish-annotator-cli annotate --input variants.vcf --output annotated.vcf`
**Explanation:** Annotate variants.

### With options
**Args:** `varfish-annotator-cli annotate --input variants.vcf --output annotated.vcf --threads 8`
**Explanation:** Use 8 threads.
