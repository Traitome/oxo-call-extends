---
name: imctools
category: formatting
description: An Image Mass Cytometry (IMC) file conversion tool that aims to convert IMC rawfiles (.mcd, .txt) into an intermediary ome.tiff, containing all the relevant metadata. Further it contains tools to generate simpler tiff files that can be directly be used as input files for e.g. CellProfiller, Ilastik, Fiji etc
tags: [imctools, formatting]
author: oxo-call-community
source_url: "https://github.com/BodenmillerGroup/imctools/blob/master/README.md"
---

## Concepts

- **Tool Overview**: imctools (v2.1.8) - An Image Mass Cytometry (IMC) file conversion tool that aims to convert IMC rawfiles (.mcd, .txt) into an intermediary ome.tiff, containing all the relevant metadata. Further it contains tools to generate simpler tiff files that can be directly be used as input files for e.g. CellProfiller, Ilastik, Fiji etc
- **Core Function**: Provides functionality for formatting tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda imctools`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
