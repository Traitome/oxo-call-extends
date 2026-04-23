---
name: proteomiqon-peptidespectrummatching
category: formatting
description: Given raw an MS run in the mzLite format, this tool iterates across all MS/MS scans, determines precursor charge states and possible peptide spectrum matches using reimplementations of SEQUEST, Andromeda and XTandem.
tags: ["proteomiqon-peptidespectrummatching", "formatting"]
author: oxo-call-community
source_url: "https://csbiology.github.io/ProteomIQon/tools/PeptideSpectrumMatching.html"
---

## Concepts

- **Tool Overview**: Given raw an MS run in the mzLite format, this tool iterates across all MS/MS scans, determines precursor charge states and possible peptide spectrum matches using reimplementations of SEQUEST, Andromeda and XTandem. (version 0.0.7)
- **Core Function**: Processes bioinformatics data related to formatting
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda proteomiqon-peptidespectrummatching`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Convert format
**Args:** `-i input.file -o output.file`
**Explanation:** Converts between file formats.

