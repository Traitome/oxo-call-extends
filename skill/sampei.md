---
name: sampei
category: qc
description: SAMPEI, a searching method leveraging high quality query spectra within the same or different dataset to assign target spectra with peptide sequence and undefined modification (mass shift)
tags: ["sampei", "qc", "sam"]
author: oxo-call-community
source_url: "https://github.com/FenyoLab/SAMPEI"
---

## Concepts

- **Tool Overview**: SAMPEI, a searching method leveraging high quality query spectra within the same or different dataset to assign target spectra with peptide sequence and undefined modification (mass shift) (version 0.0.9)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda sampei`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Quality check
**Args:** `-i input.fastq -o qc_report`
**Explanation:** Generates quality control metrics and reports.

