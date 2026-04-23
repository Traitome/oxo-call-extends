---
name: racon
category: assembly
description: Ultrafast consensus module for raw de novo genome assembly of long uncorrected reads.
tags: ["racon", "assembly"]
author: oxo-call-community
source_url: "https://github.com/lbcb-sci/racon/blob/1.5.0/README.md"
---

## Concepts

- **Tool Overview**: Ultrafast consensus module for raw de novo genome assembly of long uncorrected reads. (version 1.5.0)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda racon`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Run assembly
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assembles reads into contigs/scaffolds.

