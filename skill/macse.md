---
name: macse
category: alignment
description: MACSE: Multiple Alignment of Coding SEquences Accounting for Frameshifts and Stop Codons.
tags: [macse, alignment]
author: oxo-call-community
source_url: "https://bioweb.supagro.inra.fr/macse/"
---

## Concepts

- **Tool Overview**: macse v2.07 - MACSE aligns coding NT sequences with respect to their AA translation while allowing NT sequences to contain multiple frameshifts and/or stop codons. MACSE is hence the first automatic solution to align protein-coding gene datasets containing non-functional sequences (pseudogenes) without disrupting the underlying codon structure. It has also proved useful in detecting undocumented frameshifts in public database sequences and in aligning next-generation sequencing reads/contigs against a reference coding sequence.
- **Core Function**: MACSE: Multiple Alignment of Coding SEquences Accounting for Frameshifts and Stop Codons.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda macse`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
