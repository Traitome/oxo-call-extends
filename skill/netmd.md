---
name: netmd
category: alignment
description: NetMD is a computational method for identifying consensus behavior across multiple molecular dynamics simulations.
tags: [netmd, alignment]
author: oxo-call-community
source_url: "https://github.com/mazzalab/NetMD"
---

## Concepts
- **Tool Overview**: Using Graph-based Embeddings and Dynamic Time Warping, *NetMD* aligns trajectories that may be temporally out of sync and pinpoints the replicas that most faithfully represent the overall ensemble behavior. This enables consistent comparisons across simulations and supports reliable characterization of system variants, making it easier to detect shared patterns and reduce the influence of outliers or simulation artifacts.
- **Core Function**: Processes bioinformatics data for alignment tasks.
- **Input/Output**: Standard bioinformatics formats (FASTA/FASTQ, BAM, VCF, etc.).
- **Installation**: `conda install -c bioconda netmd`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
