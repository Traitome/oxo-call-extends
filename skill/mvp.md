---
name: mvp
category: annotation
description: detect creation/destruction of sequence motifs as a result of mutations
tags: [mvp, annotation, motif, mutation, variant]
author: oxo-call-community
source_url: "https://gitlab.com/LPCDRP/motif-variants"
---

## Concepts

- **Tool Overview**: mvp (motif-variant probe) v0.4.3 - detects creation/destruction of sequence motifs resulting from mutations.
- **Core Function**: Identifies variants that change the number of occurrences of specified motifs in nucleotide or amino acid sequences.
- **Input/Output**: Takes VCF variants, reference sequence, and motif definitions; outputs variants affecting motif occurrences.
- **Installation**: `conda install -c bioconda mvp`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Requires VCF, reference sequence, and motif definitions.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-v variants.vcf -r reference.fasta -m motifs.txt -o results.tsv`
**Explanation:** Identifies variants that create or destroy sequence motifs.
