---
name: dligand2
category: annotation
description: dligand2 - Ligand binding site prediction tool.
tags: [dligand2, annotation, ligand, binding-site, protein, structure]
author: oxo-call-community
source_url: "https://github.com/biopython/dligand2"
---

## Concepts

- **Tool Overview**: dligand2 is a tool for predicting ligand binding sites in protein structures.
- **Core Function**: Identifies potential ligand binding pockets in protein 3D structures.
- **Input/Output**: Input: Protein structures (PDB format). Output: Predicted binding sites with coordinates and scores.
- **Algorithm**: Uses geometric and physicochemical properties to identify potential binding pockets.
- **Key Features**: Binding site prediction, pocket detection, scoring, visualization, multiple structure support.
- **Installation**: `conda install -c bioconda dligand2`

## Pitfalls

- **Input Requirements**: Requires protein structure in PDB format.
- **Structure Quality**: Poor resolution structures affect prediction accuracy.
- **False Positives**: May predict false binding sites in flexible regions.
- **Ligand Specificity**: Prediction is not ligand-specific.
- **Missing Residues**: Incomplete structures affect predictions.

## Examples

### Predict binding sites
**Args:** `dligand2 --input protein.pdb --output binding_sites.tsv`
**Explanation:** Predicts ligand binding sites in protein structure.

### With custom parameters
**Args:** `dligand2 --input protein.pdb --output binding_sites.tsv --min-pocket-size 10`
**Explanation:** Set minimum pocket size threshold.

### Multiple structures
**Args:** `dligand2 --input-dir pdbs/ --output-dir results/`
**Explanation:** Process multiple protein structures in batch.

### Generate visualization
**Args:** `dligand2 --input protein.pdb --output binding_sites.tsv --visualize binding_sites.pdb`
**Explanation:** Generate visualization of predicted binding sites.

### Score only mode
**Args:** `dligand2 --input protein.pdb --output scores.tsv --score-only`
**Explanation:** Only compute binding site scores without detailed output.