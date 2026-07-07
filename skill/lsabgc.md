---
name: lsabgc
category: utility
description: lsaBGC-Pan - refined workflow for pan-BGC-omic evolutionary investigations.
tags: [lsabgc, utility, BGC, genomics]
author: oxo-call-community
source_url: "https://github.com/Kalan-Lab/lsaBGC-Pan"
---

## Concepts

- **Tool Overview**: lsabgc v1.1.10 is a workflow for pan-BGC (Biosynthetic Gene Cluster) evolutionary analysis.
- **Core Function**: Analyzes and compares biosynthetic gene clusters across multiple genomes to understand their evolution.
- **BGC Analysis**: Identifies, annotates, and compares gene clusters involved in secondary metabolite production.
- **Input/Output**: Input: Genomic sequences, annotation files; Output: BGC comparisons, phylogenetic trees, evolutionary metrics.
- **Installation**: `conda install -c bioconda lsabgc`
- **Key Features**: Integrates with antiSMASH for BGC prediction, supports comparative genomics, generates visualizations.

## Pitfalls

- **Genome Quality**: Requires high-quality genome assemblies for accurate BGC identification.
- **Annotation Quality**: Depends on gene prediction accuracy; poor annotations affect results.
- **Computation Time**: Analyzing many genomes can be computationally intensive.
- **Memory Requirements**: Large datasets may require significant memory resources.
- **Parameter Tuning**: BGC identification parameters may need adjustment for different organisms.
- **Reference Databases**: Results depend on the quality and completeness of reference BGC databases.

## Examples

### Run pan-BGC analysis
**Args:** `lsabgc-pan -i genomes/ -o results/`
**Explanation:** Runs pan-BGC analysis on genomes in input directory.

### With antiSMASH annotations
**Args:** `lsabgc-pan -i genomes/ -a antismash_results/ -o results/`
**Explanation:** Uses pre-computed antiSMASH annotations for BGC identification.

### Set minimum cluster size
**Args:** `lsabgc-pan -i genomes/ -o results/ -m 5`
**Explanation:** Sets minimum 5 genes per cluster.

### Threads
**Args:** `lsabgc-pan -i genomes/ -o results/ -t 16`
**Explanation:** Uses 16 threads for parallel processing.

### Generate visualization
**Args:** `lsabgc-visualize -i results/ -o plots/`
**Explanation:** Generates visualizations of BGC comparisons.

### Help documentation
**Args:** `lsabgc-pan --help`
**Explanation:** Displays all available options and parameters.