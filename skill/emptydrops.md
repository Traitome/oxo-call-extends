---
name: emptydrops
category: programming
description: "Python implementation of emptydrops from 10X Cellranger v3.0.2"
tags: [emptydrops, programming, single-cell, droplet-seq, empty-drops]
author: oxo-call-community
source_url: "https://pypi.org/project/emptydrops/"
---

## Concepts

- **Tool Overview**: EmptyDrops is a Python implementation of the empty droplet detection algorithm from 10X Genomics Cell Ranger v3.0.2, used to distinguish true cells from empty droplets in single-cell RNA-seq data.
- **Core Function**: Identifies and filters out empty droplets (background RNA) from droplet-based single-cell RNA-seq datasets.
- **Input/Output**: Input: Gene expression matrix (sparse matrix format), droplet barcodes. Output: Filtered cell matrix, empty droplet calls, statistics.
- **Algorithm**: Uses Monte Carlo simulation to estimate the probability that each droplet contains only background RNA.
- **Key Features**: Empty droplet detection, background estimation, FDR-based filtering, compatible with 10X data, integration with scanpy/Seurat.
- **Installation**: `pip install emptydrops` or `conda install -c bioconda emptydrops`

## Pitfalls

- **Data Format**: Requires specific sparse matrix format for input.
- **Sequencing Depth**: Performance depends on sequencing depth and library quality.
- **Parameter Tuning**: Default parameters may need adjustment for specific datasets.
- **Memory Usage**: Large datasets require significant memory.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic empty droplet filtering
**Args:** `emptydrops count_matrix.mtx -o filtered_matrix.mtx`
**Explanation:** Identifies and filters empty droplets from count matrix.

### With FDR threshold
**Args:** `emptydrops count_matrix.mtx -o filtered_matrix.mtx -f 0.01`
**Explanation:** Uses FDR threshold of 0.01 for filtering.

### Output statistics
**Args:** `emptydrops count_matrix.mtx -o filtered_matrix.mtx -s stats.txt`
**Explanation:** Outputs statistics about empty droplet detection.

### Batch processing
**Args:** `emptydrops -i samples/ -o results/ --batch`
**Explanation:** Processes multiple samples in batch mode.

### Integration with scanpy
**Args:** `python -c "import emptydrops; adata = emptydrops.filter_empty(adata)"`
**Explanation:** Filters empty droplets directly in scanpy AnnData object.