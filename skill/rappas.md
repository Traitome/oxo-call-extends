---
name: rappas
category: alignment
description: RAPPAS (Rapid Alignment-free Phylogenetic PLacement via Ancestral Sequences) is a program dedicated to Phylogenetic Placement of (meta)genomic reads on a reference tree. As apposed to previous PP programs, RAPPAS is based on the phylo-kmers idea, detailed in tis manuscript and uses a 2 step approach divided into a) the database build, and b) the placement itself. The main advantage of RAPPAS is that it is alignment free, which means that after step (a) (the DB build) is performed, metagenomic reads can be directly placed on a referene tree WITHOUT aligning them to the reference alignment on which the tree was built (as required by other approaches). The second advantage of RAPPAS is its algorithm based on phylo-kmers matches, making its execution time linear with respect to the length of the placed sequences.
tags: ["rappas", "alignment"]
author: oxo-call-community
source_url: "https://github.com/blinard-BIOINFO/RAPPAS"
---

## Concepts

- **Tool Overview**: RAPPAS (Rapid Alignment-free Phylogenetic PLacement via Ancestral Sequences) is a program dedicated to Phylogenetic Placement of (meta)genomic reads on a reference tree. As apposed to previous PP programs, RAPPAS is based on the phylo-kmers idea, detailed in tis manuscript and uses a 2 step approach divided into a) the database build, and b) the placement itself. The main advantage of RAPPAS is that it is alignment free, which means that after step (a) (the DB build) is performed, metagenomic reads can be directly placed on a referene tree WITHOUT aligning them to the reference alignment on which the tree was built (as required by other approaches). The second advantage of RAPPAS is its algorithm based on phylo-kmers matches, making its execution time linear with respect to the length of the placed sequences. (version 1.22)
- **Core Function**: Processes bioinformatics data related to alignment
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rappas`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic alignment
**Args:** `-i input.fastq -r reference.fasta -o output.bam`
**Explanation:** Aligns input reads to reference genome.

