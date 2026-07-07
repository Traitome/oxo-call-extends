---
name: ddquint
category: utility
description: Droplet Digital PCR Multiplex Analysis for chromosomal copy number detection.
tags: [ddquint, utility, ddPCR, copy-number, multiplex, chromosomal-aberrations]
author: oxo-call-community
source_url: "https://github.com/globuzzz2000/ddQuint"
---

## Concepts

- **Tool Overview**: ddquint (v0.1.0+) is a tool for analyzing multiplex droplet digital PCR (ddPCR) data to detect chromosomal copy number variations. It processes ddPCR data from multiplex reactions targeting multiple chromosomes.
- **Core Function**: Analyzes multiplex ddPCR data to determine chromosomal copy numbers, useful for detecting aneuploidies, copy number variations, and chromosomal aberrations.
- **Input/Output**: Input: ddPCR droplet data (CSV/Excel), assay configuration. Output: Copy number calls, confidence intervals, visualization plots.
- **Algorithm**: Uses Poisson statistics to calculate absolute copy numbers from droplet counts, with reference normalization for accurate CNV detection.
- **Key Features**: Multiplex analysis, reference normalization, confidence interval calculation, aneuploidy detection, visualization.
- **Installation**: `conda install -c bioconda ddquint`

## Pitfalls

- **Reference Selection**: Requires appropriate reference assays for normalization.
- **Droplet Quality**: Poor droplet generation affects accuracy.
- **Poisson Assumptions**: Assumes Poisson distribution of target molecules.
- **Multiplex Interference**: Channel bleed-through may affect multiplex accuracy.
- **Threshold Setting**: Requires proper threshold setting for positive/negative droplets.

## Examples

### Analyze multiplex ddPCR data
**Args:** `ddquint -i droplet_data.csv -c config.yaml -o results/`
**Explanation:** Analyze multiplex ddPCR data for copy number detection.

### Specify reference chromosome
**Args:** `ddquint -i droplet_data.csv -c config.yaml --ref-chr 2 -o results/`
**Explanation:** Use chromosome 2 as reference for normalization.

### Generate visualization
**Args:** `ddquint -i droplet_data.csv -c config.yaml -o results/ --plot`
**Explanation:** Generate plots showing copy number results and confidence intervals.