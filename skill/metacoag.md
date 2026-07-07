---
name: metacoag
category: assembly
description: "MetaCoAG: Binning Metagenomic Contigs via Composition, Coverage and Assembly Graphs"
tags: [metacoag, assembly, metagenomics, binning, contigs]
author: oxo-call-community
source_url: "https://github.com/metagentools/MetaCoAG"
---
## Concepts

- **Tool Overview**: MetaCoAG v1.2.2 is a metagenomic contig binning tool that leverages connectivity information from assembly graphs for improved binning accuracy.
- **Core Function**: Bins metagenomic contigs by integrating sequence composition, coverage information, and assembly graph connectivity.
- **Graph-based Binning**: Utilizes assembly graph structure to identify contigs belonging to the same genome.
- **Multi-omics Integration**: Combines compositional features (tetranucleotide frequencies) with coverage data across multiple samples.
- **Input/Output**: Accepts assembled contigs in FASTA format and coverage profiles; outputs bins as FASTA files with quality metrics.
- **Reference-free**: Does not require reference genomes for binning.

## Pitfalls

- **Assembly Quality**: Binning accuracy depends on the quality of the input assembly.
- **Graph Complexity**: Complex assembly graphs may affect binning results.
- **Coverage Variation**: Uneven coverage across samples can impact binning accuracy.
- **Memory Requirements**: Processing large assembly graphs may require significant memory.
- **Parameter Sensitivity**: Results may vary with different parameter settings.
- **Contig Length**: Short contigs may be binned less accurately than longer ones.

## Examples

### Run binning with assembly graph
**Args:** `metacoag -i contigs.fasta -g assembly_graph.gfa -o bins/`
**Explanation:** Bins contigs using assembly graph information.

### With coverage information
**Args:** `metacoag -i contigs.fasta -g assembly_graph.gfa -c coverage.txt -o bins/`
**Explanation:** Incorporates coverage data for improved binning.

### Multiple samples
**Args:** `metacoag -i contigs.fasta -g assembly_graph.gfa -c sample1.txt sample2.txt -o bins/`
**Explanation:** Uses coverage from multiple samples for binning.

### Specify minimum contig length
**Args:** `metacoag -i contigs.fasta -g assembly_graph.gfa -m 1000 -o bins/`
**Explanation:** Filters out contigs shorter than 1000 bp.

### Generate bin quality report
**Args:** `metacoag -i contigs.fasta -g assembly_graph.gfa -o bins/ --evaluate`
**Explanation:** Evaluates bin quality and generates a report.