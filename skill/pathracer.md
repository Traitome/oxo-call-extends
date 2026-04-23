---
name: pathracer
category: assembly
description: PathRacer is a tool for alignment of profile HMM against assembly graph.
tags: [pathracer, assembly]
author: oxo-call-community
source_url: "http://cab.spbu.ru/software/pathracer/"
---

## Concepts
- **Tool Overview**: PathRacer is a novel standalone tool that aligns profile HMM directly to the assembly graph (performing the codon translation on fly for amino acid pHMMs). The tool provides the set of most probable paths traversed by a HMM through the whole assembly graph, regardless whether the sequence of interested is encoded on the single contig or scattered across the set of edges, therefore significantly improving the recovery of sequences of interest even from fragmented metagenome assemblies.
- **Core Function**: PathRacer is a tool for alignment of profile HMM against assembly graph.
- **Input/Output**: FASTA/BAM/SAM
- **Installation**: `conda install -c bioconda pathracer`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
