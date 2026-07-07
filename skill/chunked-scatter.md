---
name: chunked-scatter
category: formatting
description: Chunk and scatter regions in BED or sequence dictionary files
tags: [chunked-scatter, formatting, bed, parallel-processing, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/biowdl/chunked-scatter"
---

## Concepts

- **Tool Overview**: chunked-scatter splits genomic regions from BED or sequence dict files into smaller chunks for parallel processing.
- **Core Function**: Divides large genomic regions into manageable chunks for distributed computing workflows.
- **Features**: Region chunking, scatter generation, support for various input formats, and customizable chunk sizes.
- **Input**: BED file or sequence dictionary file defining genomic regions.
- **Output**: Multiple smaller BED files or scatter files for parallel processing.
- **Application**: Parallel genomic analysis, workflow optimization, and distributed computing.
- **Installation**: Install via bioconda: `conda install -c bioconda chunked-scatter`

## Pitfalls

- **Chunk Size**: Choosing appropriate chunk size is critical for optimal parallelization.
- **Overlapping Regions**: May create overlapping chunks if not configured properly.
- **Input Format**: Requires properly formatted BED or sequence dict files.
- **Memory Usage**: May require significant memory for very large region files.
- **Output Management**: Multiple output files need proper organization.

## Examples

### Chunk BED file
**Args:** `chunked-scatter -i regions.bed -c 1000000 -o chunks/`
**Explanation:** Splits BED regions into 1MB chunks.

### Scatter for parallel processing
**Args:** `chunked-scatter -i regions.bed --scatter 10 -o scatter_files/`
**Explanation:** Creates 10 scatter files for parallel processing.

### From sequence dict
**Args:** `chunked-scatter -i sequence.dict -c 5000000 -o chunks/`
**Explanation:** Creates chunks from sequence dictionary.

### Display help
**Args:** `chunked-scatter --help`
**Explanation:** Shows all available options and usage information.