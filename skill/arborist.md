---
name: arborist
category: utility
description: Arborist - Rank SNV phylogenies inferred from bulk DNA sequencing via scDNA-seq data
tags: [arborist, utility, phylogeny, SNV, scDNA-seq, single-cell]
author: oxo-call-community
source_url: "https://github.com/VanLoo-lab/Arborist"
---

## Concepts

- **Tool Overview**: Arborist is a tool for ranking SNV phylogenies inferred from bulk DNA sequencing data through single-cell DNA sequencing (scDNA-seq) analysis. Version 1.0.0.
- **Core Function**: Compares and ranks phylogenetic trees constructed from somatic mutations, helping identify the most likely evolutionary history of tumor or cell populations.
- **Phylogeny Ranking**: Uses statistical methods to evaluate multiple phylogenetic trees and assign likelihood scores based on compatibility with the observed data.
- **Single-cell Integration**: Bridges bulk sequencing and single-cell resolution for improved phylogenetic reconstruction.
- **Mutation Analysis**: Focuses on single-nucleotide variants (SNVs) for constructing and comparing phylogenies.
- **Installation**: `conda install -c bioconda arborist` or download from GitHub repository.

## Pitfalls

- **Input Data Quality**: Phylogeny ranking accuracy depends on the quality of input SNV calls and sequencing data.
- **Tree Format**: Requires phylogenies in specific formats (Newick, Nexus). Invalid formats cause parsing errors.
- **Computational Complexity**: Ranking many large trees can be computationally intensive.
- **Mutation Calling Dependencies**: Requires high-quality SNV calls from external mutation callers as input.
- **Version Compatibility**: Command-line interface may change between versions.

## Examples

### Display help
**Args:** `arborist --help`
**Explanation:** Shows all available command-line options, subcommands, and usage information.

### Rank phylogenies
**Args:** `arborist rank --trees tree1.newick tree2.newick tree3.newick --output rankings.csv`
**Explanation:** Ranks multiple phylogenetic trees and outputs comparison scores in CSV format.

### Compare two phylogenies
**Args:** `arborist compare --tree1 tree_a.newick --tree2 tree_b.newick --output comparison.txt`
**Explanation:** Compares two phylogenetic trees and generates detailed differences.

### Analyze with mutation data
**Args:** `arborist analyze --input snvs.vcf --trees phylogeny.newick --output results/`
**Explanation:** Combines SNV data with phylogeny for integrated analysis.

### Bootstrap analysis
**Args:** `arborist bootstrap --tree original.newick --replicates 100 --output bootstrap_scores.csv`
**Explanation:** Performs bootstrap resampling to assess tree confidence.

### Export visualization
**Args:** `arborist visualize --tree phylogeny.newick --format pdf --output tree_visualization.pdf`
**Explanation:** Generates PDF visualization of the phylogenetic tree.