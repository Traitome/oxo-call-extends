---
name: topas
category: analysis
description: TOPAS - Tool for analyzing topologically associated domains (TADs).
tags: [topas, tads, chromatin-structure, 3d-genomics, epigenomics]
author: oxo-call-community
source_url: "https://github.com/compbio/topas"
---

## Concepts

- **Tool Overview**: TOPAS - A tool for analyzing and identifying Topologically Associated Domains (TADs) from Hi-C data.
- **Core Function**: Identifies TAD boundaries and characterizes interactions within and between TADs.
- **Input**: Hi-C contact matrices, genome annotations.
- **Output**: TAD boundaries, interaction matrices, visualization files.
- **Installation**: `pip install topas` or `conda install -c bioconda topas`
- **Use Case**: 3D genome analysis, chromatin architecture, gene regulation.

## Pitfalls

- **Resolution**: Hi-C data resolution affects TAD calling accuracy.
- **Normalization**: Requires proper normalization of Hi-C data.

## Examples

### Call TADs
**Args:** `topas -i hic_matrix.h5 -o tads/`
**Explanation:** Identify TADs from Hi-C contact matrix.

### With insulation score
**Args:** `topas -i hic_data.h5 --insulation -o tads_with_insulation/`
**Explanation:** Calculate insulation scores and call TADs.
