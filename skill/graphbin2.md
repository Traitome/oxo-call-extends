---
name: graphbin2
category: bioinformatics
description: GraphBin2 performs refined and overlapped binning of metagenomic contigs using assembly graphs for improved metagenome-assembled genomes (MAGs).
tags: [graphbin2, metagenomics, binning, MAGs, bioinformatics]
author: oxo-call-community
source_url: "https://graphbin2.readthedocs.io/"
---

## Concepts

- **Metagenomic Binning**: GraphBin2 bins metagenomic contigs into groups representing individual genomes (MAGs).

- **Assembly Graph Integration**: Uses assembly graph information to improve binning accuracy by considering contig connectivity.

- **Overlapped Binning**: Allows contigs to belong to multiple bins, reflecting the complexity of metagenomic data.

- **Machine Learning**: Uses machine learning models to predict bin membership based on sequence composition and graph features.

- **Refinement**: Refines initial bins using graph-based information to improve MAG quality.

- **Quality Assessment**: Provides metrics for assessing bin quality including completeness and contamination.

## Pitfalls

- **Assembly Quality**: Results depend on the quality of the input assembly. Poor assemblies will produce poor bins.

- **Graph Complexity**: Highly complex assembly graphs can affect binning accuracy.

- **Coverage Variation**: Uneven coverage across contigs can complicate binning. Normalize coverage when possible.

- **Computational Resources**: Processing large metagenomic datasets may require significant memory.

- **Parameter Tuning**: Adjust parameters based on dataset characteristics and desired binning stringency.

## Examples

### Basic binning with assembly graph
**Args:** `graphbin2 -c contigs.fasta -g assembly.gfa -b initial_bins/ -o bins/`
**Explanation:** Performs refined binning using assembly graph information.

### Include coverage information
**Args:** `graphbin2 -c contigs.fasta -g assembly.gfa -b initial_bins/ -cov coverage.txt -o bins/`
**Explanation:** Incorporates coverage information for improved binning.

### Enable overlapped binning
**Args:** `graphbin2 -c contigs.fasta -g assembly.gfa -b initial_bins/ -o bins/ --overlap`
**Explanation:** Allows contigs to belong to multiple bins.

### Adjust binning sensitivity
**Args:** `graphbin2 -c contigs.fasta -g assembly.gfa -b initial_bins/ -s 0.8 -o bins/`
**Explanation:** Sets sensitivity threshold for bin assignment.

### Generate bin quality report
**Args:** `graphbin2 -c contigs.fasta -b bins/ -q -o quality.txt`
**Explanation:** Generates quality metrics for each bin.

### Batch processing
**Args:** `graphbin2 batch -d samples/ -o results/`
**Explanation:** Processes multiple metagenomic samples in a directory.

### Visualize binning results
**Args:** `graphbin2 visualize -g assembly.gfa -b bins/ -o visualization.png`
**Explanation:** Creates a visualization of bins on the assembly graph.