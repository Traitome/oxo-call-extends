---
name: foldmason
category: alignment
description: Multiple Protein Structure Alignment at Scale with FoldMason.
tags: [foldmason, protein structure, multiple alignment, structural bioinformatics]
author: oxo-call-community
source_url: "https://github.com/steineggerlab/foldmason"
---

## Concepts
- **Multiple Structure Alignment**: Aligns three or more protein structures simultaneously.
- **Structure-Based Phylogeny**: Uses structural similarity to infer evolutionary relationships.
- **Profile-Guided Alignment**: Constructs alignments based on structural profiles rather than just sequences.
- **Scalable Alignment**: Designed to handle hundreds to thousands of structures efficiently.
- **MSA Integration**: Can incorporate sequence-based multiple sequence alignments with structural information.

## Pitfalls
- **Computational Complexity**: Aligning many structures is computationally intensive.
- **Structure Quality**: Poorly resolved structures can reduce alignment accuracy.
- **Homology Requirement**: Requires detectable structural homology between proteins.
- **Memory Usage**: Aligning large datasets requires substantial memory.
- **Output Size**: Full alignments of many structures can produce very large output files.

## Examples
### Align multiple structures
**Args:** `foldmason align struct1.pdb struct2.pdb struct3.pdb -o alignment.sto`
**Explanation:** Aligns three protein structures and outputs in Stockholm format.

### Build structure-based tree
**Args:** `foldmason tree structures/*.pdb -o tree.nwk`
**Explanation:** Constructs a phylogenetic tree based on structural similarity.

### Align with sequence profiles
**Args:** `foldmason align --seq-profile msa.fasta structs/*.pdb -o combined.aln`
**Explanation:** Combines sequence MSA with structural alignment for improved accuracy.

### Large-scale alignment
**Args:** `foldmason align --batch struct_dir/ -o alignments/ --threads 12`
**Explanation:** Batch processes and aligns all structures in a directory using 12 threads.

### Refine existing alignment
**Args:** `foldmason refine input.aln structs/*.pdb -o refined.aln`
**Explanation:** Refines an existing alignment using structural information.