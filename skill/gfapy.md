---
name: gfapy
category: sequence-format
description: gfapy - Library for handling data in the GFA1 and GFA2 formats.
tags: [gfapy, sequence-format, GFA, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/ggonnella/gfapy"
---

## Concepts
- **GFA Handling**: Handles GFA1 and GFA2 formats.
- **Graph Parsing**: Parses graph data from GFA files.
- **Graph Construction**: Constructs graphs programmatically.
- **Format Conversion**: Converts between GFA versions.
- **Graph Validation**: Validates GFA file integrity.

## Pitfalls
- **Format Compatibility**: Requires correct GFA format.
- **Memory Usage**: Large graphs require significant memory.
- **Version Differences**: GFA1 vs GFA2 differences.
- **Validation**: Requires careful validation.
- **API Changes**: API may change between versions.

## Examples
### Parse GFA file
**Args:** `python -c "import gfapy; g = gfapy.Gfa.from_file('graph.gfa')"`
**Explanation:** Parses GFA file into graph object.

### Create graph
**Args:** `python -c "g = gfapy.Gfa(); g.add_segment('s1', 'ACGT')"`
**Explanation:** Creates GFA graph programmatically.

### Validate graph
**Args:** `python -c "g.validate()"`
**Explanation:** Validates graph integrity.

### Convert format
**Args:** `python -c "g.to_gfa2()"`
**Explanation:** Converts GFA1 to GFA2 format.

### Save graph
**Args:** `python -c "g.to_file('output.gfa')"`
**Explanation:** Saves graph to GFA file.