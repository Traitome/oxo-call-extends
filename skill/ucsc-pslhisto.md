---
name: ucsc-pslhisto
category: utility
description: UCSC pslHisto - Tool for generating PSL alignment histograms.
tags: [ucsc-pslhisto, ucsc, psl, histogram, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC pslHisto - A tool for generating histograms from PSL alignments.
- **Core Function**: Creates histograms from alignment data.
- **Input**: PSL file.
- **Output**: Histogram data.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data visualization, statistical analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper PSL format.

## Examples

### Generate histogram
**Args:** `pslHisto input.psl > histogram.txt`
**Explanation:** Generate alignment histogram.

### With options
**Args:** `pslHisto -bins=100 input.psl > histogram.txt`
**Explanation:** Number of histogram bins.
