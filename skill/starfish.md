---
name: starfish
category: spatial-omics
description: Standardized analysis pipeline for image-based transcriptomics.
tags: [starfish, spatial-omics, image-analysis, transcriptomics]
author: oxo-call-community
source_url: "https://spacetx-starfish.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: starfish (v0.4.0) is a Python library for analyzing image-based spatial transcriptomics data.
- **Core Function**: Provides standardized pipeline for processing, analyzing, and visualizing spatial transcriptomics images.
- **Workflow Components**: Image registration → spot detection → gene assignment → spatial visualization.
- **Input/Output**: Input: Multi-channel images from spatial transcriptomics experiments; Output: Gene expression matrices with spatial coordinates.
- **Supported Technologies**: MERFISH, SeqFISH, osmFISH, and other image-based transcriptomics methods.
- **Installation**: `conda install -c bioconda starfish` or `pip install starfish`.

## Pitfalls

- **Image Quality**: Low-quality or blurry images affect spot detection accuracy.
- **Registration Errors**: Incorrect image registration leads to misaligned spatial data.
- **Spot Detection**: Improper spot detection parameters miss or misidentify spots.
- **Gene Assignment**: Ambiguous barcodes cause incorrect gene assignments.
- **Memory Requirements**: Large high-resolution images require significant memory.
- **Computational Time**: Processing large datasets can be computationally intensive.

## Examples

### Display help
**Args:** `starfish --help`
**Explanation:** Shows available options and usage information.

### Basic analysis
**Args:** `starfish run --input experiment.json --output results/`
**Explanation:** Run complete analysis pipeline using experiment configuration.

### Image registration
**Args:** `starfish register -i images/ -o registered/ --method rigid`
**Explanation:** Register multi-channel images using rigid transformation.

### Spot detection
**Args:** `starfish detect -i registered/ -o spots.npy --method blob`
**Explanation:** Detect spots using blob detection algorithm.

### Gene decoding
**Args:** `starfish decode -i spots.npy -b barcodes.json -o counts.csv`
**Explanation:** Decode barcodes and generate gene expression matrix.

### Visualization
**Args:** `starfish plot -i counts.csv -o spatial_plot.png`
**Explanation:** Generate spatial visualization of gene expression.

### Quality control
**Args:** `starfish qc -i images/ -o qc_report.html`
**Explanation:** Generate quality control report.

### Verbose mode
**Args:** `starfish run --input experiment.json --output results/ -v`
**Explanation:** Run with detailed logging for debugging.

### Interactive analysis
**Args:** `starfish notebook`
**Explanation:** Launch Jupyter notebook for interactive analysis.
