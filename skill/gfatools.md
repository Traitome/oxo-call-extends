---
name: gfatools
category: sequence-format
description: gfatools - Tools for manipulating sequence graphs in GFA and rGFA formats.
tags: [gfatools, sequence-format, GFA, rGFA, assembly-graphs]
author: oxo-call-community
source_url: "https://github.com/lh3/gfatools/blob/master/README.md"
---

## Concepts
- **GFA Manipulation**: Manipulates GFA format graphs.
- **Graph Construction**: Constructs sequence graphs.
- **Format Conversion**: Converts between formats.
- **Graph Simplification**: Simplifies graph structures.
- **Path Extraction**: Extracts paths from graphs.

## Pitfalls
- **Format Compatibility**: Requires correct GFA format.
- **Graph Complexity**: Complex graphs may affect performance.
- **Memory Usage**: Large graphs require significant memory.
- **Tool Compatibility**: May have compatibility issues.
- **Validation**: Requires graph validation.

## Examples
### Build graph
**Args:** `gfatools gfa build -i contigs.fasta -o graph.gfa`
**Explanation:** Builds GFA graph from contigs.

### Extract path
**Args:** `gfatools gfa path -i graph.gfa -p path_name -o sequence.fasta`
**Explanation:** Extracts sequence from graph path.

### Simplify graph
**Args:** `gfatools gfa simplify -i graph.gfa -o simplified.gfa`
**Explanation:** Simplifies graph structure.

### Convert to FASTA
**Args:** `gfatools gfa to-fasta -i graph.gfa -o sequences.fasta`
**Explanation:** Converts graph to FASTA sequences.

### Validate graph
**Args:** `gfatools gfa validate -i graph.gfa`
**Explanation:** Validates GFA file integrity.