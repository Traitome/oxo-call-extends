---
name: gtotree
category: bioinformatics
description: GToTree is a user-friendly workflow for phylogenomics, enabling rapid construction of phylogenetic trees from genomic data.
tags: [gtotree, phylogenomics, tree-construction, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/AstrobioMike/GToTree/wiki"
---

## Concepts

- **Phylogenomics Workflow**: GToTree provides a complete phylogenomics workflow.

- **Tree Construction**: Constructs phylogenetic trees from genomic data.

- **Genome Integration**: Integrates multiple genomes into a single analysis.

- **Marker Genes**: Uses conserved marker genes for tree inference.

- **Alignment**: Performs multiple sequence alignment.

- **Visualization**: Supports tree visualization and annotation.

## Pitfalls

- **Genome Quality**: Results depend on input genome quality.

- **Computational Resources**: Large datasets may require significant resources.

- **Marker Gene Selection**: Choose appropriate marker genes for analysis.

- **Alignment Quality**: Poor alignments affect tree accuracy.

- **Result Interpretation**: Interpret phylogenetic results carefully.

## Examples

### Run complete workflow
**Args:** `GToTree -f genomes/ -o tree/`
**Explanation:** Runs the complete phylogenomics workflow.

### Add reference genomes
**Args:** `GToTree -f genomes/ -r references/ -o tree/`
**Explanation:** Includes reference genomes in analysis.

### Specify marker genes
**Args:** `GToTree -f genomes/ -m markers.txt -o tree/`
**Explanation:** Uses custom marker gene set.

### Generate visualization
**Args:** `GToTree -f genomes/ -o tree/ -p`
**Explanation:** Generates tree visualization.

### Batch processing
**Args:** `GToTree batch -d datasets/ -o results/`
**Explanation:** Processes multiple datasets.

### Check dependencies
**Args:** `GToTree check`
**Explanation:** Verifies required dependencies are installed.

### Help command
**Args:** `GToTree --help`
**Explanation:** Shows available options and usage information.