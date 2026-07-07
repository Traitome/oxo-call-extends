---
name: ucsc-pslprottornacoords
category: utility
description: UCSC pslProtToNacords - Tool for converting protein to NA coordinates.
tags: [ucsc-pslprottornacoords, ucsc, psl, protein, coordinates, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslProtToNacords - A tool for converting protein to nucleic acid coordinates.
- **Core Function**: Converts protein coordinates to nucleotide coordinates.
- **Input**: PSL file.
- **Output**: Converted coordinates.
- **Installation**: Part of UCSC utilities
- **Use Case**: Coordinate conversion, protein analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Convert protein to NA coordinates
**Args:** `pslProtToNacords input.psl > output.psl`
**Explanation:** Convert protein coordinates.

### With options
**Args:** `pslProtToNacords -verbose input.psl > output.psl`
**Explanation:** Convert with verbose output.
