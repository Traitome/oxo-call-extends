---
name: muscle
category: alignment
description: Multiple sequence and structure alignment with top benchmark scores scalable to thousands of sequences.
tags: [muscle, alignment, multiple-sequence-alignment, msa, protein-alignment, dna-alignment]
author: oxo-call-community
source_url: "https://github.com/rcedgar/muscle"
---

## Concepts

- **Tool Overview**: MUSCLE v5.3 is a multiple sequence alignment (MSA) tool that achieves top benchmark scores while scaling to thousands of sequences. It performs both protein and DNA alignments, with particular strength in protein sequences where it exploits amino acid properties for improved accuracy.
- **Core Function**: Produces fast, accurate multiple sequence alignments using a combination of progressive alignment, tree building (UPGMA or Neighbor-Joining), and iterative refinement strategies. Supports both sequence-only and sequence-plus-structure alignment modes.
- **Algorithm**: Uses log-expectation (LE) scoring derived from profile-profile comparisons, which better captures amino acid substitution patterns than simple identity scoring. Implements three core stages: draft progressive, improved progressive (with tree-dependent refinement), and iterative refinement.
- **Input Format**: Accepts FASTA, ClustalW, MSF, and other common sequence formats. Can handle protein sequences (default) or DNA sequences (use `-d` flag).
- **Output**: Produces alignments in FASTA, ClustalW, EMBL, GCG, JSON, and other formats. Supports output of both alignment and phylogenetic tree.
- **Performance**: Can align thousands of sequences efficiently. Default mode prioritizes speed while maintaining high accuracy. Use `-maxiters` for more refinement iterations at cost of speed.

## Pitfalls

- **Version 5 Syntax Changes**: MUSCLE v5 has different command-line syntax than v3/v4. Many online tutorials refer to old syntax. Check `muscle -help` for current options.
- **Protein vs DNA Mode**: Default mode is protein alignment. For nucleotide sequences, use the `-d` or `-n` flag, otherwise amino acid scoring will be incorrectly applied.
- **Iterative Refinement**: Default is 2 iterations. For difficult alignments (highly divergent or with many indels), increase with `-maxiters`. More iterations improve accuracy but increase runtime.
- **Large Alignments**: Memory usage scales with sequence count and length. For very large sets (10,000+ sequences), consider partitioning or using faster settings.
- **Tree Output**: MUSCLE can output a phylogenetic tree (Newick format) with `-outtree`. The tree is computed from the alignment, not independently.
- **Output Format Matters**: Default output is FASTA. Use `-clw` for ClustalW, `-clwstrict` for strict ClustalW with header, `-html` for HTML output.

## Examples

### Basic protein alignment
**Args:** `-align input.fasta -output aligned.fasta`
**Explanation:** Standard protein multiple sequence alignment. Input sequences are assumed to be proteins. Output in FASTA format (default).

### DNA sequence alignment
**Args:** `-align input.fasta -output dna_aligned.fasta -d`
**Explanation:** Aligns DNA sequences using nucleotide scoring. The `-d` flag specifies DNA mode, which uses appropriate scoring matrices for nucleotides.

### Generate aligned stockholm format
**Args:** `-align input.fasta -output stockholm.sth -stockholm`
**Explanation:** Outputs alignment in Stockholm format, commonly used for Pfam and Rfam domain alignments. Useful for protein family database work.

### Align with more iterations
**Args:** `-align input.fasta -output refined.fasta -maxiters 16`
**Explanation:** Uses 16 iterations of iterative refinement instead of the default 2. Better accuracy for difficult alignments at cost of slower speed.

### Output phylogenetic tree
**Args:** `-align input.fasta -outtree tree.nwk -tree1 tree.nwk`
**Explanation:** Produces both alignment and Newick-format phylogenetic tree. The `-tree1` option outputs a UPGMA tree computed from the alignment.

### Specify iterations and log file
**Args:** `-align input.fasta -output aligned.fasta -log align.log -verbose`
**Explanation:** Creates alignment with verbose logging to a file. Useful for debugging or understanding alignment decisions for large runs.
