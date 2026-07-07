---
name: sativa
category: taxonomy
description: SATIVA - Semi-Automatic Taxonomy Improvement and Validation Algorithm
tags: ["sativa", "taxonomy", "phylogenetics", "tree-validation"]
author: oxo-call-community
source_url: "https://github.com/amkozlov/sativa"
---

## Concepts

- **Tool Overview**: SATIVA (v0.9.3) is a Semi-Automatic Taxonomy Improvement and Validation Algorithm for phylogenetic tree refinement and taxonomic classification.
- **Core Function**: Validates and improves taxonomic classifications by comparing user-provided trees with reference taxonomies.
- **Algorithm**: Uses maximum likelihood and Bayesian methods to assess tree topology and taxonomic consistency.
- **Input/Output**: Accepts phylogenetic trees in Newick format and produces validated/improved trees with taxonomic annotations.
- **Reference Integration**: Compares input trees against NCBI taxonomy and other reference databases.
- **Applications**: Taxonomic validation, phylogenetic tree improvement, and biodiversity analysis.

## Pitfalls

- **Reference Database Dependencies**: Requires up-to-date reference taxonomy databases.
- **Tree Quality**: Results depend on input tree quality and resolution.
- **Computational Time**: May require significant time for large trees with many taxa.
- **Ambiguity Handling**: May produce ambiguous results for poorly resolved taxa.
- **Memory Requirements**: Large datasets may require substantial memory resources.
- **Expert Interpretation**: Some results may require manual expert review.

## Examples

### Validate taxonomy
**Args:** `sativa -i tree.nwk -o validated_tree.nwk -t ncbi`
**Explanation:** `-i` input Newick tree; `-o` validated output tree; `-t ncbi` uses NCBI taxonomy.

### Compare multiple trees
**Args:** `sativa -i tree1.nwk tree2.nwk -o comparison_report.txt`
**Explanation:** Compares multiple trees and generates comparison report.

### Improve tree topology
**Args:** `sativa -i tree.nwk -r reference.tax -o improved.nwk -m improve`
**Explanation:** `-m improve` activates tree improvement mode using reference taxonomy.

### Generate statistics
**Args:** `sativa -i tree.nwk -o stats.json --stats`
**Explanation:** `--stats` outputs validation statistics in JSON format.

### Interactive mode
**Args:** `sativa -i tree.nwk -i`
**Explanation:** `-i` runs in interactive mode for manual review of taxonomic assignments.

### Custom reference
**Args:** `sativa -i tree.nwk -r custom_taxonomy.tsv -o output.nwk`
**Explanation:** `-r` specifies custom taxonomy file for validation.

### Visualize conflicts
**Args:** `sativa -i tree.nwk -o conflicts.svg --visualize`
**Explanation:** `--visualize` generates visualization of taxonomic conflicts.