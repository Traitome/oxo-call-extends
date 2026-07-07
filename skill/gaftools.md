---
name: gaftools
category: alignment
description: Fast and comprehensive toolkit for processing pangenome alignments in GAF format.
tags: [gaftools, pangenome, GAF, sequence alignment]
author: oxo-call-community
source_url: "https://github.com/marschall-lab/gaftools"
---

## Concepts
- **GAF Processing**: Comprehensive GAF file processing toolkit.
- **Pangenome Alignments**: Handles pangenome alignment data.
- **Fast Processing**: Optimized for high-performance processing.
- **Format Conversion**: Converts between alignment formats.
- **Filtering**: Filters alignments based on various criteria.

## Pitfalls
- **GAF Format**: Requires proper GAF format understanding.
- **Memory Usage**: Large files require significant memory.
- **Indexing**: May require indexing for large files.
- **Complex Filters**: Complex filtering options require care.
- **Output Compatibility**: Output may need conversion for other tools.

## Examples
### Filter alignments
**Args:** `gaftools filter -i alignments.gaf -o filtered.gaf -m 100`
**Explanation:** Filters alignments with mapping quality >= 100.

### Convert to PAF
**Args:** `gaftools convert -i alignments.gaf -o alignments.paf -f paf`
**Explanation:** Converts GAF to PAF format.

### Sort alignments
**Args:** `gaftools sort -i alignments.gaf -o sorted.gaf`
**Explanation:** Sorts alignments by reference position.

### Calculate coverage
**Args:** `gaftools coverage -i alignments.gaf -o coverage.txt`
**Explanation:** Calculates coverage statistics.

### Merge GAF files
**Args:** `gaftools merge -i file1.gaf file2.gaf -o merged.gaf`
**Explanation:** Merges multiple GAF files.