---
name: cmappy
category: utility
description: Tools for interacting with Connectivity Map data formats (.gct, .gctx, .grp, .gmt)
tags: [cmappy, connectivity-map, gct, gctx, bioinformatics, data-analysis]
author: oxo-call-community
source_url: "https://github.com/cmap/cmapPy"
---

## Concepts

- **Tool Overview**: cmappy (cmapPy) provides tools for working with Connectivity Map data formats and interacting with Broad Institute's Connectivity Map resources.
- **Core Function**: Handles .gct (Gene Cluster Text), .gctx (Gene Cluster Text eXtended), .grp (group), and .gmt (GMT) file formats.
- **Algorithm**: Parses and manipulates Connectivity Map data structures and formats.
- **Input**: Connectivity Map file formats (.gct, .gctx, .grp, .gmt).
- **Output**: Processed data in various formats for downstream analysis.
- **Application**: Gene expression analysis, Connectivity Map queries, and drug discovery.
- **Installation**: Install via bioconda: `conda install -c bioconda cmappy`

## Pitfalls

- **File Format**: Requires specific Connectivity Map formats (.gct, .gctx, etc.).
- **Data Size**: May require significant memory for large .gctx files.
- **Version Compatibility**: Different file versions may have different structures.
- **Data Integrity**: Requires properly formatted input files.
- **Dependency**: May require other Connectivity Map tools for full functionality.

## Examples

### Read GCT file
**Args:** `cmappy read_gct -i data.gct -o output.txt`
**Explanation:** Reads and processes a GCT format file.

### Convert GCT to GCTX
**Args:** `cmappy convert -i data.gct -o data.gctx`
**Explanation:** Converts GCT format to GCTX format.

### Query Connectivity Map
**Args:** `cmappy query -i signature.gct -o results.txt`
**Explanation:** Queries Connectivity Map with a gene expression signature.

### Display help
**Args:** `cmappy --help`
**Explanation:** Shows all available options and usage information.