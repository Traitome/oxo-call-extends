---
name: usalign
category: alignment
description: USAlign - Universal Structure Alignment tool.
tags: [usalign, structure-alignment, bioinformatics, proteomics]
author: oxo-call-community
source_url: "https://github.com/pylelab/USAlign"
---

## Concepts

- **Tool Overview**: USAlign - A tool for universal protein structure alignment.
- **Core Function**: Aligns protein 3D structures.
- **Input**: Protein structure files (PDB).
- **Output**: Alignment results.
- **Installation**: Install via conda or source
- **Use Case**: Protein structure analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large structures.
- **Structure Quality**: Results depend on input structure quality.

## Examples

### Align structures
**Args:** `usalign -i1 structure1.pdb -i2 structure2.pdb -o alignment.txt`
**Explanation:** Align two protein structures.

### With options
**Args:** `usalign -i1 structure1.pdb -i2 structure2.pdb -o alignment.txt -m tmscore`
**Explanation:** Use TM-score metric.
