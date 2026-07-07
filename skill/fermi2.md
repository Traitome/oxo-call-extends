---
name: fermi2
category: formatting
description: "Fermi2 focuses on the exploration of FMD-index as a graph."
tags: [fermi2, formatting, FM-index, graph, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/lh3/fermi2"
---

## Concepts

- **Tool Overview**: Fermi2 is a tool for exploring FMD-index (FM-index with bidirectional searching) as a graph structure for sequence analysis.
- **Core Function**: Provides graph-based sequence analysis using FMD-index data structures.
- **Input/Output**: Input: Sequence data. Output: Graph representations, analysis results.
- **Algorithm**: Uses FMD-index for efficient graph construction and traversal.
- **Key Features**: FMD-index exploration, graph-based analysis, sequence assembly, variant detection, efficient memory usage.
- **Installation**: `conda install -c bioconda fermi2`

## Pitfalls

- **Memory Usage**: Large graphs may require significant memory.
- **Index Construction**: Building FMD-index can be time-consuming.
- **Graph Complexity**: Complex regions may produce complex graphs.
- **Algorithm Parameters**: Performance depends on parameter settings.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic graph construction
**Args:** `fermi2 graph -i sequences.fasta -o graph.gfa`
**Explanation:** Constructs FMD-index graph from sequences.

### Sequence mapping
**Args:** `fermi2 map -i graph.gfa -q reads.fastq -o mappings.sam`
**Explanation:** Maps reads to graph.

### Variant detection
**Args:** `fermi2 variants -i graph.gfa -r reference.fasta -o variants.vcf`
**Explanation:** Detects variants using graph.

### Graph visualization
**Args:** `fermi2 view -i graph.gfa -o graph.png`
**Explanation:** Visualizes graph structure.

### Assembly
**Args:** `fermi2 assemble -i graph.gfa -o contigs.fasta`
**Explanation:** Assembles contigs from graph.