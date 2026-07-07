---
name: ipk
category: phylogenetics
description: Inference of Phylo-K-mers - Efficient computation of phylogenetic k-mers for alignment-free placement.
tags: [ipk, phylogenetics, k-mers, alignment-free, placement]
author: oxo-call-community
source_url: "https://github.com/phylo42/ipk"
---

## Concepts

- **Tool Overview**: IPK (v0.5.1) - A tool for efficient computation of phylo-k-mers for phylogenetic analysis.
- **Core Function**: Generates phylo-k-mer databases from multiple sequence alignments and phylogenetic trees.
- **Alignment-Free**: Enables alignment-free phylogenetic placement using k-mer signatures.
- **Divide-and-Conquer**: Implements divide-and-conquer strategy for improved scalability.
- **Integration**: Works seamlessly with EPIK, SHERPAS, and CLAPPAS tools for downstream analysis.
- **Ancestral Reconstruction**: Uses maximum likelihood ancestral sequence reconstruction.

## Pitfalls

- **Memory Requirements**: Large datasets may require significant memory for database construction.
- **Alignment Quality**: Results depend on the quality of the input multiple sequence alignment.
- **K-mer Selection**: Optimal k-mer size depends on dataset characteristics and may require tuning.
- **Tree Requirements**: Requires a rooted phylogenetic tree for accurate phylo-k-mer computation.
- **Computation Time**: Database construction can be time-consuming for large phylogenies.
- **Binary Compatibility**: Database format may change between versions, requiring re-computation.

## Examples

### Build phylo-k-mer database
**Args:** `ipk build -a alignment.fasta -t tree.newick -o ipk_db/`
**Explanation:** Builds a phylo-k-mer database from a multiple sequence alignment and phylogenetic tree.

### Custom k-mer size
**Args:** `ipk build -a alignment.fasta -t tree.newick -o ipk_db/ -k 21`
**Explanation:** Builds database using k-mer size of 21 (default is typically 31).

### Filter low-scoring k-mers
**Args:** `ipk build -a alignment.fasta -t tree.newick -o ipk_db/ --score-threshold 0.8`
**Explanation:** Filters k-mers to retain only those with score >= 0.8 for improved accuracy.

### Ancestral reconstruction
**Args:** `ipk build -a alignment.fasta -t tree.newick -o ipk_db/ --ancestral-method ml`
**Explanation:** Uses maximum likelihood method for ancestral sequence reconstruction.

### Database statistics
**Args:** `ipk stats -d ipk_db/ -o stats.txt`
**Explanation:** Generates statistics about the phylo-k-mer database including size and composition.

### Validate database
**Args:** `ipk validate -d ipk_db/ -a test_alignment.fasta`
**Explanation:** Validates the constructed database against a test alignment.