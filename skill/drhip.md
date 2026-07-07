---
name: drhip
category: utility
description: "DRHIP - Data Reduction for HyPhy with Inference Processing"
tags: [drhip, utility, HyPhy, evolutionary-analysis, selection-analysis]
author: oxo-call-community
source_url: "https://github.com/veg/drhip"
---

## Concepts

- **Tool Overview**: DRHIP is a Python package for analyzing and summarizing results from HyPhy evolutionary selection analyses.
- **Core Function**: Processes outputs from BUSTED, RELAX, MEME, and other HyPhy methods to generate summary statistics.
- **Input/Output**: Input: HyPhy analysis outputs. Output: Summary statistics, site-specific analyses, visualizations.
- **Algorithm**: Parses HyPhy JSON outputs and computes aggregated statistics.
- **Key Features**: Supports multiple HyPhy methods, generates publication-ready figures, batch processing.
- **Installation**: `conda install -c bioconda drhip`

## Pitfalls

- **Output Format**: Ensure HyPhy outputs are in compatible JSON format.
- **Version Compatibility**: Different HyPhy versions may produce different output formats.
- **Multiple Tests**: Correct for multiple hypothesis testing when analyzing many sites.
- **Alignment Quality**: Poor sequence alignment can affect selection inference results.
- **Model Assumptions**: Understand the assumptions of each HyPhy method used.

## Examples

### Process BUSTED results
**Args:** `--input busted_output.json --output summary.txt --method BUSTED`
**Explanation:** Processes BUSTED output and generates summary statistics.

### Multiple files
**Args:** `--input-dir hyphy_results/ --output summary.txt`
**Explanation:** Processes all HyPhy output files in a directory.

### Generate visualization
**Args:** `--input busted_output.json --output plot.png --plot`
**Explanation:** Creates visualization of selection analysis results.

### Site-specific analysis
**Args:** `--input meme_output.json --output sites.txt --sites`
**Explanation:** Extracts site-specific selection results from MEME output.

### Compare methods
**Args:** `--input busted.json relax.json --output comparison.txt --compare`
**Explanation:** Compares results from different HyPhy methods.