---
name: dinamo
category: utility
description: DINAMO - Motif discovery tool for nucleotide sequences.
tags: [dinamo, utility, motif-discovery, nucleotide]
author: oxo-call-community
source_url: "https://github.com/dinamo-motif/dinamo"
---

## Concepts

- **Tool Overview**: dinamo is a motif discovery tool for finding conserved patterns in nucleotide sequences.
- **Core Function**: Discovers over-represented sequence motifs in sets of nucleotide sequences using statistical methods.
- **Input/Output**: Input: Nucleotide FASTA sequences. Output: Discovered motifs with position weight matrices, significance scores.
- **Algorithm**: Uses statistical over-representation analysis to identify conserved sequence patterns.
- **Key Features**: de novo motif discovery, position weight matrix generation, significance testing, visualization, multiple motif detection.
- **Installation**: `conda install -c bioconda dinamo`

## Pitfalls

- **Input Requirements**: Requires nucleotide sequences in FASTA format.
- **Sequence Quality**: Poor quality sequences can affect motif discovery.
- **Motif Length**: Must specify appropriate motif length range.
- **Background Model**: Requires appropriate background sequence for comparison.
- **Multiple Testing**: Can produce many false positive motifs without proper filtering.

## Examples

### Discover motifs in sequences
**Args:** `dinamo --input sequences.fa --output motifs/`
**Explanation:** Discovers sequence motifs in nucleotide data.

### With specific motif length
**Args:** `dinamo --input sequences.fa --output motifs/ --min-length 6 --max-length 20`
**Explanation:** Search for motifs between 6-20 bp in length.

### Use background model
**Args:** `dinamo --input sequences.fa --background background.fa --output motifs/`
**Explanation:** Use background sequences for significance testing.

### Number of motifs
**Args:** `dinamo --input sequences.fa --output motifs/ --num-motifs 10`
**Explanation:** Discover top 10 most significant motifs.

### Generate visualization
**Args:** `dinamo --input sequences.fa --output motifs/ --plot motifs.png`
**Explanation:** Generate visualization of discovered motifs.