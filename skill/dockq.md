---
name: dockq
category: annotation
description: DockQ - Quality measure for evaluating protein, nucleic acid, and ligand docking models.
tags: [dockq, annotation, docking, protein-structure, molecular-modeling, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/bjornwallner/DockQ"
---

## Concepts

- **Tool Overview**: DockQ is a tool for evaluating the quality of protein-ligand, protein-protein, and nucleic acid docking models.
- **Core Function**: Calculates the DockQ score by comparing predicted complex structures against reference structures.
- **Input/Output**: Input: PDB files (predicted model and reference structure). Output: Quality scores and metrics.
- **Algorithm**: Combines multiple structural similarity metrics including RMSD, contact-based measures, and interface quality.
- **Key Features**: Multi-scale scoring, support for various docking types, detailed output reports, benchmarking capabilities.
- **Installation**: `conda install -c bioconda dockq`

## Pitfalls

- **Input Requirements**: Requires properly formatted PDB files with correct chain identifiers.
- **Structure Quality**: Poor quality input structures (missing atoms, incorrect coordinates) affect scoring.
- **Chain Matching**: Must ensure correct chain correspondence between model and reference.
- **Interface Definition**: Different interface definitions can lead to varying scores.
- **Ligand Handling**: Small molecule ligands require specific handling for accurate scoring.
- **Symmetry Issues**: Symmetric complexes may require special consideration.

## Examples

### Basic docking quality assessment
**Args:** `dockq --model predicted.pdb --reference native.pdb`
**Explanation:** Evaluates docking model quality against the native reference structure.

### With chain specification
**Args:** `dockq --model predicted.pdb --reference native.pdb --chain A --target-chain B`
**Explanation:** Specifies which chains to compare in multi-chain complexes.

### Output detailed report
**Args:** `dockq --model predicted.pdb --reference native.pdb --verbose --output report.txt`
**Explanation:** Generates a detailed report with all scoring metrics.

### Evaluate multiple models
**Args:** `dockq --model-dir models/ --reference native.pdb --output scores.txt`
**Explanation:** Batch evaluation of multiple docking models against a single reference.

### Protein-protein docking
**Args:** `dockq --model complex.pdb --reference native.pdb --mode protein-protein`
**Explanation:** Optimized scoring for protein-protein docking evaluation.

### Include ligand scoring
**Args:** `dockq --model predicted.pdb --reference native.pdb --ligand-chain L`
**Explanation:** Includes ligand-specific scoring metrics in the evaluation.