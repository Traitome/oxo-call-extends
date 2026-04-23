---
name: fragpipe
category: utility
description: Pipeline for comprehensive analysis of shotgun proteomics data
tags: [fragpipe, utility]
author: oxo-call-community
source_url: "https://github.com/Nesvilab/FragPipe"
---

## Concepts
- **Tool Overview**: FragPipe is a Java Graphical User Interface (GUI) for a suite of computational tools enabling comprehensive analysis of mass spectrometry-based proteomics data. It is powered by MSFragger - an ultrafast proteomic search engine suitable for both conventional and "open" (wide precursor mass tolerance) peptide identification. FragPipe includes the Philosopher toolkit for downstream post-processing of MSFragger search results (PeptideProphet, iProphet, ProteinProphet), FDR filtering, label-based quantification, and multi-experiment summary report generation. Crystal-C and PTM-Shepherd are included to aid interpretation of open search results. Also included in FragPipe binary are TMT-Integrator for TMT/iTRAQ isobaric labeling-based quantification, IonQuant for label-free quantification with match-between-run (MBR) functionality, spectral library building with EasyPQP, and MSFragger-DIA and DIA-Umpire SE modules for direct analysis of data independent acquisition (DIA) data.
- **Core Function**: Pipeline for comprehensive analysis of shotgun proteomics data
- **Input/Output**: Depends on tool configuration and data formats.
- **Installation**: `conda install -c bioconda fragpipe`

## Pitfalls
- **Version**: Options may vary between versions.

## Examples
### Help
**Args:** `--help`
**Explanation:** Shows available options.
