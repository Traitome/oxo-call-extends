---
name: seqan_tcoffee
category: alignment
description: seqan_tcoffee - Multiple sequence alignment using SeqAn T-Coffee
tags: ["seqan_tcoffee", "alignment", "MSA", "T-Coffee"]
author: oxo-call-community
source_url: "http://www.seqan.de/apps/seqan-t-coffee"
---

## Concepts

- **Tool Overview**: seqan_tcoffee (v1.13.8) performs multiple sequence alignment using SeqAn T-Coffee.
- **Core Function**: Aligns multiple biological sequences using T-Coffee algorithm.
- **Algorithm**: Implements T-Coffee algorithm for progressive alignment.
- **Input/Output**: Accepts FASTA files and produces aligned sequences.
- **Multiple Alignment**: Focuses on aligning multiple sequences simultaneously.
- **Applications**: Phylogenetics, sequence analysis, and comparative genomics.

## Pitfalls

- **Memory Usage**: High memory requirements for large alignments.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Format**: Requires correct FASTA format.
- **Sequence Length**: May have limitations on sequence length.
- **Version Compatibility**: Different versions may have breaking changes.

## Examples

### Align sequences
**Args:** `seqan_tcoffee -i sequences.fasta -o aligned.fasta`
**Explanation:** `-i` input FASTA; `-o` output aligned FASTA.

### With guide tree
**Args:** `seqan_tcoffee -i sequences.fasta -t tree.nw -o aligned.fasta`
**Explanation:** `-t` specifies guide tree.

### Verbose logging
**Args:** `seqan_tcoffee -i sequences.fasta -v -o aligned.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `seqan_tcoffee -i sequences.fasta -p 8 -o aligned.fasta`
**Explanation:** `-p 8` uses 8 threads for parallel processing.

### Help command
**Args:** `seqan_tcoffee --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqan_tcoffee --version`
**Explanation:** Shows current version.

### Output format
**Args:** `seqan_tcoffee -i sequences.fasta -f phylip -o aligned.phy`
**Explanation:** `-f phylip` outputs in PHYLIP format.