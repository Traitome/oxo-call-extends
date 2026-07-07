---
name: graphmb
category: bioinformatics
description: GraphMB is a metagenomic binner for long-read assemblies that uses graph machine learning algorithms and assembly graph information.
tags: [graphmb, metagenomics, binning, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/MicrobialDarkMatter/GraphMB"
---

## Concepts

- **Metagenomic Binning**: GraphMB bins metagenomic contigs into groups representing individual microbial genomes (MAGs).

- **Graph Machine Learning**: Uses graph neural networks and machine learning to analyze assembly graph structure.

- **Long-Read Support**: Specifically designed for long-read metagenomic assemblies from Oxford Nanopore and PacBio.

- **Assembly Graph Integration**: Leverages assembly graph information to improve binning accuracy.

- **Overlapped Binning**: Allows contigs to belong to multiple bins, reflecting the complexity of metagenomic data.

- **Quality Assessment**: Provides metrics for evaluating bin quality including completeness and contamination.

## Pitfalls

- **Assembly Quality**: Results depend on the quality of the input assembly. Poor assemblies will produce poor bins.

- **Graph Complexity**: Highly fragmented or complex assembly graphs can reduce binning accuracy.

- **Computational Resources**: Processing large metagenomic datasets may require significant memory and GPU resources.

- **Training Data**: Machine learning models require appropriate training data. Limited training data may affect performance.

- **Parameter Tuning**: Adjust parameters based on dataset characteristics and desired binning stringency.

## Examples

### Basic binning
**Args:** `graphmb -c contigs.fasta -g assembly.gfa -o bins/`
**Explanation:** Performs metagenomic binning using assembly graph information.

### Include coverage information
**Args:** `graphmb -c contigs.fasta -g assembly.gfa -cov coverage.txt -o bins/`
**Explanation:** Incorporates coverage information for improved binning.

### Enable overlapped binning
**Args:** `graphmb -c contigs.fasta -g assembly.gfa -o bins/ --overlap`
**Explanation:** Allows contigs to belong to multiple bins.

### Use GPU acceleration
**Args:** `graphmb -c contigs.fasta -g assembly.gfa -o bins/ --gpu`
**Explanation:** Uses GPU for accelerated computation.

### Generate bin quality report
**Args:** `graphmb -c contigs.fasta -b bins/ -q -o quality.txt`
**Explanation:** Generates quality metrics for each bin.

### Batch processing
**Args:** `graphmb batch -d samples/ -o results/`
**Explanation:** Processes multiple metagenomic samples in a directory.

### Adjust binning sensitivity
**Args:** `graphmb -c contigs.fasta -g assembly.gfa -s 0.8 -o bins/`
**Explanation:** Sets sensitivity threshold for bin assignment.