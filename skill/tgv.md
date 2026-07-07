---
name: tgv
category: visualization
description: TGV - Tool for genomic visualization with focus on structural variants.
tags: [tgv, visualization, structural-variant, genomic, svg, display]
author: oxo-call-community
source_url: "https://github.com/genome-tools/tgv"
---

## Concepts

- **Tool Overview**: TGV (Tool for Genomic Visualization) - A visualization tool specialized for displaying genomic data with emphasis on structural variants.
- **Core Function**: Creates publication-quality visualizations of genomic regions, alignments, and structural variants.
- **Input**: VCF files, BAM alignments, genome annotation files.
- **Output**: Vector graphics (SVG) or raster images showing genomic data.
- **Installation**: `pip install tgv` or `conda install -c bioconda tgv`
- **Use Case**: Visualizing structural variants, comparing genomic regions, publication figures.

## Pitfalls

- **Large Regions**: Very large genomic regions may require subsampling for visualization.
- **Customization**: Complex visualizations may require detailed configuration.

## Examples

### Visualize genomic region
**Args:** `tgv region -c chr1:1000000-2000000 -g genome.fasta -o region.svg`
**Explanation:** Visualize a specific genomic region.

### Display structural variants
**Args:** `tgv sv -v variants.vcf -g genome.fasta -o sv_display.svg`
**Explanation:** Visualize structural variants from VCF file.
