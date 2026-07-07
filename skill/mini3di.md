---
name: mini3di
category: utility
description: A NumPy port of the foldseek code for encoding protein structures to 3di.
tags: [mini3di, utility, protein-structure]
author: oxo-call-community
source_url: "https://github.com/althonos/mini3di"
---

## Concepts

- **Tool Overview**: mini3di v0.2.1 encodes protein structures to 3DI format.
- **Core Function**: Converts protein structures to 3DI encoding.
- **3DI Encoding**: Encodes 3D protein structure information.
- **NumPy Implementation**: Implemented using NumPy for efficiency.
- **Input/Output**: Accepts PDB files; outputs 3DI encodings.
- **Protein Structure Analysis**: Supports protein structure analysis workflows.

## Pitfalls

- **Protein Specific**: Designed for protein structure data.
- **Computational Resources**: Processing large structures may require significant resources.
- **Memory Requirements**: Memory usage can be high for complex structures.
- **Parameter Tuning**: May require parameter adjustment for optimal encoding.
- **Structure Quality**: Results depend on input structure quality.
- **Format Requirements**: Requires PDB format input.

## Examples

### Encode protein structure
**Args:** `mini3di -i protein.pdb -o encoding.txt`
**Explanation:** Encodes protein structure to 3DI format.

### With custom parameters
**Args:** `mini3di -i protein.pdb -o encoding.txt -r 3.5`
**Explanation:** Uses custom radius for encoding.

### Batch processing
**Args:** `mini3di -i pdb/ -o encodings/`
**Explanation:** Processes multiple protein structures.

### Detailed output
**Args:** `mini3di -i protein.pdb -o encoding.txt -v`
**Explanation:** Generates detailed encoding report.

### Visualize encoding
**Args:** `mini3di -i protein.pdb -o encoding.txt -p plot.png`
**Explanation:** Generates visualization of encoding.