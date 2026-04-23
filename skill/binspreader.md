---
name: binspreader
category: metagenomics
description: Improve existing binning using assembly graph and connectivity information
tags: [mag, binning-refinement, assembly-graph, hi-c]
author: oxo-call-community
source_url: "https://cab.spbu.ru/software/binspreader/"
---

## Concepts
- **Tool Overview**: BinSPreader refines metagenome-assembled genomes (MAGs) by exploiting assembly graph topology and connectivity information (paired-end reads, Hi-C contacts).
- **Graph-Based Refinement**: Uses assembly graph structure to propagate binning from well-binned contigs to poorly-binned ones.
- **Connectivity Sources**: Leverages paired-end read links and Hi-C contacts to connect contigs.
- **Capabilities**: Corrects binning errors, propagates binning to shorter contigs, and identifies contigs belonging to multiple bins (strain variation).

## Pitfalls
- **Input Requirements**: Requires assembly graph (GFA format) and existing binning results.
- **Connectivity Data**: Quality of refinement depends on availability and quality of connectivity data.
- **Strain Resolution**: May identify multi-bin contigs but cannot fully resolve strain mixtures.

## Examples
### Refine binning with paired-end data
**Args:** `binspreader --graph assembly.gfa --bins initial_bins.tsv --pe-reads reads.bam --output refined_bins.tsv`
**Explanation:** Refines bins using assembly graph and paired-end read connectivity.

### Refine with Hi-C data
**Args:** `binspreader --graph assembly.gfa --bins bins.tsv --hic-reads hic.bam --output refined.tsv`
**Explanation:** Uses Hi-C contacts for bin refinement.
