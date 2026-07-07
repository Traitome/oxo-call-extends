---
name: escher
category: population-genomics
description: "Escher: A Web Application for Building, Sharing, and Embedding Data-Rich Visualizations of Metabolic Pathways"
tags: [escher, population-genomics, metabolic-pathways, visualization, pathways]
author: oxo-call-community
source_url: "https://escher.github.io"
---

## Concepts

- **Tool Overview**: Escher is a web-based tool for visualizing and exploring metabolic pathways, allowing users to build, share, and embed data-rich pathway visualizations.
- **Core Function**: Creates interactive visualizations of metabolic pathways with support for overlaying experimental data such as gene expression levels or metabolite concentrations.
- **Input/Output**: Input: Pathway models (SBML, JSON), experimental data (CSV, JSON). Output: Interactive pathway visualizations, embedded widgets, static images.
- **Algorithm**: Uses SVG-based rendering for interactive pathway visualization with zooming, panning, and data overlay capabilities.
- **Key Features**: Interactive visualization, data overlay, pathway editing, sharing capabilities, embedding support, multi-species pathways.
- **Installation**: `conda install -c bioconda escher`

## Pitfalls

- **Web Browser**: Requires modern web browser with JavaScript enabled.
- **Pathway Data**: Requires properly formatted pathway models.
- **Data Format**: Experimental data must be in compatible formats.
- **Server Requirements**: Self-hosted instances require web server setup.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Launch Escher web app
**Args:** `escher`
**Explanation:** Launches the Escher web application.

### Load pathway model
**Args:** `escher --load pathway.json`
**Explanation:** Loads a pathway model from JSON file.

### Overlay experimental data
**Args:** `escher --load pathway.json --data expression_data.csv`
**Explanation:** Overlays gene expression data on pathway visualization.

### Export visualization
**Args:** `escher --load pathway.json --export pathway.png`
**Explanation:** Exports pathway visualization as PNG image.

### Batch processing
**Args:** `escher --batch config.json`
**Explanation:** Processes multiple pathways with configuration file.