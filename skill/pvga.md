---
name: pvga
category: assembly
description: PVGA is a powerful virus-focused assembler that does both assembly and polishing.
tags: ["pvga", "assembly"]
author: oxo-call-community
source_url: "https://github.com/SoSongzhi/PVGA"
---

## Concepts

- **Tool Overview**: PVGA is a powerful virus-focused assembler that does both assembly and polishing. (version 0.1.2)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pvga`

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

