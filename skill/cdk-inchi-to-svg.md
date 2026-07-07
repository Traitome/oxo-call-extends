---
name: cdk-inchi-to-svg
category: visualization
description: Convert InChI strings to SVG molecular structure images
tags: [cdk-inchi-to-svg, inchi, svg, molecular-visualization, chemistry]
author: oxo-call-community
source_url: "https://github.com/ipb-halle/cdk-inchi-to-svg"
---

## Concepts

- **Tool Overview**: cdk-inchi-to-svg converts InChI strings to SVG molecular structure images using CDK.
- **Core Function**: Generates 2D molecular structure diagrams from InChI identifiers.
- **Algorithm**: Uses Chemistry Development Kit (CDK) for molecular parsing and rendering.
- **Input**: InChI string or file containing InChI strings.
- **Output**: SVG image file with molecular structure.
- **Application**: Visualizing chemical structures in bioinformatics workflows.
- **Installation**: Install via bioconda: `conda install -c bioconda cdk-inchi-to-svg`

## Pitfalls

- **InChI Format**: Requires valid InChI strings.
- **Complex Molecules**: Very large molecules may produce cluttered SVG output.
- **CDK Dependencies**: Requires CDK library installation.
- **SVG Rendering**: Output may need adjustment for publication quality.

## Examples

### Convert single InChI to SVG
**Args:** `cdk-inchi-to-svg -i "InChI=1S/C6H6/c1-2-4-6-5-3-1/h1-6H" -o benzene.svg`
**Explanation:** Converts benzene InChI to SVG image.

### Batch conversion from file
**Args:** `cdk-inchi-to-svg -f inchis.txt -o output_dir/`
**Explanation:** Converts multiple InChI strings from file to SVG images.

### Set output size
**Args:** `cdk-inchi-to-svg -i "InChI=1S/H2O/h1H2" -o water.svg -w 200 -h 200`
**Explanation:** Creates 200x200 pixel SVG image.

### Display help
**Args:** `cdk-inchi-to-svg --help`
**Explanation:** Shows all available options and usage information.