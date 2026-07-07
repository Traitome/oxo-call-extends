---
name: svtopovz
category: visualization
description: Complex structural variant visualization plotting tool for HiFi sequencing data.
tags: [svtopovz, structural-variants, visualization, plotting]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/HiFi-SVTopo"
---

## Concepts

- **Tool Overview**: svtopovz (v0.3.0) visualizes complex structural variants from HiFi data.
- **Core Function**: Creates publication-ready visualizations of complex SVs.
- **Algorithm**: Renders SV information into graphical representations.
- **Input/Output**: Input: SV info file from svtopo; Output: SVG/PNG figures.
- **Applications**: Complex SV visualization, publication figures.
- **Installation**: `conda install -c bioconda svtopovz` or download from GitHub.

## Pitfalls

- **Input Quality**: Requires high-quality SV information from svtopo.
- **Memory Requirements**: Complex SVs require significant memory.
- **Performance**: Complex visualizations may be slow to render.
- **Parameter Tuning**: Incorrect parameters affect visualization quality.
- **Output Quality**: May require manual adjustment for publication.
- **SV Complexity**: Very complex SVs may be hard to visualize.

## Examples

### Display help
**Args:** `svtopovz --help`
**Explanation:** Shows available options and usage information.

### Basic SV visualization
**Args:** `svtopovz plot -i sv_info.txt -o sv_figure.svg`
**Explanation:** Generate visualization from extracted SV information.

### High resolution output
**Args:** `svtopovz plot -i sv_info.txt -o sv_figure.png -d 300`
**Explanation:** Generate high resolution PNG output.

### Verbose mode
**Args:** `svtopovz plot -i sv_info.txt -o sv_figure.svg -v`
**Explanation:** Run with detailed logging for debugging.

### Output statistics
**Args:** `svtopovz plot -i sv_info.txt -o sv_figure.svg --stats`
**Explanation:** Generate statistics about visualization.

### Batch processing
**Args:** `svtopovz plot -i info_files/ -o figures/`
**Explanation:** Process multiple info files together.

### Include labels
**Args:** `svtopovz plot -i sv_info.txt -o sv_figure.svg --labels`
**Explanation:** Add labels to visualization.

### Custom colors
**Args:** `svtopovz plot -i sv_info.txt -o sv_figure.svg -c colors.yaml`
**Explanation:** Use custom color scheme.

### Generate report
**Args:** `svtopovz plot -i sv_info.txt -o sv_figure.svg --report`
**Explanation:** Generate visualization with summary report.
