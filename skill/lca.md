---
name: lca
category: taxonomy
description: Lowest Common Ancestor calculation tool for taxonomic classification
tags: [lca, taxonomy, LCA, taxonomic-classification, metagenomics]
author: oxo-call-community
source_url: "https://github.com/hildebra/LCA"
---

## Concepts

- **LCA Calculation**: Computes lowest common ancestors for taxonomic profiles
- **Taxonomic Classification**: Assigns taxonomy to classified sequences
- **Metagenomics**: Works with metagenomic classification results
- **Tree Traversal**: Traverses taxonomic trees to find LCAs
- **Multiple Hits**: Handles multiple classification hits per read
- **Profile Generation**: Generates taxonomic abundance profiles

## Pitfalls

- **Database Quality**: Classification depends on underlying database
- **Multiple Matches**: Multiple taxonomic hits require resolution
- **Rank Incompleteness**: Missing ranks complicate LCA calculation
- **Threshold Selection**: Confidence thresholds affect classifications
- **Memory Usage**: Large taxonomic trees need memory management
- **Format Compatibility**: Input format requirements

## Examples

### Calculate LCA
**Args:** `LCA -i classifications.txt -o lca_results.txt`
**Explanation:** Calculates LCA for classification results.

### Specify taxonomy
**Args:** `LCA -i classifications.txt -t taxonomy.dmp -o results.txt`
**Explanation:** Uses NCBI taxonomy database.

### Set threshold
**Args:** `LCA -i classifications.txt -c 0.8 -o results.txt`
**Explanation:** Only includes classifications with 80% confidence.

### Generate profile
**Args:** `LCA -i classifications.txt -p -o profile.txt`
**Explanation:** Generates taxonomic abundance profile.

### Batch processing
**Args:** `LCA batch -d classifications/ -o results/`
**Explanation:** Processes multiple classification files.

### Export tree
**Args:** `LCA -i classifications.txt --tree -o tree.nwk`
**Explanation:** Exports taxonomic tree in Newick format.