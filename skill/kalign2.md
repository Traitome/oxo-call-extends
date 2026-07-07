---
name: kalign2
category: alignment
description: Kalign2 - fast and accurate multiple sequence alignment for proteins.
tags: [kalign2, alignment, MSA, protein, sequence]
author: oxo-call-community
source_url: "http://msa.sbc.su.se/cgi-bin/msa.cgi"
---

## Concepts

- **Tool Overview**: kalign2 (v2.04) - A fast multiple sequence alignment algorithm for proteins.
- **Speed**: Optimized for aligning large numbers of sequences.
- **Accuracy**: Provides accurate alignments using profile hidden Markov models.
- **Input Formats**: Supports FASTA, Clustal, and NEXUS formats.
- **Output Formats**: Generates aligned sequences in multiple formats.
- **Scalability**: Handles thousands of sequences efficiently.

## Pitfalls

- **Memory Usage**: Large datasets require significant memory.
- **Time Complexity**: Very large alignments can be time-consuming.
- **Sequence Similarity**: Poor performance on highly divergent sequences.
- **Format Issues**: Strict input format requirements.
- **Version Differences**: Options differ between versions.
- **Protein Focus**: Primarily designed for protein sequences.

## Examples

### Align sequences
**Args:** `kalign -i input.fasta -o aligned.fasta`
**Explanation:** Aligns sequences in FASTA format.

### Output in Clustal format
**Args:** `kalign -i input.fasta -o aligned.clustal -f clustal`
**Explanation:** Outputs alignment in Clustal format.

### Fast mode
**Args:** `kalign -i input.fasta -o aligned.fasta -m fast`
**Explanation:** Uses fast alignment mode.

### Profile alignment
**Args:** `kalign -i input.fasta -p profile.fasta -o aligned.fasta`
**Explanation:** Aligns sequences to existing profile.

### Verbose output
**Args:** `kalign -i input.fasta -o aligned.fasta -v`
**Explanation:** Shows verbose output with alignment statistics.

### Set gap penalty
**Args:** `kalign -i input.fasta -o aligned.fasta -g 10`
**Explanation:** Sets gap opening penalty to 10.