---
name: hla-asm
category: hla-typing
description: HLA-ASM identifies HLA gene exon coordinates in long read-based assemblies and performs HLA typing at G group resolution.
tags: [hla-asm, HLA-typing, long-reads, genome-assembly]
author: oxo-call-community
source_url: "https://github.com/DiltheyLab/HLA-LA"
---

## Concepts

- **HLA Typing**: Determines HLA genotypes from sequencing data.

- **Long Read Analysis**: Optimized for long-read sequencing technologies.

- **Exon Coordinates**: Identifies exon coordinates of HLA genes.

- **G Group Resolution**: Provides HLA typing at G group resolution.

- **Assembly Integration**: Works with genome assembly data.

- **Variant Detection**: Detects HLA-specific genetic variants.

## Pitfalls

- **Assembly Quality**: Results depend on assembly quality.

- **Read Length**: Requires sufficient read length for accurate typing.

- **Reference Database**: Must use appropriate HLA reference database.

- **Computational Resources**: May require significant computational resources.

- **Ambiguity Resolution**: HLA typing may have ambiguities.

## Examples

### Run HLA-ASM on assembly
**Args:** `hla-asm --assembly assembly.fasta --output hla_types.txt`
**Explanation:** Performs HLA typing from long-read assembly.

### With custom reference
**Args:** `hla-asm --assembly assembly.fasta --reference hla_reference.fasta --output hla_types.txt`
**Explanation:** Uses custom HLA reference database.

### High resolution typing
**Args:** `hla-asm --assembly assembly.fasta --high-resolution --output hla_types.txt`
**Explanation:** Performs high-resolution HLA typing.

### Batch processing
**Args:** `for f in *.fasta; do hla-asm --assembly $f --output ${f%.fasta}_hla.txt; done`
**Explanation:** Processes multiple assembly files.

### Generate report
**Args:** `hla-asm --assembly assembly.fasta --output hla_types.txt --report report.html`
**Explanation:** Generates comprehensive HLA typing report.

### With quality filtering
**Args:** `hla-asm --assembly assembly.fasta --min-quality 20 --output hla_types.txt`
**Explanation:** Filters results by quality score.

### Help command
**Args:** `hla-asm --help`
**Explanation:** Shows available options and usage information.