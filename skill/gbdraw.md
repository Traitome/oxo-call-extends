---
name: gbdraw
category: utility
description: A genome diagram generator for microbes and organelles, producing publication-quality figures
tags: [gbdraw, genome-visualization, genbank, circular-genome, linear-genome, svg-png-pdf]
author: oxo-call-community
source_url: "https://github.com/satoshikawato/gbdraw"
---

## Concepts

- **Tool Overview**: gbdraw is a command-line tool for generating publication-quality genome diagrams from GenBank/EMBL/DDBJ annotation files, supporting both circular and linear genome visualizations.
- **Core Function**: Converts annotated genome sequences (in GenBank format) into visual diagrams showing genes, CDS features, and other genomic annotations as customizable graphical representations.
- **Input Format**: Accepts standard bioinformatics formats including .gb, .gbk, .gbff, .embl, .ddbj files containing genome annotations.
- **Output Formats**: Multiple vector and raster formats including SVG (primary, editable), PNG (high DPI for publications), PDF, EPS, and PS formats.
- **Genome Types**: Supports both circular genomes (bacteria, plasmids, mitochondria, chloroplasts) and linear genomes (eukaryotes, large DNA viruses).
- **Key Features**:
  - `--separate_strands` option to show forward and reverse strand features on opposite sides
  - `--track_type tuckin` for compact visualization of gene density
  - BLAST-based whole genome comparison support
  - Streamlit web application available at https://gbdraw.app/
- **Design Philosophy**: Emphasizes creating "beautiful figures" with customizable styling, element placement, and color schemes that are intuitive for biologists.
- **Installation**: `conda install -c bioconda gbdraw` or `pip install gbdraw`

## Pitfalls

- **CRITICAL: GenBank Quality**: The quality of the output diagram depends heavily on the quality and completeness of the input GenBank file. Ensure features have proper qualifiers (/label, /product, /translation) for meaningful labels.
- **File Encoding**: Ensure input files are properly formatted. gbdraw may fail on files with non-standard line endings or encoding issues.
- **Large Genomes**: Very large genomes (>10 Mb) may produce complex diagrams that are difficult to interpret. Consider subsetting to regions of interest.
- **Memory Usage**: High-resolution PNG output (300-600 DPI) requires significant memory. Ensure adequate RAM for large figures.
- **Color Scheme**: Default colors may not be optimal for all publications. Use --track_color or similar options to customize.
- **Feature Overlap**: Dense feature regions may have overlapping labels. Adjust figure dimensions or use --separate_strands to reduce clutter.
- **Python Version**: Requires Python 3.x. Some dependencies may conflict with Python 2 environments.

## Examples

### Draw circular genome with default settings
**Args:** `circular -i AP027078.gb -f svg`
**Explanation:** The simplest usage for a circular genome. Takes a GenBank file and outputs an SVG diagram. SVG format is recommended for editable vector graphics that can be modified in Inkscape or Illustrator.

### Circular genome with strand separation
**Args:** `circular -i ecoli_chromosome.gb -f svg --separate_strands --track_type tuckin`
**Explanation:** The `--separate_strands` option places forward-strand features on the outside track and reverse-strand features on the inside track. `--track_type tuckin` creates a more compact visualization showing gene density rather than individual gene labels.

### Export as PNG for publication (300 DPI)
**Args:** `circular -i genome.gb -f png --width 300 --height 300 -o output.png`
**Explanation:** PNG output at 300 DPI is suitable for journal publications. The --width and --height parameters control figure dimensions in pixels at the specified resolution.

### Linear genome visualization
**Args:** `linear -i chromosome.gb -f svg -o chromosome_view.svg`
**Explanation:** For linear genomes, use the `linear` subcommand instead of `circular`. Useful for eukaryotic chromosomes, large viral genomes, or any linear assembly.

### Compare two genomes with BLAST
**Args:** `circular -i genome1.gb -i genome2.gb -f svg --compare --method blast`
**Explanation:** The `--compare` flag enables whole-genome comparison between two GenBank files using BLAST. This highlights homologous regions between the genomes with connecting lines.

### Custom color scheme for tracks
**Args:** `circular -i genome.gb -f svg --track_color blue,red,green`
**Explanation:** Customize the color scheme for different feature tracks. Useful for matching publication figures or highlighting specific genomic regions of interest.

### Show only CDS features
**Args:** `circular -i genome.gb -f svg --feature_types CDS,tRNA,rRNA`
**Explanation:** Use `--feature_types` to filter which features are displayed. This is useful for reducing clutter or focusing on specific feature categories like protein-coding genes (CDS) and non-coding RNAs.

### Multi-page PDF for large genomes
**Args:** `linear -i large_genome.gb -f pdf --pagesize A4 --orientation landscape`
**Explanation:** For very large genomes, PDF output with multiple pages may be more manageable than a single large SVG. Use --pagesize and --orientation to control page layout.
