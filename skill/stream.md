---
name: stream
category: single-cell
description: STREAM - Single-cell Trajectories Reconstruction, Exploration And Mapping.
tags: [stream, single-cell, trajectory-analysis, rna-seq]
author: oxo-call-community
source_url: "https://github.com/pinellolab/STREAM"
---

## Concepts

- **Tool Overview**: stream (v1.1) is a tool for reconstructing and analyzing single-cell trajectories from scRNA-seq data.
- **Core Function**: Identifies developmental trajectories and cell fate transitions from single-cell data.
- **Algorithm**: Uses graph-based trajectory inference to model cell differentiation paths.
- **Input/Output**: Input: scRNA-seq count matrix; Output: Trajectory model with cell ordering.
- **Applications**: Developmental biology, cell differentiation, pseudotime analysis.
- **Installation**: `conda install -c bioconda stream` or download from GitHub.

## Pitfalls

- **Data Quality**: Poor quality scRNA-seq data affects trajectory accuracy.
- **Cell Filtering**: Poor quality cells affect trajectory inference.
- **Parameter Tuning**: Incorrect parameters affect trajectory topology.
- **Batch Effects**: Batch effects between samples affect comparison.
- **Memory Requirements**: Large datasets require significant memory.
- **Computational Time**: Processing large datasets can be slow.

## Examples

### Display help
**Args:** `stream --help`
**Explanation:** Shows available options and usage information.

### Basic trajectory analysis
**Args:** `stream -i counts.h5ad -o results/`
**Explanation:** Reconstruct trajectories from scRNA-seq data.

### With normalization
**Args:** `stream -i counts.h5ad -o results/ --normalize`
**Explanation:** Apply normalization before trajectory inference.

### Verbose mode
**Args:** `stream -i counts.h5ad -o results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Output visualization
**Args:** `stream -i counts.h5ad -o results/ --plot`
**Explanation:** Generate visualization of trajectories.

### Custom parameters
**Args:** `stream -i counts.h5ad -o results/ -k 15`
**Explanation:** Use k=15 nearest neighbors for graph construction.

### Batch processing
**Args:** `stream -i batch/ -o results/`
**Explanation:** Process multiple scRNA-seq datasets together.

### Pseudotime calculation
**Args:** `stream -i counts.h5ad -o results/ --pseudotime`
**Explanation:** Calculate pseudotime for cells along trajectory.

### Generate report
**Args:** `stream -i counts.h5ad -o results/ --report`
**Explanation:** Generate comprehensive HTML report.
