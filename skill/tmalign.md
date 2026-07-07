---
name: tmalign
category: analysis
description: TMalign - Protein structure alignment tool for comparing protein structures.
tags: [tmalign, protein-structure, alignment, structural-biology, pdb]
author: oxo-call-community
source_url: "https://zhanggroup.org/TM-align/"
---

## Concepts

- **Tool Overview**: TMalign - A tool for aligning protein structures and calculating structural similarity.
- **Core Function**: Performs structural alignment of protein structures and calculates TM-score for similarity measurement.
- **Input**: Protein structure files (PDB format).
- **Output**: Structural alignment, TM-score, RMSD, aligned structures.
- **Installation**: Download from official website, compile from source
- **Use Case**: Protein structure comparison, fold recognition, structural genomics.

## Pitfalls

- **Structure Quality**: Alignment quality depends on input structure resolution.
- **Sequence Length**: Works best with structures of similar size.

## Examples

### Align two structures
**Args:** `TMalign protein1.pdb protein2.pdb`
**Explanation:** Align two protein structures and calculate TM-score.

### Output aligned structure
**Args:** `TMalign structure1.pdb structure2.pdb -o aligned.pdb`
**Explanation:** Align structures and output aligned PDB file.
