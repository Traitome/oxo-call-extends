---
name: apoc
category: structural-bioinformatics
description: APoc (Alignment of Pockets) - Large-scale structural comparison of protein pockets
tags: [apoc, protein-pocket, structural-comparison, ligand-binding, drug-design]
author: oxo-call-community
source_url: "http://cssb.biology.gatech.edu/APoc"
---

## Concepts

- **Tool Overview**: APoc (Alignment of Pockets) v1b16 - A computational method for large-scale, sequence order-independent structural comparison of protein pockets.
- **Core Function**: Compares protein ligand-binding pockets using a scoring function (PS-score) to measure structural similarity, enabling classification of binding sites and prediction of protein function.
- **Pocket Similarity Score (PS-score)**: Measures similarity based on geometry of backbone Cα atoms, side chain orientation, and chemical properties of aligned pocket-lining residues (perfect score = 1).
- **Key Features**:
  - Sequence order-independent alignment
  - Statistical significance estimation using millions of random pocket comparisons
  - Works with experimentally observed or predicted pockets
  - High-performance for large-scale comparisons
- **Applications**: 
  - Classification of ligand-binding sites
  - Prediction of protein molecular function
  - Drug design and discovery
  - Analysis of protein-ligand interactions
- **Installation**: `conda install -c bioconda apoc`

## Pitfalls

- **Structural Input**: Requires 3D protein structures (PDB format) as input
- **Pocket Detection**: May require prior pocket detection using tools like SURFNET, LIGSITE, or CAST
- **Computational Resources**: Large-scale comparisons may require significant computational resources
- **Linux Only**: Primarily designed for Linux environments
- **Version Compatibility**: Limited updates; version b16 is the latest stable release

## Examples

### Compare two protein pockets
**Args:** `apoc -query query_pocket.pdb -target target_pocket.pdb -o comparison_result.txt`
**Explanation:** Compares a query pocket against a target pocket and outputs the PS-score.

### Batch comparison
**Args:** `apoc -query query_pocket.pdb -target_list pocket_list.txt -o batch_results.txt`
**Explanation:** Compares a query pocket against multiple targets listed in a file.

### Large-scale all-against-all comparison
**Args:** `apoc -all -input_dir pockets/ -o all_vs_all_results.txt`
**Explanation:** Performs all-against-all pocket comparisons for all pockets in the input directory.

### Calculate statistical significance
**Args:** `apoc -query query.pdb -target target.pdb -pvalue -o result_with_pvalue.txt`
**Explanation:** Computes the PS-score along with its statistical significance (p-value).

### Help documentation
**Args:** `apoc --help`
**Explanation:** Shows available options and parameters.