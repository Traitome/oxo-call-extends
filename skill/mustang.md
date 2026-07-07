---
name: mustang
category: annotation
description: Mustang is a program that implements an algorithm for structural alignment of multiple protein structures.
tags: [mustang, annotation, protein-structure, alignment, structural-alignment, pdb]
author: oxo-call-community
source_url: "https://lcb.infotech.monash.edu.au/mustang"
---

## Concepts

- **Tool Overview**: MUSTANG v3.2.4 is a multiple protein structure alignment tool that aligns protein chains based on their 3D coordinates. It can align multiple protein structures simultaneously, producing structural alignments that reveal evolutionary relationships even when sequence similarity is low.
- **Core Function**: Performs structural alignment of 3 or more protein chains, identifying conserved structural motifs and corresponding residues across the structures. Outputs both the alignment and a superposed structure.
- **Algorithm**: Uses a combination of local structure comparison, pairwise alignment, and progressive multiple alignment strategies. It builds upon pairwise structural alignments to construct a multiple structural alignment.
- **Input Format**: Accepts a list of PDB files (or chains within PDB files) specified in a text file. Each line should contain a PDB ID or filename with optional chain identifier.
- **Output**: Produces superposed PDB structures, a multiple sequence alignment in FASTA or MSF format, and a summary of structurally conserved regions (SCRs).
- **Use Case**: Essential for protein family classification, homology modeling, protein function annotation, and studying evolutionary relationships where sequence alignment fails.

## Pitfalls

- **Input File Format**: MUSTANG expects a specific input format - a file listing PDB identifiers or file paths, not the PDB files themselves. Prepare an input list file first.
- **Chain Specification**: For multi-chain PDBs, specify which chain to use (e.g., `1ABC.A` for chain A of PDB 1ABC). Default may not be the intended chain.
- **Structural Divergence**: Proteins with highly divergent structures (different folds) may produce poor alignments or fail. MUSTANG works best on proteins with detectable structural similarity.
- **Memory for Large Alignments**: Aligning many large structures requires significant memory. For very large sets, consider selecting representative structures.
- **Gap Penalties**: Default gap penalties may not be optimal for all protein families. Consider adjusting if alignment seems unreasonable.
- **Output Interpretation**: The superposed PDB output shows structural superposition but may have large RMSD values if structures are truly divergent.

## Examples

### Basic multiple structure alignment
**Args:** `-i structures.list -o aligned.pdb`
**Explanation:** Aligns all structures listed in structures.list file. The list should contain one PDB ID or filename per line.

### Specify output format
**Args:** `-i structures.list -o alignment.fasta -f fasta`
**Explanation:** Outputs multiple sequence alignment in FASTA format instead of superposed PDB coordinates. Useful for downstream phylogenetic analysis.

### Include all chains from PDB files
**Args:** `-i pdblist.txt -o results/ -s`
**Explanation:** The `-s` flag processes all chains in each PDB file. Without it, only the first chain is used.

### Set scoring parameters
**Args:** `-i structures.list -o aligned.pdb -gp -3.0 -ge -0.5`
**Explanation:** Sets gap penalty start (`-gp`) and extension (`-ge`) values. More negative values allow more gaps in the alignment.

### Run with verbose output
**Args:** `-i structures.list -o aligned.pdb -v`
**Explanation:** Verbose mode prints detailed progress information including pairwise alignments being computed and scoring updates.
