---
name: ctc-scite
category: programming
description: CTC-SCITE infers cell lineages from single-cell sequencing data
tags: [ctc-scite, programming, single-cell, lineage-inference, phylogeny, cancer]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/CTC-SCITE"
---

## Concepts

- **Tool Overview**: CTC-SCITE (v1.0.2+) is a software package for inferring cell lineages from single-cell sequencing data, particularly for cancer cells.
- **Core Function**: Reconstructs phylogenetic trees from single-cell variants to infer clonal evolution and cellular relationships.
- **Input/Output**: Input: Variant matrix (cells vs mutations), copy number profiles. Output: Phylogenetic trees, clonal assignments, visualization.
- **Algorithm**: Uses maximum parsimony and probabilistic methods to infer cell lineages from mutation data.
- **Key Features**: Handles both SNV and CNV data, supports single-cell and bulk sequencing integration, provides confidence estimates.
- **Installation**: `conda install -c bioconda ctc-scite`

## Pitfalls

- **Input Format**: Requires specific input format for variant matrices; use provided converters.
- **Mutation Call Quality**: Poor quality variant calls significantly affect lineage inference.
- **Missing Data**: Handle missing calls carefully; imputation may be required.
- **Computational Complexity**: Large datasets may require parallel processing or subset analysis.
- **Tree Interpretation**: Multiple equally parsimonious trees may exist; consider consensus methods.

## Examples

### Infer cell lineage tree
**Args:** `ctc-scite -i variants.txt -o tree.nwk -m 1000`
**Explanation:** Infer cell lineage from variant matrix with 1000 MCMC iterations.

### Run with copy number data
**Args:** `ctc-scite -i variants.txt -c cnv.txt -o tree.nwk --cnv`
**Explanation:** Incorporate copy number data into lineage inference.

### Generate visualization
**Args:** `ctc-scite -i variants.txt -o tree.html --visualize`
**Explanation:** Generate interactive HTML visualization of inferred lineage tree.
