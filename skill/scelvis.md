---
name: scelvis
category: visualization
description: SCelVis - web-based visualization of single-cell data
tags: ["scelvis", "visualization", "single-cell", "web-app"]
author: oxo-call-community
source_url: "https://github.com/bihealth/scelvis"
---

## Concepts

- **Tool Overview**: SCelVis (v0.8.9) is a web-based visualization tool for single-cell data exploration.
- **Core Function**: Provides interactive visualization of single-cell RNA-seq data.
- **Algorithm**: Implements various visualization techniques for single-cell data.
- **Input/Output**: Accepts AnnData files and produces interactive web visualizations.
- **Web Interface**: Offers user-friendly web-based interface for data exploration.
- **Applications**: Single-cell data exploration, publication-quality figures, and collaborative analysis.

## Pitfalls

- **Data Size**: May struggle with very large datasets.
- **Memory Usage**: High memory requirements for large datasets.
- **Browser Compatibility**: Requires modern web browser.
- **Network Requirements**: Web-based interface requires network access.
- **Computational Resources**: Server-side processing may require significant resources.
- **Dependency Management**: Requires proper environment setup.

## Examples

### Start web server
**Args:** `scelvis serve -i data.h5ad --host 0.0.0.0 --port 8000`
**Explanation:** Starts web server for interactive visualization.

### Generate static report
**Args:** `scelvis report -i data.h5ad -o report.html`
**Explanation:** Generates static HTML report.

### Multiple datasets
**Args:** `scelvis serve -i dataset1.h5ad dataset2.h5ad`
**Explanation:** Serves multiple datasets simultaneously.

### Custom port
**Args:** `scelvis serve -i data.h5ad --port 9000`
**Explanation:** Uses custom port for web server.

### Verbose logging
**Args:** `scelvis serve -i data.h5ad -v`
**Explanation:** `-v` enables verbose output for debugging.

### Export visualization
**Args:** `scelvis export -i data.h5ad -t umap -o umap.png`
**Explanation:** Exports specific visualization to image file.

### Help command
**Args:** `scelvis --help`
**Explanation:** Shows available commands and options.