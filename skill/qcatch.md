---
name: qcatch
category: qc
description: QCatch: Quality Control downstream of alevin-fry / simpleaf.
tags: ["qcatch", "qc"]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/QCatch"
---

## Concepts

- **Tool Overview**: QCatch: Quality Control downstream of alevin-fry / simpleaf. (version 0.2.11)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda qcatch`

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

