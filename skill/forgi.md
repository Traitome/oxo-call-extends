---
name: forgi
category: programming
description: RNA Graph Library for analyzing and visualizing RNA secondary structures.
tags: [forgi, RNA, secondary structure, graph analysis]
author: oxo-call-community
source_url: "https://viennarna.github.io/forgi/"
---

## Concepts
- **RNA Graph Representation**: Represents RNA secondary structures as graphs.
- **Secondary Structure Parsing**: Parses RNA secondary structures from various formats.
- **Graph Operations**: Supports graph traversal, manipulation, and analysis.
- **Visualization**: Provides tools for visualizing RNA structures.
- **Structure Comparison**: Compares RNA structures based on graph similarity.

## Pitfalls
- **Structure Format**: Requires specific input formats (Dot-Bracket, CT, BPSEQ).
- **Complex Structures**: May struggle with highly complex pseudoknots.
- **Memory Requirements**: Large RNA structures require significant memory.
- **Visualization Limitations**: Very large structures may produce cluttered visualizations.
- **Dependency on ViennaRNA**: Relies on ViennaRNA library for some operations.

## Examples
### Parse RNA structure
**Args:** `forgi parse --input rna.fasta --output structure.dot`
**Explanation:** Parses RNA sequence and predicts secondary structure.

### Visualize RNA structure
**Args:** `forgi visualize --input structure.dot --output rna.png`
**Explanation:** Generates a visualization of the RNA secondary structure.

### Compare structures
**Args:** `forgi compare --input1 struct1.dot --input2 struct2.dot --output similarity.txt`
**Explanation:** Compares two RNA structures and computes similarity score.

### Extract substructures
**Args:** `forgi extract --input structure.dot --region 1-50 --output substruct.dot`
**Explanation:** Extracts a substructure from positions 1-50.

### Convert format
**Args:** `forgi convert --input structure.dot --output structure.ct`
**Explanation:** Converts Dot-Bracket format to CT format.