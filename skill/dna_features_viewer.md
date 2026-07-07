---
name: dna_features_viewer
category: utility
description: DNA Features Viewer - Python library for visualizing DNA features.
tags: [dna_features_viewer, utility, visualization, dna, features, genbank]
author: oxo-call-community
source_url: "https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer"
---

## Concepts

- **Tool Overview**: DNA Features Viewer is a Python library for visualizing DNA sequences and annotations.
- **Core Function**: Creates publication-quality visualizations of DNA features, annotations, and sequences.
- **Input/Output**: Input: GenBank records, FASTA with annotations. Output: Visual diagrams (PNG/SVG).
- **Algorithm**: Renders DNA features and annotations in linear or circular format.
- **Key Features**: Feature visualization, customizable styles, multiple output formats, circular/linear views, publication-ready figures.
- **Installation**: `conda install -c bioconda dna_features_viewer`

## Pitfalls

- **Input Requirements**: Requires DNA sequences with feature annotations.
- **Complexity**: Too many features can make visualization cluttered.
- **Output Size**: High-resolution images may be large.
- **Annotation Format**: Must use supported annotation formats.
- **Memory Usage**: Large sequences with many features may require significant memory.

## Examples

### Visualize DNA features
**Args:** `dna_features_viewer --record sequence.gb --output plot.png`
**Explanation:** Visualizes DNA features from GenBank record.

### Circular view
**Args:** `dna_features_viewer --record sequence.gb --output plot.png --circular`
**Explanation:** Generate circular visualization of DNA features.

### Custom colors
**Args:** `dna_features_viewer --record sequence.gb --output plot.png --colors colors.json`
**Explanation:** Use custom color scheme for features.

### Linear view with scale
**Args:** `dna_features_viewer --record sequence.gb --output plot.png --linear --show-scale`
**Explanation:** Generate linear view with scale bar.

### Batch visualization
**Args:** `dna_features_viewer --input-dir genbank/ --output-dir plots/`
**Explanation:** Visualize multiple GenBank records in batch.