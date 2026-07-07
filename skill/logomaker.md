---
name: logomaker
category: visualization
description: logomaker - Python package for creating sequence logos
tags: [logomaker, visualization, sequence-logo, python, bioinformatics]
author: oxo-call-community
source_url: "http://logomaker.readthedocs.io"
---

## Concepts

- **Sequence Logos**: Visual representation of sequence alignments
- **Python Package**: Python-based logo generation
- **Information Content**: Shows information content at each position
- **Multiple Formats**: Supports various input/output formats
- **Customization**: High degree of logo customization
- **Publication Quality**: Publication-quality figures

## Pitfalls

- **Alignment Quality**: Poor quality alignments affect logos
- **Memory Usage**: Memory-intensive for large alignments
- **Customization Complexity**: May require significant customization
- **Dependency Management**: Requires proper dependency management
- **Output Format**: Limited output formats available
- **Performance**: May be slow for large datasets

## Examples

### Create logo from matrix
**Args:** `import logomaker; logo = logomaker.Logo(matrix); logo.ax.set_title('Sequence Logo')`
**Explanation:** Creates sequence logo from matrix.

### Save logo
**Args:** `logo.savefig('logo.png', dpi=300)`
**Explanation:** Saves logo to PNG file.

### Custom colors
**Args:** `logo = logomaker.Logo(matrix, color_scheme='classic')`
**Explanation:** Uses classic color scheme.

### Logo size
**Args:** `logo.style_spines(visible=False); logo.style_xticks(rotation=90)`
**Explanation:** Customizes logo appearance.

### Information content
**Args:** `logo = logomaker.Logo(matrix, width_per_position=0.8)`
**Explanation:** Sets custom width per position.

### Stacked logo
**Args:** `logo = logomaker.Logo(matrix, stack_order='biggest_on_top')`
**Explanation:** Stacks letters by size.