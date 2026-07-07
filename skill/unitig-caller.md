---
name: unitig-caller
category: bioinformatics
description: Unitig-Caller - Tool for calling unitigs from assemblies.
tags: [unitig-caller, unitigs, assembly, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/unitig-caller/"
---

## Concepts

- **Tool Overview**: Unitig-Caller - A tool for extracting unitigs from assemblies.
- **Core Function**: Identifies and extracts unitigs from sequence assemblies.
- **Input**: Assembly file (FASTA).
- **Output**: Unitigs file.
- **Installation**: Install via conda or source
- **Use Case**: Assembly analysis, graph-based genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large assemblies.
- **Complexity**: May be slow for highly fragmented assemblies.

## Examples

### Call unitigs
**Args:** `unitig-caller -i assembly.fasta -o unitigs.fasta`
**Explanation:** Extract unitigs from assembly.

### With options
**Args:** `unitig-caller -i assembly.fasta -o unitigs.fasta -min_length 100`
**Explanation:** Set minimum unitig length.
