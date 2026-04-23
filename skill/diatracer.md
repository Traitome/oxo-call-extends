---
name: diatracer
category: annotation
description: A diaPASEF spectrum-centric analysis tool for DIA proteomics data.
tags: [diatracer, annotation, proteomics, dia-pasef, spectrum-centric]
author: oxo-call-community
source_url: "https://diatracer.nesvilab.org/"
---

## Concepts

- **Tool Overview**: diaTracer v1.2.5 - Spectrum-centric analysis tool for Bruker diaPASEF DIA proteomics data.
- **Core Function**: Enables spectral-library-free peptide identification and quantification from diaPASEF data.
- **Input/Output**: Expects Bruker diaPASEF data; outputs peptide identifications and quantifications.
- **Installation**: `conda install -c bioconda diatracer`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Licensing**: Available for academic research and educational purposes only.
- **Input Format**: Requires Bruker diaPASEF format data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `diatracer --input sample.d --output results/`
**Explanation:** Performs spectrum-centric analysis on diaPASEF data.
