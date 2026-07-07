---
name: colorbrewer
category: programming
description: Access ColorBrewer color schemes from Python programs
tags: [colorbrewer, python, visualization, color-schemes, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/hoffmangroup/colorbrewer"
---

## Concepts

- **Tool Overview**: colorbrewer is a Python package that provides easy access to ColorBrewer color schemes for data visualization in scientific applications.
- **Core Function**: Provides programmatic access to ColorBrewer's carefully designed color palettes optimized for scientific visualization.
- **Algorithm**: Implements ColorBrewer color scheme definitions with validation and accessibility features.
- **Input**: Color scheme names and parameters.
- **Output**: Color values in various formats (RGB, hex, etc.).
- **Application**: Data visualization, plotting, and scientific figure generation.
- **Installation**: Install via bioconda: `conda install -c bioconda colorbrewer`

## Pitfalls

- **Color Blindness**: Some schemes are not colorblind-friendly.
- **Print Quality**: Some schemes optimized for screens may not print well.
- **Scheme Selection**: Must choose appropriate scheme type (sequential, diverging, qualitative).
- **Number of Colors**: Each scheme has specific number of colors available.
- **License**: ColorBrewer schemes have specific usage restrictions.

## Examples

### Get color scheme
**Args:** `python -c "from colorbrewer import get_scheme; colors = get_scheme('Blues', 5)"`
**Explanation:** Retrieves 5-color Blues sequential scheme.

### Get all schemes
**Args:** `python -c "from colorbrewer import all_schemes; print(all_schemes.keys())"`
**Explanation:** Lists all available ColorBrewer schemes.

### Export to file
**Args:** `python -c "from colorbrewer import export; export(' Reds', 7, 'colors.txt')"`
**Explanation:** Exports 7-color Reds scheme to text file.

### Display help
**Args:** `python -c "import colorbrewer; help(colorbrewer)"`
**Explanation:** Shows available functions and documentation.