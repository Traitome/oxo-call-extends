---
name: lightstringgraph
category: assembly
description: LightStringGraphs (LSG) - External memory string graph construction tool
tags: [lightstringgraph, assembly, string-graph, de-novo, external-memory, bioinformatics]
author: oxo-call-community
source_url: "http://lsg.algolab.eu"
---

## Concepts

- **String Graph**: Construction of string graphs for genome assembly
- **External Memory**: Uses external memory for large dataset processing
- **De Novo Assembly**: De novo genome assembly from sequencing reads
- **Graph Construction**: Efficient graph construction algorithms
- **Memory Efficiency**: Designed to handle datasets larger than RAM
- **Overlap Detection**: Detects overlaps between sequencing reads

## Pitfalls

- **Memory Management**: Requires careful memory management
- **Input Format**: Strict format requirements for input files
- **Performance**: May be slow for very large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Complex Regions**: Repeat regions may cause graph complexity issues
- **Disk I/O**: Performance depends on disk speed

## Examples

### Build string graph
**Args:** `lsg build -i reads.fastq -o graph.lsg`
**Explanation:** Builds string graph from sequencing reads.

### Assemble contigs
**Args:** `lsg assemble -i graph.lsg -o contigs.fasta`
**Explanation:** Assembles contigs from string graph.

### Overlap detection
**Args:** `lsg overlap -i reads.fastq -o overlaps.txt`
**Explanation:** Detects overlaps between reads.

### Graph statistics
**Args:** `lsg stats -i graph.lsg -o stats.txt`
**Explanation:** Generates graph statistics.

### Filter graph
**Args:** `lsg filter -i graph.lsg -m 1000 -o filtered.lsg`
**Explanation:** Filters graph by minimum overlap length.

### Merge graphs
**Args:** `lsg merge -i graph1.lsg graph2.lsg -o merged.lsg`
**Explanation:** Merges multiple string graphs.