---
name: deepdirect
category: annotation
description: DeepDirect - in silico mutation generation for protein complexes to modify binding affinity.
tags: [deepdirect, annotation, protein-design, binding-affinity, mutations]
author: oxo-call-community
source_url: "https://github.com/Jappy0/deepdirect"
---

## Concepts

- **Tool Overview**: deepdirect (v0.2.5+) is a deep learning-based tool for in silico generation of mutations in protein complexes to increase or decrease binding affinity.
- **Core Function**: Predicts mutations that will either increase or decrease the binding affinity between protein complexes based on structural and sequence information.
- **Input/Output**: Input: Protein structure (PDB), target affinity direction (increase/decrease). Output: Predicted mutations, affinity change predictions, structural analysis.
- **Algorithm**: Uses deep neural networks trained on protein-protein interaction data to predict the effect of mutations on binding affinity.
- **Key Features**: Affinity modulation, bidirectional prediction, structural analysis, supports multiple protein complexes, visualization tools.
- **Installation**: `conda install -c bioconda deepdirect`

## Pitfalls

- **Structure Quality**: Requires high-quality protein structures.
- **Complex Systems**: May struggle with very large protein complexes.
- **Mutation Coverage**: May not cover all possible mutations.
- **Computational Resources**: Requires significant computational resources.
- **Prediction Accuracy**: Predictions may not always match experimental results.

## Examples

### Predict mutations for increased affinity
**Args:** `deepdirect -i complex.pdb -d increase -o mutations.txt`
**Explanation:** Predict mutations that increase binding affinity.

### Predict mutations for decreased affinity
**Args:** `deepdirect -i complex.pdb -d decrease -o mutations.txt`
**Explanation:** Predict mutations that decrease binding affinity.

### With visualization
**Args:** `deepdirect -i complex.pdb -d increase -o mutations.txt --visualize`
**Explanation:** Generate visualization of predicted mutations.