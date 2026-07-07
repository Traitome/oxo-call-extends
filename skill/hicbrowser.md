---
name: hicbrowser
category: bioinformatics
description: HiCBrowser is a web browser for visualizing Hi-C and other genomic tracks (bigwig, BED, interactions).
tags: [hicbrowser, Hi-C, visualization, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/maxplanck-ie/HiCBrowser"
---

## Concepts

- **Hi-C Visualization**: HiCBrowser visualizes Hi-C contact maps.

- **Genomic Tracks**: Displays various genomic track types.

- **Interactive Browser**: Provides interactive visualization.

- **BigWig Support**: Supports BigWig format tracks.

- **BED Support**: Supports BED format annotations.

- **Contact Maps**: Visualizes chromatin interactions.

## Pitfalls

- **Data Loading**: Large files may take time to load.

- **Browser Compatibility**: Requires modern web browser.

- **Memory Usage**: Large datasets may require significant memory.

- **Network Access**: Web interface requires network access.

- **Rendering Performance**: May have performance issues with large data.

## Examples

### Start browser
**Args:** `hicbrowser --port 8080 --data data/`
**Explanation:** Starts HiCBrowser on port 8080.

### With custom configuration
**Args:** `hicbrowser --config config.yaml --port 8080`
**Explanation:** Uses custom configuration file.

### Load specific track
**Args:** `hicbrowser --tracks tracks.txt --port 8080`
**Explanation:** Loads specific tracks.

### Batch processing
**Args:** `for f in *.cool; do hicbrowser --add-track $f; done`
**Explanation:** Adds multiple tracks.

### Help command
**Args:** `hicbrowser --help`
**Explanation:** Shows available options and usage information.