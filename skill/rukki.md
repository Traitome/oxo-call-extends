---
name: rukki
category: assembly
description: Extracting paths from assembly graphs.
tags: ["rukki", "assembly", "graph", "path", "bioinformatics"]
author: oxo-call-community
source_url: "https://github.com/marbl/rukki/blob/v0.3.0/README.md"
---

## Concepts

- **Tool Overview**: rukki (v0.3.0) is a bioinformatics tool for extracting paths from assembly graphs. It analyzes de Bruijn graphs or overlap graphs generated during genome assembly to identify valid paths and potential contig sequences.
- **Core Function**: Takes assembly graph files and extracts linear paths representing potential contigs or scaffolds. Supports various graph formats and path finding algorithms.
- **Algorithm**: Implements graph traversal algorithms to find valid paths through assembly graphs, considering coverage, edge weights, and graph topology.
- **Input Format**: Assembly graph files in GFA (Graphical Fragment Assembly) format or custom graph formats from assemblers like SPAdes.
- **Output Format**: FASTA files with extracted contig sequences, path information in JSON/TSV format, and visualization of graph paths.
- **Use Case**: Post-processing assembly graphs, extracting alternative contig paths, resolving assembly ambiguities, improving draft genome quality.

## Pitfalls

- **Graph complexity**: Complex assembly graphs with many branches can lead to excessive path extraction.
- **Memory requirements**: Large graphs require significant memory for processing.
- **Graph format compatibility**: May not support all assembly graph formats.
- **Path selection**: Default parameters may not select optimal paths; requires tuning.
- **Ambiguity resolution**: Cannot resolve all graph ambiguities automatically.
- **Assembly quality**: Dependent on input graph quality; poor assemblies yield poor results.

## Examples

### Extract paths from graph
**Args:** `rukki -i assembly.gfa -o contigs.fasta`
**Explanation:** `-i` input assembly graph in GFA format; `-o` output FASTA with extracted contigs.

### Specify minimum path length
**Args:** `rukki -i assembly.gfa -o contigs.fasta -m 1000`
**Explanation:** `-m` minimum path length in base pairs. Filters out short paths.

### Include alternative paths
**Args:** `rukki -i assembly.gfa -o contigs.fasta -a`
**Explanation:** `-a` extracts alternative paths in addition to primary paths.

### Output path information
**Args:** `rukki -i assembly.gfa -o contigs.fasta -p paths.tsv`
**Explanation:** `-p` outputs path information (node IDs, lengths) to TSV file.

### Visualize paths
**Args:** `rukki -i assembly.gfa -o contigs.fasta -v path_visualization.png`
**Explanation:** `-v` generates visualization of extracted paths in graph.

### Threaded processing
**Args:** `rukki -i assembly.gfa -o contigs.fasta -t 8`
**Explanation:** `-t` number of threads for parallel processing.

### Filter by coverage
**Args:** `rukki -i assembly.gfa -o contigs.fasta -c 10`
**Explanation:** `-c` minimum coverage threshold for path selection.
