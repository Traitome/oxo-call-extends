---
name: sap
category: alignment
description: Pairwise structure alignment via double dynamic programming
tags: ["sap", "alignment", "protein-structure", "structural-alignment"]
author: oxo-call-community
source_url: "https://github.com/mathbio-nimr-mrc-ac-uk/SAP"
---

## Concepts

- **Tool Overview**: SAP (v1.1.3) performs pairwise protein structure alignment using double dynamic programming to compare 3D structures.
- **Core Function**: Aligns protein structures by comparing Cα/Cβ atom coordinates and calculating structural similarity scores.
- **Algorithm**: Implements nested dynamic programming - outer DP for sequence alignment and inner DP for structural similarity scoring.
- **Scoring**: Combines sequence similarity with structural features including distance matrices and dihedral angles.
- **Output**: Structural alignment with RMSD values and alignment scores for assessing similarity.
- **Applications**: Protein structure comparison, fold recognition, and evolutionary analysis based on 3D structure.

## Pitfalls

- **Computational Cost**: Double dynamic programming is computationally intensive for large proteins.
- **Memory Requirements**: DP matrices require O(n^2) memory for proteins of length n.
- **Structure Quality**: Depends on high-quality PDB structures with resolved coordinates.
- **Sequence Order**: Assumes sequential alignment; may miss non-sequential structural similarities.
- **Parameter Sensitivity**: Gap penalties and scoring weights significantly affect alignment results.
- **Local Optima**: Greedy dynamic programming may find suboptimal alignments.

## Examples

### Basic structure alignment
**Args:** `sap -i1 protein1.pdb -i2 protein2.pdb -o alignment.txt`
**Explanation:** `-i1/-i2` input PDB files; `-o` output alignment file with structural comparison.

### RMSD calculation
**Args:** `sap -i1 protein1.pdb -i2 protein2.pdb --rmsd`
**Explanation:** Computes RMSD between two protein structures after optimal alignment.

### Output alignment format
**Args:** `sap -i1 p1.pdb -i2 p2.pdb -o align.fasta -f fasta`
**Explanation:** `-f fasta` outputs alignment in FASTA format with structural mapping.

### Custom gap penalties
**Args:** `sap -i1 p1.pdb -i2 p2.pdb -g 10 -e 2 -o align.txt`
**Explanation:** `-g 10` gap opening penalty; `-e 2` gap extension penalty.

### Verbose mode
**Args:** `sap -i1 p1.pdb -i2 p2.pdb -v -o align.txt`
**Explanation:** `-v` enables verbose output with detailed scoring information.

### Structure-only alignment
**Args:** `sap -i1 p1.pdb -i2 p2.pdb --structure-only -o align.txt`
**Explanation:** Ignores sequence information and aligns based solely on 3D structure.

### Multiple output formats
**Args:** `sap -i1 p1.pdb -i2 p2.pdb -o align -f all`
**Explanation:** Generates alignment in multiple formats (FASTA, PDB, text).