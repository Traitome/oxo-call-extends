---
name: cogtriangles
category: assembly
description: Low-polynomial algorithm for assembling clusters of orthologous groups from intergenomic symmetric best matches.
tags: [cogtriangles, assembly]
author: oxo-call-community
source_url: "https://ftp.ncbi.nih.gov/pub/wolf/COGs/COGsoft"
---

## Concepts

- **Tool Overview**: cogtriangles (v2012.04) - Low-polynomial algorithm for assembling clusters of orthologous groups from intergenomic symmetric best matches.
- **Core Function**: Low-polynomial algorithm for assembling clusters of orthologous groups from intergenomic symmetric best matches.
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda cogtriangles`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assemble reads into contigs
