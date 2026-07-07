---
name: sapling
category: population-genomics
description: Inferring and Summarizing Tumor Phylogenies from Bulk DNA Data
tags: ["sapling", "population-genomics", "cancer", "phylogeny"]
author: oxo-call-community
source_url: "https://github.com/elkebir-group/Sapling"
---

## Concepts

- **Tool Overview**: Sapling (v1.0.0) is a Python tool for inferring and summarizing tumor phylogenies from bulk DNA sequencing data.
- **Core Function**: Constructs backbone trees that summarize the space of plausible evolutionary histories from noisy bulk sequencing data.
- **Algorithm**: Implements heuristic solutions for Backbone Tree Inference and Expansion problems, both proven NP-hard.
- **Input**: Variant read count matrices from bulk DNA sequencing of multiple tumor samples.
- **Output**: Small set of backbone trees on a subset of mutations representing the solution space.
- **Applications**: Cancer evolution analysis, intra-tumor heterogeneity characterization, and clonal architecture inference.

## Pitfalls

- **Computational Complexity**: NP-hard problems require heuristic solutions with potential optimality trade-offs.
- **Input Quality**: Requires high-quality SNV calls with accurate read counts across multiple samples.
- **Sample Requirements**: Performance degrades with fewer than 5-10 samples per patient.
- **Solver Dependencies**: Requires fastPPM, CVXOPT, or Gurobi for frequency matrix estimation.
- **Memory Usage**: Large mutation matrices may require significant computational resources.
- **Interpretation**: Backbone trees represent summaries and may not capture all evolutionary details.

## Examples

### Infer backbone tree
**Args:** `sapling backbone -i variants.csv -o backbone.tree -l 5`
**Explanation:** `-i` input variant read counts; `-o` output backbone tree; `-l` number of mutations in backbone.

### Expand backbone tree
**Args:** `sapling expand -b backbone.tree -i variants.csv -o full_tree.nwk`
**Explanation:** Expands backbone tree to full tumor phylogeny with all mutations.

### Multiple backbones
**Args:** `sapling backbone -i variants.csv -k 3 -o backbone_`
**Explanation:** `-k 3` generates up to 3 distinct backbone trees summarizing solution space.

### Custom solver
**Args:** `sapling backbone -i variants.csv -s cvxopt -o tree.nwk`
**Explanation:** `-s cvxopt` specifies CVXOPT solver for frequency estimation.

### Verbose output
**Args:** `sapling backbone -i variants.csv -o tree.nwk -v`
**Explanation:** `-v` enables verbose mode showing progress and algorithm details.

### Quality filtering
**Args:** `sapling backbone -i variants.csv -q 0.95 -o tree.nwk`
**Explanation:** `-q 0.95` filters low-quality variants with confidence below 95%.

### Output summary statistics
**Args:** `sapling backbone -i variants.csv -o tree.nwk -r stats.txt`
**Explanation:** `-r` generates summary statistics about the inferred backbone trees.