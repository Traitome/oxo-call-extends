---
name: blastalign
category: alignment
description: Align nucleotide sequences with large indels using NCBI BLAST
tags: [blastalign, alignment, msa, indel, blast]
author: oxo-call-community
source_url: "http://evolve.zoo.ox.ac.uk/Evolve/Blastalign.html"
---

## Concepts

- **Tool Overview**: BlastAlign uses NCBI BLAST to align nucleotide sequences with large indels.
- **Core Function**: Aligns sequences that are difficult to align globally due to large insertions/deletions.
- **Input**: FASTA file with nucleotide sequences.
- **Output**: Multiple sequence alignment in FASTA format.
- **Advantage**: Handles large indels better than standard MSA tools.
- **Installation**: Install via bioconda: `conda install -c bioconda blastalign`

## Pitfalls

- **BLAST Required**: Requires NCBI BLAST to be installed and in PATH.
- **Sequence Divergence**: Very divergent sequences may produce poor alignments.
- **Output Format**: Output is FASTA alignment; convert for phylogenetic software.
- **Speed**: Slower than standard MSA tools due to BLAST-based approach.

## Examples

### Align sequences
**Args:** `blastalign sequences.fa > aligned.fa`
**Explanation:** Aligns sequences with large indels using BLAST-based approach.

### Specify output file
**Args:** `blastalign sequences.fa -o aligned.fa`
**Explanation:** Writes alignment to specified output file.

### Adjust gap parameters
**Args:** `blastalign sequences.fa -g 5 > aligned.fa`
**Explanation:** Uses custom gap penalty for alignment.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
