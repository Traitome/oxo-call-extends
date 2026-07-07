---
name: agtools
category: assembly
description: A software framework to manipulate assembly graphs with support for GFA, FASTG, ASQG, and DOT formats
tags: [agtools, assembly-graph, gfa, fastg, asqg, metagenomics, graph-manipulation]
author: oxo-call-community
source_url: "https://github.com/Vini2/agtools"
---

## Concepts

- **Tool Overview**: agtools is a Python framework for manipulating assembly graphs for downstream metagenomic applications, with primary focus on the Graphical Fragment Assembly (GFA) format.
- **Core Function**: Provides both command-line interface and Python API for loading, querying, analyzing, and manipulating assembly graphs from popular genome and metagenome assemblers.
- **Graph Classes**: Two main classes - UnitigGraph (for GFA files) and ContigGraph (for assembler-specific contig graphs from SPAdes, MEGAHIT, Flye, myloasm).
- **Supported Formats**: GFA (Graphical Fragment Assembly), FASTG, ASQG, DOT (GraphViz/ABySS).
- **Input/Output**: Input: Assembly graph files in various formats. Output: Converted formats, filtered segments, extracted components, graph statistics.
- **Installation**: Install via bioconda: `conda install -c bioconda agtools` or pip: `pip install agtools`
- **Python Version**: Requires Python >= 3.13

## Pitfalls

- **Memory Usage**: Assembly graphs can be very large (10-100 GB) - segment sequences are not loaded into memory by default for efficiency.
- **Format Differences**: Different assemblers represent graphs differently - use appropriate loader for each assembler.
- **Graph Complexity**: Complex graphs with many nodes and edges may require significant computational resources for analysis.
- **Python Version**: Requires Python >= 3.13 - older Python versions are not supported.

## Examples

### Display help information
**Args:** `agtools --help`
**Explanation:** Shows all available CLI commands and options.

### Convert GFA to FASTG
**Args:** `agtools convert -i assembly.gfa -o assembly.fastg --format fastg`
**Explanation:** Converts assembly graph from GFA format to FASTG format.

### Convert GFA to DOT for visualization
**Args:** `agtools convert -i assembly.gfa -o assembly.dot --format dot`
**Explanation:** Converts GFA to DOT format for visualization with GraphViz.

### Filter segments by length
**Args:** `agtools filter -i assembly.gfa -o filtered.gfa --min-length 1000`
**Explanation:** Filters out segments shorter than 1000bp from the assembly graph.

### Extract connected component
**Args:** `agtools extract -i assembly.gfa -o component.gfa --component-id 1`
**Explanation:** Extracts a specific connected component from the assembly graph.

### Calculate graph statistics
**Args:** `agtools stats -i assembly.gfa`
**Explanation:** Calculates and displays statistics about the assembly graph (node count, edge count, N50, etc.).

### Load GFA in Python
**Args:**
```python
from agtools.core.unitig_graph import UnitigGraph

# Load GFA file
ug = UnitigGraph.from_gfa("assembly.gfa")

# Get graph statistics
print(f"Vertices: {ug.vcount}")
print(f"Edges: {ug.ecount}")
print(f"Paths: {ug.pcount}")

# Calculate N50 and L50
n50, l50 = ug.calculate_n50_l50()
print(f"N50: {n50}, L50: {l50}")
```
**Explanation:** Loads a GFA file and calculates basic graph statistics using Python API.

### Get segment sequence
**Args:**
```python
from agtools.core.unitig_graph import UnitigGraph

ug = UnitigGraph.from_gfa("assembly.gfa")

# Get sequence for a specific segment
seq = ug.get_segment_sequence("segment_id")
print(seq)

# Get reverse complement
rc_seq = seq.reverse_complement()
print(rc_seq)
```
**Explanation:** Retrieves the DNA sequence for a specific segment from the assembly graph.

### Query neighbors
**Args:**
```python
from agtools.core.unitig_graph import UnitigGraph

ug = UnitigGraph.from_gfa("assembly.gfa")

# Get neighboring segments
neighbors = ug.get_neighbors("segment_id")
print(f"Neighbors: {neighbors}")
```
**Explanation:** Queries the graph to find neighboring segments of a given segment.

### Check connectivity
**Args:**
```python
from agtools.core.unitig_graph import UnitigGraph

ug = UnitigGraph.from_gfa("assembly.gfa")

# Check if two segments are connected
connected = ug.is_connected("segment1", "segment2")
print(f"Connected: {connected}")

# Get all connected components
components = ug.get_connected_components()
print(f"Number of components: {len(components)}")
```
**Explanation:** Checks connectivity between segments and identifies connected components.

### Load SPAdes contig graph
**Args:**
```python
from agtools.core.contig_graph import ContigGraph

# Load SPAdes assembly graph
cg = ContigGraph.from_spades("assembly_graph.fastg")

# Query contig information
print(f"Contigs: {cg.vcount}")
```
**Explanation:** Loads a SPAdes-specific contig graph using the ContigGraph class.

### Calculate GC content
**Args:**
```python
from agtools.core.unitig_graph import UnitigGraph

ug = UnitigGraph.from_gfa("assembly.gfa")

# Calculate GC content for all segments
gc_content = ug.get_gc_content()
print(f"Average GC content: {gc_content}")
```
**Explanation:** Calculates the GC content of segment sequences in the assembly graph.