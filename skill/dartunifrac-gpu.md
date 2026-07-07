---
name: dartunifrac-gpu
category: formatting
description: DartUniFrac - ultra-fast UniFrac algorithm using GPU acceleration
tags: [dartunifrac-gpu, formatting, UniFrac, metagenomics, GPU]
author: oxo-call-community
source_url: "https://github.com/jianshu93/DartUniFrac/blob/v0.3.0/README.md"
---

## Concepts

- **Tool Overview**: dartunifrac-gpu (v0.3.0+) is an ultra-fast UniFrac algorithm that scales to millions of samples using GPU acceleration.
- **Core Function**: Computes UniFrac distances for microbial community comparison at scale.
- **Input/Output**: Input: OTU tables, phylogenetic trees. Output: Distance matrices, PCoA plots.
- **Algorithm**: Uses optimal balanced parenthesis and Weighted MinHash sketching for efficient computation.
- **Key Features**: GPU-accelerated, handles millions of samples, memory-efficient.
- **Installation**: `conda install -c bioconda dartunifrac-gpu`

## Pitfalls

- **GPU Requirements**: Requires NVIDIA GPU with CUDA support.
- **Memory Constraints**: Large datasets may require significant GPU memory.
- **Tree Format**: Requires properly formatted phylogenetic trees.
- **OTU Table Quality**: Results depend on OTU table completeness.
- **Sketch Size**: MinHash sketch size affects accuracy-performance tradeoff.

## Examples

### Compute UniFrac distances
**Args:** `dartunifrac-gpu -i otu_table.tsv -t tree.nwk -o distances.txt`
**Explanation:** Compute UniFrac distances using GPU acceleration.

### Use MinHash sketching
**Args:** `dartunifrac-gpu -i otu_table.tsv -t tree.nwk -o distances.txt --sketch-size 1000`
**Explanation:** Use MinHash sketching with 1000 sketches for faster computation.

### Generate PCoA
**Args:** `dartunifrac-gpu -i otu_table.tsv -t tree.nwk -o pcoa.txt --pcoa`
**Explanation:** Compute UniFrac distances and generate PCoA coordinates.
