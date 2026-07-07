---
name: soda-gallery
category: visualization
description: SODA Gallery - Python-based UCSC genome browser gallery generator
tags: [soda-gallery, visualization, ucsc, genome-browser, gallery]
author: oxo-call-community
source_url: "https://github.com/alexpreynolds/soda"
---

## Concepts

- **Tool Overview**: soda-gallery (v1.2.0) - A UCSC genome browser gallery generator
- **Core Function**: Creates visual galleries for UCSC genome browser tracks
- **Input/Output**: Accepts track files; outputs HTML gallery with visualizations
- **Algorithm**: Generates static HTML galleries from genome browser data
- **Installation**: `conda install -c bioconda soda-gallery`
- **Key Features**: Gallery generation, UCSC integration, HTML output

## Pitfalls

- **Input Requirements**: Requires properly formatted track files
- **UCSC Compatibility**: Requires UCSC genome browser compatibility
- **Output Directory**: Requires proper output directory setup
- **Track Format**: Track files must be in correct format
- **HTML Generation**: Requires proper HTML template
- **Large Tracks**: Large tracks may slow gallery generation

## Examples

### Display help
**Args:** `soda-gallery --help`
**Explanation:** Shows available options and usage information.

### Basic gallery generation
**Args:** `soda-gallery -i tracks.bed -o gallery.html`
**Explanation:** Generate gallery from track file.

### With multiple tracks
**Args:** `soda-gallery -i track1.bed track2.bed -o gallery.html`
**Explanation:** Generate gallery from multiple tracks.

### With genome assembly
**Args:** `soda-gallery -i tracks.bed -g hg38 -o gallery.html`
**Explanation:** Specify genome assembly for gallery.

### With custom template
**Args:** `soda-gallery -i tracks.bed -t template.html -o gallery.html`
**Explanation:** Use custom HTML template.

### With title
**Args:** `soda-gallery -i tracks.bed -o gallery.html --title "My Gallery"`
**Explanation:** Set gallery title.

### Output directory
**Args:** `soda-gallery -i tracks.bed -o gallery_dir/`
**Explanation:** Output gallery to directory.

### Generate report
**Args:** `soda-gallery -i tracks.bed -o gallery.html --report`
**Explanation:** Generate gallery report.