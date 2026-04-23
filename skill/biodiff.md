---
name: biodiff
category: variant-calling
description: Exact comparison of biological sequences
tags: [sequence-comparison, variant-calling, diff]
author: oxo-call-community
source_url: "https://gitlab.com/LPCDRP/biodiff"
---

## Concepts
- **Tool Overview**: biodiff is a variant caller that determines exact differences between two biological sequences (DNA or protein) in FASTA format.
- **Exact Comparison**: Finds all sequence differences without statistical modeling, suitable for comparing assemblies or validating mutations.
- **Output Format**: VCF format showing all variants between reference and query sequences.
- **Applications**: Assembly comparison, mutation validation, sequence quality control.

## Pitfalls
- **Sequence Matching**: Sequences to compare should have matching headers (up to first whitespace), or be single-sequence files.
- **Coordinate System**: Output uses 1-based coordinates in VCF format.

## Examples
### Compare two sequences
**Args:** `biodiff reference.fa query.fa > variants.vcf`
**Explanation:** Finds all differences between reference and query sequences.

### Compare protein sequences
**Args:** `biodiff --protein ref_protein.fa query_protein.fa > protein_variants.vcf`
**Explanation:** Compares protein sequences and reports amino acid differences.
