---
name: fastdtw
category: utility
description: "Dynamic Time Warping (DTW) algorithm with an O(N) time and memory complexity"
tags: [fastdtw, utility, DTW, time-series, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/slaypni/fastdtw"
---

## Concepts

- **Tool Overview**: FastDTW is an implementation of the Dynamic Time Warping algorithm optimized for O(N) time and memory complexity.
- **Core Function**: Performs time series alignment using dynamic time warping with improved efficiency.
- **Input/Output**: Input: Time series data. Output: Alignment path, distance score.
- **Algorithm**: Implements FastDTW algorithm for efficient time series comparison.
- **Key Features**: O(N) complexity, fast alignment, memory efficient, multiple distance metrics, Python integration.
- **Installation**: `conda install -c bioconda fastdtw`

## Pitfalls

- **Parameter Tuning**: Requires careful parameter selection.
- **Data Scaling**: May require data normalization.
- **Memory Usage**: Very long sequences may require significant memory.
- **Computation Time**: Complex alignments may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic DTW alignment
**Args:** `python -c "from fastdtw import fastdtw; distance, path = fastdtw(series1, series2)"`
**Explanation:** Performs FastDTW alignment between two time series.

### Custom distance metric
**Args:** `python -c "distance, path = fastdtw(series1, series2, dist=euclidean)"`
**Explanation:** Uses custom distance metric for alignment.

### With radius parameter
**Args:** `python -c "distance, path = fastdtw(series1, series2, radius=3)"`
**Explanation:** Sets search radius for faster computation.

### Output alignment path
**Args:** `python -c "distance, path = fastdtw(series1, series2); print(path)"`
**Explanation:** Prints alignment path.

### Batch processing
**Args:** `python -c "for s in series_list: fastdtw(s, reference)"`
**Explanation:** Processes multiple time series.