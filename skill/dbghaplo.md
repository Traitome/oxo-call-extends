---
name: dbghaplo
category: variant-calling
description: Haplotyping small sequences from heterogeneous long-read sequencing samples using SNP-encoded positional de Bruijn Graph.
tags: [dbghaplo, variant-calling, haplotyping, long-reads, de-Bruijn-graph]
author: oxo-call-community
source_url: "https://github.com/bluenote-1577/dbghaplo"
---

## Concepts

- **Tool Overview**: dbghaplo (v0.0.2+) is a tool for reconstructing haplotypes from heterogeneous samples using long-read sequencing data. It uses a SNP-encoded positional de Bruijn graph approach.
- **Core Function**: Reconstructs individual haplotypes from mixed samples (e.g., viral quasispecies, bacterial strains) by building a positional de Bruijn graph encoded with SNP information.
- **Input/Output**: Input: Aligned BAM/SAM files, reference FASTA. Output: Reconstructed haplotype sequences, variant calls, abundance estimates.
- **Algorithm**: Constructs a positional de Bruijn graph where nodes represent SNP-encoded k-mers, then traverses the graph to reconstruct haplotypes.
- **Key Features**: Handles heterogeneous samples, uses long-read information, provides haplotype abundance estimates, supports viral quasispecies reconstruction.
- **Installation**: `conda install -c bioconda dbghaplo`

## Pitfalls

- **Read Coverage**: Requires sufficient coverage for each haplotype.
- **SNP Density**: Performance depends on appropriate SNP density.
- **Graph Complexity**: Complex graphs may be difficult to resolve.
- **Long Read Errors**: Noisy long reads may introduce errors in haplotypes.
- **Parameter Selection**: K-mer size and SNP thresholds affect results.

## Examples

### Reconstruct haplotypes
**Args:** `dbghaplo -i aligned.bam -r reference.fasta -o haplotypes.fasta`
**Explanation:** Reconstruct haplotypes from aligned long reads.

### Adjust k-mer size
**Args:** `dbghaplo -i aligned.bam -r reference.fasta -k 25 -o haplotypes.fasta`
**Explanation:** Use k-mer size 25 for positional de Bruijn graph construction.

### Output abundance estimates
**Args:** `dbghaplo -i aligned.bam -r reference.fasta -o haplotypes.fasta --abundance abundances.tsv`
**Explanation:** Reconstruct haplotypes and estimate their relative abundances.