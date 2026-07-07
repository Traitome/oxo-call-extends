---
name: strawc
category: data-format
description: Straw bound with pybind11 for reading Hi-C data from .hic files.
tags: [strawc, hic-data, bioinformatics, c++]
author: oxo-call-community
source_url: "https://github.com/aidenlab/straw"
---

## Concepts

- **Tool Overview**: strawc (v0.0.2.1) is a C++ library bound with pybind11 for efficiently reading Hi-C contact matrices from .hic files.
- **Core Function**: Provides fast access to Hi-C interaction data stored in .hic format.
- **Algorithm**: Uses optimized file parsing to extract contact matrices at different resolutions.
- **Input/Output**: Input: .hic file with genomic coordinates; Output: Contact matrix data.
- **Applications**: Hi-C data analysis, 3D genome visualization, chromatin interaction studies.
- **Installation**: `conda install -c bioconda strawc` or compile from source.

## Pitfalls

- **File Format**: Requires specific .hic file format; other formats not supported.
- **Resolution Limits**: Very high resolution matrices may require significant memory.
- **Coordinate System**: Requires correct chromosome naming convention.
- **Memory Requirements**: Large matrices require significant memory.
- **Version Compatibility**: Older .hic file versions may not be supported.
- **Chromosome Order**: Requires consistent chromosome ordering in input data.

## Examples

### Display help
**Args:** `strawc --help`
**Explanation:** Shows available options and usage information.

### Extract contact matrix
**Args:** `strawc KR input.hic chr1 chr2 BP 1000000`
**Explanation:** Extract KR-normalized contact matrix for chr1-chr2 at 1MB resolution.

### With different normalization
**Args:** `strawc VC input.hic chr1 chr1 BP 500000`
**Explanation:** Extract VC-normalized matrix for chr1 at 500KB resolution.

### Verbose mode
**Args:** `strawc KR input.hic chr1 chr2 BP 1000000 -v`
**Explanation:** Run with detailed logging for debugging.

### Output to file
**Args:** `strawc KR input.hic chr1 chr2 BP 1000000 > matrix.txt`
**Explanation:** Redirect output to file.

### Full genome extraction
**Args:** `strawc KR input.hic ALL ALL BP 1000000`
**Explanation:** Extract all-by-all contact matrix.

### Specific region
**Args:** `strawc KR input.hic chr1:1-1000000 chr2:1-1000000 BP 10000`
**Explanation:** Extract contact matrix for specific regions.

### Multiple resolutions
**Args:** `strawc KR input.hic chr1 chr1 BP 10000 50000 100000`
**Explanation:** Extract matrices at multiple resolutions.

### Python API usage
**Args:** `python -c "import strawc; result = strawc.straw('KR', 'input.hic', 'chr1', 'chr2', 'BP', 1000000)"`
**Explanation:** Use Python API to extract contact matrix.
