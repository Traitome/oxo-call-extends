---
name: borf
category: annotation
description: ORF predictions from FASTA files
tags: [borf, orf, gene-prediction, annotation]
author: oxo-call-community
source_url: "https://github.com/betsig/borf"
---

## Concepts

- **Tool Overview**: BORF predicts open reading frames (ORFs) from nucleotide sequences.
- **Core Function**: Identifies potential protein-coding regions in DNA sequences.
- **Input**: FASTA file with nucleotide sequences.
- **Output**: ORF coordinates and translated protein sequences.
- **Features**: Supports both strand prediction and minimum length filtering.
- **Installation**: Install via bioconda: `conda install -c bioconda borf`

## Pitfalls

- **Minimum Length**: Short ORFs may be false positives; use length filter.
- **Strand Specificity**: Consider both strands for complete ORF prediction.
- **Start Codons**: Standard ATG start; can include alternative start codons.
- **Stop Codons**: Standard TAA, TAG, TGA stop codons used.

## Examples

### Predict ORFs from sequences
**Args:** `borf sequences.fa -o orfs.gff`
**Explanation:** Predicts all ORFs from input sequences outputting GFF format.

### Set minimum ORF length
**Args:** `borf sequences.fa -m 150 -o orfs.gff`
**Explanation:** Only reports ORFs with minimum 150 nucleotides (50 amino acids).

### Output protein sequences
**Args:** `borf sequences.fa -p orfs_proteins.fa`
**Explanation:** Outputs translated protein sequences from predicted ORFs.

### Predict on both strands
**Args:** `borf sequences.fa --both-strands -o orfs.gff`
**Explanation:** Searches for ORFs on both forward and reverse strands.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
