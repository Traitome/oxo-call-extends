---
name: gbkviz
category: utility
description: Web-based Genbank data visualization and genome comparison tool using Streamlit and GenomeDiagram
tags: [gbkviz, genome-visualization, genbank, genbank-visualization, streamlit, animated-diagram]
author: oxo-call-community
source_url: "https://github.com/moshi4/GBKviz/"
---

## Concepts

- **Tool Overview**: GBKviz is a web-based Genbank data visualization and comparison tool developed with the Streamlit framework. It enables easy and flexible drawing of CDS features in user-specified genomic regions.
- **Core Function**: Visualizes GenBank file annotations as interactive or static diagrams, allowing comparison between multiple genomes. Supports both single-genome visualization and whole-genome comparisons using MUMmer.
- **Input Format**: Accepts standard GenBank format files (.gb, .gbk, .gbff). Files can be uploaded through the web interface or specified via command line.
- **Output Formats**: PNG (raster) and SVG (vector) image formats are available for download. The web interface provides interactive pan/zoom capabilities.
- **Comparison Feature**: When comparing multiple genomes, GBKviz uses MUMmer for whole-genome alignment and visualizes homologous regions with connecting lines.
- **Key Technologies**:
  - Streamlit for the web framework
  - GenomeDiagram (part of Biopython) for rendering
  - MUMmer for genome comparison algorithms
- **Deployment Options**:
  - Local installation and run via web browser
  - Streamlit Cloud deployment (https://share.streamlit.io/moshi4/gbkviz/main/src/gbkviz/gbkviz_webapp.py)
- **Installation**: `pip install gbkviz` (requires Python 3.7+). Bioconda: `conda install -c bioconda gbkviz`

## Pitfalls

- **CRITICAL: MUMmer Dependency**: Genome comparison features require MUMmer4 (>=4.0.0rc1) to be installed separately. Without it, single-genome visualization still works but comparison mode will fail.
- **CRITICAL: Streamlit Execution**: GBKviz runs as a web application. You must keep the terminal open while using it. Closing the terminal terminates the application.
- **Large GenBank Files**: Very large genomes with thousands of features may be slow to render. Consider using the region selection feature to focus on specific genomic intervals.
- **Browser Compatibility**: Some features may not work properly in all browsers. Chrome/Chromium-based browsers are recommended.
- **Memory Usage**: Loading multiple large GenBank files simultaneously may require significant RAM.
- **File Format Issues**: GBKviz expects standard GenBank format. Inconsistent feature tables or malformed files may cause rendering errors.
- **Web App Port Conflicts**: If port 8501 is already in use, Streamlit will auto-increment to 8502, etc. Ensure no other Streamlit apps are running simultaneously.

## Examples

### Launch GBKviz web application locally
**Args:** `gbkviz_webapp`
**Explanation:** Starts the GBKviz web interface on localhost (default port 8501). Open a web browser and navigate to http://localhost:8501 to access the interface. Upload GenBank files through the web interface to begin visualization.

### Visualize single genome via command line (if CLI available)
**Args:** `gbkviz --input genome.gb --output genome.png --format png`
**Explanation:** Some versions may support command-line rendering. Check `gbkviz --help` for available options. This bypasses the web interface for batch processing.

### Compare two bacterial genomes
**Args:** Upload genome1.gb and genome2.gb through the web interface, select "Compare Genomes" mode, then click "Run Comparison"
**Explanation:** The web interface allows uploading multiple GenBank files. Select comparison mode to run MUMmer alignment and visualize homologous regions between the two genomes with connecting lines.

### Focus on specific genomic region
**Args:** In the web interface, enter coordinates like "10000-50000" in the region selection box and click "Update"
**Explanation:** Instead of rendering the entire genome, specify a start and end position to zoom into a specific region. Useful for detailed examination of genomic islands, operons, or other features of interest.

### Export as vector SVG
**Args:** In the web interface, select "SVG" from the format dropdown and click "Download"
**Explanation:** SVG format produces scalable vector graphics suitable for publication figures. Unlike PNG, SVG can be edited in vector graphics software like Adobe Illustrator or Inkscape.

### Customize gene color scheme
**Args:** In the web interface, modify color settings in the sidebar panel, then click "Redraw"
**Explanation:** The sidebar provides options to customize colors for different feature types (CDS, tRNA, rRNA, etc.). Changes are reflected immediately in the preview.

### Set track height and feature spacing
**Args:** Adjust "Track Height" and "Feature Spacing" sliders in the web interface sidebar
**Explanation:** These parameters control the density of the visualization. Increase track height for more vertical space per gene, adjust spacing to prevent label overlap in dense regions.

### Generate circular genome diagram
**Args:** Select "Circular" from the "Diagram Type" dropdown in the web interface
**Explanation:** GBKviz supports both linear and circular diagram types. Circular is ideal for bacterial chromosomes and plasmids, while linear works better for large eukaryotic chromosomes or when comparing collinear regions.

### Save session state
**Args:** Click "Save Settings" in the web interface to download a JSON file with current visualization settings
**Explanation:** Save your color schemes, region selections, and other settings to a JSON file. Load it later with "Load Settings" to reproduce the exact same visualization without reconfiguring manually.
