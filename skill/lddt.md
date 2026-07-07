---
name: lddt
category: structure
description: Local Distance Difference Test - evaluates model quality without superposition
tags: [lddt, structure, protein-structure, quality-assessment, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/swissmodel/lddt"
---

## Concepts

- **Superposition-free**: Evaluates model quality without structural superposition
- **Local Distance**: Focuses on local distance differences
- **Structure Quality**: Assesses protein structure model quality
- **Per-residue Score**: Provides per-residue quality scores
- **Reference Comparison**: Compares model against reference structure
- **Multiple Cutoffs**: Uses multiple distance cutoffs for evaluation

## Pitfalls

- **Reference Required**: Needs reference structure for comparison
- **Resolution Limits**: Performance depends on reference resolution
- **Sequence Identity**: Low identity affects score interpretation
- **Disordered Regions**: Disordered regions may give low scores
- **Model Completeness**: Incomplete models affect scoring
- **Missing Residues**: Missing residues affect local scores

## Examples

### Calculate LDDT score
**Args:** `lddt -m model.pdb -r reference.pdb -o score.txt`
**Explanation:** Computes LDDT score for model vs reference.

### Per-residue output
**Args:** `lddt -m model.pdb -r reference.pdb --per-residue -o scores.txt`
**Explanation:** Outputs per-residue LDDT scores.

### Multiple cutoffs
**Args:** `lddt -m model.pdb -r reference.pdb --cutoffs 1,2,4,8 -o score.txt`
**Explanation:** Uses custom distance cutoffs.

### Batch processing
**Args:** `lddt batch -d models/ -r reference.pdb -o results/`
**Explanation:** Processes multiple model files.

### Generate plot
**Args:** `lddt -m model.pdb -r reference.pdb --plot -o plot.png`
**Explanation:** Creates quality plot.

### JSON output
**Args:** `lddt -m model.pdb -r reference.pdb --json -o score.json`
**Explanation:** Outputs results in JSON format.