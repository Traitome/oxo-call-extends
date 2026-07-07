---
name: ucsc-texthistogram
category: utility
description: UCSC textHistogram - Tool for generating text histograms.
tags: [ucsc-texthistogram, ucsc, histogram, statistics, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC textHistogram - A tool for generating text histograms.
- **Core Function**: Generates histogram from numerical data.
- **Input**: Numerical data file.
- **Output**: Histogram text output.
- **Installation**: Part of UCSC utilities
- **Use Case**: Data visualization, statistics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Data Format**: Requires proper numerical format.

## Examples

### Generate histogram
**Args:** `textHistogram input.txt > histogram.txt`
**Explanation:** Generate histogram from data.

### With options
**Args:** `textHistogram -bins=20 input.txt > histogram.txt`
**Explanation:** Generate with 20 bins.
