---
name: bcgtree
category: utility
description: BCGtree - Automatized phylogenetic tree building from bacterial core genomes
tags: [phylogenetics, core-genome, bacterial-genomics, tree-building]
author: oxo-call-community
source_url: "https://github.com/molbiodiv/bcgtree"
---

## Concepts

- **Tool Overview**: BCGtree automates phylogenetic tree construction from bacterial core genomes, from alignment to tree visualization.

- **Core Genome Alignment**: Identifies and aligns core genes across multiple bacterial genomes.

- **Automated Pipeline**: Handles entire workflow from genome files to final tree.

- **Tree Building**: Uses standard phylogenetic methods (maximum likelihood, neighbor-joining).

## Pitfalls

- **Annotation Dependency**: Requires gene annotations for core gene identification.

- **Core Definition**: Core genome definition affects results. Adjust parameters as needed.

- **Outgroup Selection**: Proper outgroup selection important for tree rooting.

## Examples

### Basic tree construction
**Args:** `bcgtree --genomes genomes/*.fna --output tree/`
**Explanation:** Builds phylogenetic tree from bacterial genome files.

### Specify outgroup
**Args:** `bcgtree --genomes genomes/*.fna --outgroup outgroup.fna --output tree/`
**Explanation:** Uses specified genome as outgroup for tree rooting.
