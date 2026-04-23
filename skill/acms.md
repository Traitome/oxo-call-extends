---
name: acms
category: utility
description: Ambivalent Covariance Models extending CMs with multiple consensus structures for RNA analysis
tags: [rna, covariance-model, secondary-structure, cm, ambivalent]
author: oxo-call-community
source_url: "https://bibiserv.cebitec.uni-bielefeld.de/acms"
---

## Concepts

- **Tool Overview**: aCMs (Ambivalent Covariance Models) extend standard Covariance Models with more than one consensus structure for RNA sequence analysis.
- **Core Function**: Builds and uses covariance models that can represent multiple consensus secondary structures, useful for RNAs with structural variability.
- **Input/Output**: Input: RNA sequence alignments with structural annotations. Output: Ambivalent CM models for RNA homology search.
- **Use Case**: Particularly useful for RNA families where different members adopt different secondary structures.
- **Installation**: Install via bioconda: `conda install -c bioconda acms`

## Pitfalls

- **Structure Annotation**: Requires properly annotated structural alignments - missing annotations will limit model quality.
- **Computational Cost**: Building aCMs is more expensive than standard CMs due to multiple structure handling.
- **Infernal Compatibility**: aCMs extend Infernal's CM format but may not be compatible with all Infernal tools.

## Examples

### Display help information
**Args:** `-h`
**Explanation:** Shows available options and commands for aCMs.

### Build ambivalent CM from alignment
**Args:** `build -i alignment.sto -o model.acm`
**Explanation:** Builds an ambivalent covariance model from a structural Stockholm alignment.

### Search with ambivalent CM
**Args:** `search -i model.acm -d genome.fa -o hits.tsv`
**Explanation:** Searches genomic sequence for RNA homologs using the ambivalent CM.

### Calibrate model
**Args:** `calibrate -i model.acm -o calibrated.acm`
**Explanation:** Calibrates the aCM for accurate E-value calculation in searches.

### Convert standard CM to aCM
**Args:** `convert -i standard.cm -o ambivalent.acm`
**Explanation:** Converts a standard Infernal CM to ambivalent format for multi-structure support.
