---
name: w4mclstrpeakpics
category: bioinformatics
description: W4M-ClstrPeakPics - Peak clustering tool.
tags: [w4mclstrpeakpics, metabolomics, peak-clustering, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/workflow4metabolomics/"
---

## Concepts

- **Tool Overview**: W4M-ClstrPeakPics - Peak clustering tool.
- **Core Function**: Clusters peaks in metabolomics data.
- **Input**: Peak data.
- **Output**: Clustered peaks.
- **Installation**: Install via conda
- **Use Case**: Metabolomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large datasets.
- **Parameters**: Clustering parameters affect results.

## Examples

### Cluster peaks
**Args:** `w4mclstrpeakpics -i peaks.csv -o clusters.csv`
**Explanation:** Cluster peaks.

### With options
**Args:** `w4mclstrpeakpics -i peaks.csv -o clusters.csv -k 5`
**Explanation:** Cluster into 5 groups.
