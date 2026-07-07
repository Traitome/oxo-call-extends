---
name: graphbin
category: bioinformatics
description: GraphBin performs refined binning of metagenomic contigs using assembly graphs to improve metagenome-assembled genomes (MAGs).
tags: [graphbin, metagenomics, binning, MAGs, bioinformatics]
author: oxo-call-community
source_url: "https://graphbin.readthedocs.io/"
---

## Concepts

- **Metagenomic Binning**: GraphBin bins metagenomic contigs into groups representing individual microbial genomes (MAGs).

- **Assembly Graph Integration**: Uses assembly graph information to improve binning accuracy by considering contig connectivity and overlap.

- **Refined Binning**: Improves upon initial binning results by leveraging graph structure to reassign contigs.

- **Multiple Binning Methods**: Supports various binning algorithms including CONCOCT, MaxBin2, and MetaBAT2.

- **Visualization**: Generates visualizations of the assembly graph with colored bins for quality assessment.

- **Quality Metrics**: Provides metrics for evaluating bin quality including completeness and contamination.

## Pitfalls

- **Assembly Quality**: Results depend on the quality of the input assembly. Poor assemblies will produce poor bins.

- **Graph Complexity**: Highly fragmented or complex assembly graphs can reduce binning accuracy.

- **Initial Bins**: Requires initial binning results from other tools. Poor initial bins will affect refinement.

- **Computational Resources**: Processing large metagenomic datasets may require significant memory.

- **Parameter Tuning**: Adjust parameters based on dataset characteristics and desired binning stringency.

## Examples

### Basic binning refinement
**Args:** `graphbin -c contigs.fasta -g assembly.gfa -b initial_bins/ -o refined_bins/`
**Explanation:** Refines initial bins using assembly graph information.

### Specify initial binning tool
**Args:** `graphbin -c contigs.fasta -g assembly.gfa -b initial_bins/ -t concoct -o refined_bins/`
**Explanation:** Specifies CONCOCT as the initial binning tool format.

### Include coverage information
**Args:** `graphbin -c contigs.fasta -g assembly.gfa -b initial_bins/ -cov coverage.txt -o refined_bins/`
**Explanation:** Incorporates coverage information for improved binning.

### Generate visualization
**Args:** `graphbin -c contigs.fasta -g assembly.gfa -b bins/ -v -o visualization.png`
**Explanation:** Creates a visualization of bins on the assembly graph.

### Evaluate bin quality
**Args:** `graphbin -c contigs.fasta -b bins/ -e -o quality.txt`
**Explanation:** Evaluates bin quality using CheckM or similar metrics.

### Batch processing
**Args:** `graphbin batch -d samples/ -o results/`
**Explanation:** Processes multiple metagenomic samples in a directory.

### Adjust refinement sensitivity
**Args:** `graphbin -c contigs.fasta -g assembly.gfa -b initial_bins/ -s 0.7 -o refined_bins/`
**Explanation:** Sets sensitivity threshold for contig reassignment.