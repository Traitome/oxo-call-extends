---
name: dnapi
category: utility
description: DNApi - DNA primer design tool.
tags: [dnapi, utility, primer-design, pcr, dna]
author: oxo-call-community
source_url: "https://github.com/kblin/dnaprimer"
---

## Concepts

- **Tool Overview**: DNApi is a tool for designing PCR primers.
- **Core Function**: Designs optimal primers for PCR amplification with various constraints.
- **Input/Output**: Input: Target sequences (FASTA), optional reference genome. Output: Primer designs with properties.
- **Algorithm**: Uses thermodynamic calculations and specificity checks for primer design.
- **Key Features**: Primer design, specificity checking, Tm calculation, multiplex primer design, batch processing.
- **Installation**: `conda install -c bioconda dnapi`

## Pitfalls

- **Input Requirements**: Requires target DNA sequences.
- **Tm Calculation**: Primer melting temperature depends on salt concentration.
- **Specificity**: Poor specificity can lead to non-specific amplification.
- **Primer Dimer**: Must check for primer-primer interactions.
- **GC Content**: Extreme GC content can affect PCR efficiency.

## Examples

### Design PCR primers
**Args:** `dnapi design --input target.fa --output primers.tsv`
**Explanation:** Designs PCR primers for target sequences.

### With specificity check
**Args:** `dnapi design --input target.fa --reference ref.fa --output primers.tsv`
**Explanation:** Check primer specificity against reference genome.

### Custom Tm range
**Args:** `dnapi design --input target.fa --output primers.tsv --tm-range 55-65`
**Explanation:** Design primers with specific melting temperature range.

### Multiplex primers
**Args:** `dnapi design --input targets.fa --output primers.tsv --multiplex`
**Explanation:** Design primers for multiplex PCR.

### Batch primer design
**Args:** `dnapi design --input-dir targets/ --output-dir primers/`
**Explanation:** Design primers for multiple target files.