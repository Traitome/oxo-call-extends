---
name: porechop_abi
category: qc
description: Adapter inferrence and removal of Oxford Nanopore reads.
tags: ["porechop_abi", "qc"]
author: oxo-call-community
source_url: "https://github.com/bonsai-team/Porechop_ABI/blob/master/README.md"
---

## Concepts

- **Tool Overview**: Adapter inferrence and removal of Oxford Nanopore reads. (version 0.5.1)
- **Core Function**: Processes bioinformatics data related to qc
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda porechop_abi`

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

