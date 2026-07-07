---
name: dampa
category: metagenomics
description: DAMPA - designs probes for targeted metagenomics using pangenome graphs
tags: [dampa, metagenomics, targeted-metagenomics, probes, pangenome]
author: oxo-call-community
source_url: "https://github.com/MultipathogenGenomics/dampa"
---

## Concepts

- **Tool Overview**: dampa (v0.2.0+) designs probes for targeted metagenomics using pangenome graphs to increase speed and accuracy.
- **Core Function**: Generates optimal probe sets for targeted sequencing of pathogen genes from pangenome representations.
- **Input/Output**: Input: Pangenome graph, gene sequences. Output: Probe sequences, coverage statistics.
- **Algorithm**: Uses pangenome graph traversal to identify conserved and variable regions for probe design.
- **Key Features**: Optimized probe design, handles pangenome diversity, high specificity.
- **Installation**: `conda install -c bioconda dampa`

## Pitfalls

- **Graph Quality**: Requires well-constructed pangenome graphs.
- **Probe Specificity**: May need validation against off-target sequences.
- **Genome Diversity**: Performance depends on diversity within pangenome.
- **Probe Length**: Optimal probe length varies by application.
- **Validation**: Designed probes should be validated experimentally.

## Examples

### Design probes from pangenome
**Args:** `dampa design -g pangenome.gfa -o probes.fasta`
**Explanation:** Design probes from pangenome graph for targeted sequencing.

### Specify probe length
**Args:** `dampa design -g graph.gfa -o probes.fasta --length 60`
**Explanation:** Generate 60bp probes from pangenome.

### Optimize for coverage
**Args:** `dampa design -g graph.gfa -o probes.fasta --coverage 95`
**Explanation:** Design probes to achieve 95% gene coverage.
