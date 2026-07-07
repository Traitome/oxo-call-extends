---
name: bwread
category: programming
description: Fast BigWig file reader for Python with PyRanges and DataFrame support
tags: [bwread, bigwig, python, genomics, data-loading]
author: oxo-call-community
source_url: "http://github.com/endrebak/bwread"
---

## Concepts

- **Tool Overview**: bwread is a fast Python library for reading BigWig files into PyRanges or pandas DataFrames.
- **Core Function**: Efficiently loads genomic signal data from BigWig format.
- **Features**: Fast parsing, support for multiple output formats, region-based queries.
- **Input**: BigWig format files containing genomic signal data.
- **Output**: PyRanges objects or pandas DataFrames.
- **Installation**: Install via bioconda: `conda install -c bioconda bwread`

## Pitfalls

- **Python Library**: This is a Python library, not a command-line tool.
- **BigWig Format**: Only works with BigWig files; not BED or other formats.
- **Memory Usage**: Large BigWig files may require significant memory.
- **Chromosome Names**: Ensure chromosome naming consistency between files.

## Examples

### Read BigWig to PyRanges
**Args:** `import bwread; result = bwread.read_bigwig('signal.bw')`
**Explanation:** Reads entire BigWig file into a PyRanges object.

### Query specific region
**Args:** `result = bwread.read_bigwig('signal.bw', chrom='chr1', start=1000, end=2000)`
**Explanation:** Reads signal from specific genomic region.