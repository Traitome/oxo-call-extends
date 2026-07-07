---
name: metacluster
category: alignment
description: MetaCluster5.1 is a new software for binning short pair-end reads
tags: [metacluster, alignment, metagenomics, binning, reads]
author: oxo-call-community
source_url: "http://i.cs.hku.hk/~alse/MetaCluster/"
---

## Concepts

- **Tool Overview**: MetaCluster v5.1 is an unsupervised binning method designed for binning short paired-end reads from metagenomic samples.
- **Core Function**: Groups sequencing reads into bins based on sequence composition and coverage patterns without requiring reference genomes.
- **Low-abundance Detection**: Specifically designed to handle samples with low-abundance species and many extremely-low-abundance species.
- **Paired-end Support**: Optimized for paired-end sequencing data where odd-numbered reads and their next read are treated as pairs.
- **Input/Output**: Accepts FASTA-formatted paired-end reads; outputs read bins with taxonomic assignments when possible.
- **Unsupervised Learning**: Uses machine learning algorithms to automatically group reads without prior knowledge.

## Pitfalls

- **Input Format**: Requires specific input format where paired reads are consecutive in the file.
- **Read Length**: Performance may vary with different read lengths.
- **Complex Communities**: May struggle with highly complex metagenomic communities.
- **Computational Resources**: Memory usage can be high for large datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal binning results.
- **Contamination**: Cross-contamination between bins can occur with closely related species.

## Examples

### Run binning on paired-end reads
**Args:** `MetaCluster -i reads.fasta -o bins/`
**Explanation:** Bins paired-end reads from input FASTA file.

### Specify k-mer size
**Args:** `MetaCluster -i reads.fasta -k 25 -o bins/`
**Explanation:** Uses k-mer size of 25 for binning.

### With coverage information
**Args:** `MetaCluster -i reads.fasta -c coverage.txt -o bins/`
**Explanation:** Incorporates coverage information for improved binning.

### Output bin statistics
**Args:** `MetaCluster -i reads.fasta -o bins/ -s`
**Explanation:** Generates statistics for each bin.

### Run in parallel mode
**Args:** `MetaCluster -i reads.fasta -o bins/ -p 8`
**Explanation:** Uses 8 threads for parallel processing.