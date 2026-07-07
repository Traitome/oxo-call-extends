---
name: sainsc
category: single_cell
description: Segmentation-free Analysis of In Situ Capture data for spatial transcriptomics
tags: ["sainsc", "spatial transcriptomics", "in situ", "RNA-seq", "segmentation"]
author: oxo-call-community
source_url: "https://sainsc.readthedocs.io"
---

## Concepts

- **Tool Overview**: SAiNSC (v0.3.1) is a segmentation-free analysis tool for in situ capture spatial transcriptomics data, enabling cell type identification without requiring image segmentation.
- **Core Function**: Analyzes spatial transcriptomics data to identify cell types and their spatial organization without relying on image segmentation.
- **Algorithm**: Uses graph-based clustering and spatial autocorrelation analysis to identify cell neighborhoods and cell types from transcriptomic data.
- **Input Format**: Spatial transcriptomics data (count matrices, spatial coordinates), optional imaging data.
- **Output Format**: Cell type annotations, spatial neighborhood maps, visualization plots, statistical reports.
- **Use Case**: Spatial transcriptomics analysis, tissue architecture studies, developmental biology, cancer research.

## Pitfalls

- **Data quality**: Requires high-quality spatial transcriptomics data with good coverage.
- **Cell density**: Works best with moderate to high cell density samples.
- **Reference data**: May require reference transcriptomes for cell type annotation.
- **Computational resources**: Large datasets require significant memory and CPU.
- **Parameter tuning**: May require adjustment of clustering parameters for optimal results.
- **Imaging data**: While segmentation-free, imaging data can improve results if available.

## Examples

### Basic analysis
**Args:** `sainsc analyze -i counts.csv -c coordinates.csv -o results`
**Explanation:** `-i` gene expression counts; `-c` spatial coordinates; `-o` output directory.

### With imaging data
**Args:** `sainsc analyze -i counts.csv -c coordinates.csv -m image.tif -o results`
**Explanation:** `-m` optional imaging data for enhanced analysis.

### Specify resolution
**Args:** `sainsc analyze -i counts.csv -c coordinates.csv -o results -r 50`
**Explanation:** `-r` spatial resolution parameter (default: 30).

### Cell type annotation
**Args:** `sainsc annotate -i results/clusters.h5ad -r reference.h5ad -o annotated.h5ad`
**Explanation:** Annotates clusters using reference transcriptome data.

### Visualize results
**Args:** `sainsc plot -i results/clusters.h5ad -o spatial_plot.png`
**Explanation:** Generates spatial visualization of cell clusters.

### Differential expression
**Args:** `sainsc de -i results/clusters.h5ad -o de_genes.csv`
**Explanation:** Performs differential expression analysis between clusters.

### Batch processing
**Args:** `sainsc batch -d sample_dir -o batch_results`
**Explanation:** Processes multiple samples in batch mode.