---
name: hicmatrix
category: bioinformatics
description: HiCMatrix is a library to manage Hi-C matrices for HiCExplorer and pyGenomeTracks.
tags: [hicmatrix, Hi-C, matrix, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/deeptools/HiCMatrix"
---

## Concepts

- **Hi-C Matrices**: HiCMatrix manages Hi-C contact matrices.

- **Data Storage**: Provides efficient storage for Hi-C data.

- **Matrix Operations**: Supports various matrix operations.

- **Format Support**: Supports multiple Hi-C formats.

- **Data Compression**: Handles compressed Hi-C data.

- **Integration**: Integrates with HiCExplorer and pyGenomeTracks.

## Pitfalls

- **Memory Usage**: Large matrices may require significant memory.

- **Format Compatibility**: Ensure format compatibility.

- **Data Integrity**: Verify data integrity after operations.

- **Performance**: May have performance considerations.

- **Version Compatibility**: Ensure compatibility with dependencies.

## Examples

### Load Hi-C matrix
**Args:** `python -c "from hicmatrix import HiCMatrix; m = HiCMatrix('matrix.cool')"`
**Explanation:** Loads Hi-C matrix from file.

### Save matrix
**Args:** `python -c "from hicmatrix import HiCMatrix; m = HiCMatrix('matrix.cool'); m.save('output.cool')"`
**Explanation:** Saves Hi-C matrix to file.

### Matrix operations
**Args:** `python -c "from hicmatrix import HiCMatrix; m = HiCMatrix('matrix.cool'); m.normalize('KR')"`
**Explanation:** Normalizes Hi-C matrix using KR method.

### Batch processing
**Args:** `for f in *.cool; do python -c "from hicmatrix import HiCMatrix; m = HiCMatrix('$f'); m.save('${f%.cool}_norm.cool')"; done`
**Explanation:** Processes multiple Hi-C matrices.

### Help command
**Args:** `python -c "from hicmatrix import HiCMatrix; help(HiCMatrix)"`
**Explanation:** Shows available methods and usage.