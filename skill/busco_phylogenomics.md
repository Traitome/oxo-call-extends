---
name: busco_phylogenomics
category: population-genomics
description: Utility script to construct species phylogenies using BUSCO proteins
tags: [busco, phylogenomics, phylogeny, ortholog]
author: oxo-call-community
source_url: "https://github.com/jamiemcg/BUSCO_phylogenomics"
---

## Concepts

- **Tool Overview**: BUSCO_phylogenomics constructs species phylogenies from BUSCO orthologs.
- **Core Function**: Builds phylogenetic trees using conserved single-copy orthologs.
- **Input**: BUSCO output directories from multiple species.
- **Output**: Multiple sequence alignments and phylogenetic tree.
- **Workflow**: Extract orthologs → align → concatenate → build tree.
- **Installation**: Install via bioconda: `conda install -c bioconda busco_phylogenomics`

## Pitfalls

- **BUSCO Required**: Requires BUSCO results from all species.
- **Ortholog Selection**: Choose appropriate ortholog set for phylogeny.
- **Alignment Quality**: Poor alignments affect tree accuracy.

## Examples

### Build phylogeny from BUSCO results
**Args:** `busco_phylogenomics -i busco_results/ -o phylogeny_output/`
**Explanation:** Constructs species phylogeny from BUSCO ortholog proteins.

### Set alignment method
**Args:** `busco_phylogenomics -i busco_dirs/ --aligner mafft -o phylogeny/`
**Explanation:** Uses MAFFT for multiple sequence alignment.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
