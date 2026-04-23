---
name: masurca
category: assembly
description: MaSuRCA (Maryland Super-Read Celera Assembler) genome assembly software.
tags: [masurca, assembly]
author: oxo-call-community
source_url: "https://masurca.blogspot.co.uk"
---

## Concepts

- **Tool Overview**: masurca v4.1.4 - MaSuRCA (Maryland Super-Read Celera Assembler) genome assembly software. MaSuRCA requires Illumina data, and supports third-generation PacBio/Nanopore MinION reads for hybrid assembly..
- **Core Function**: MaSuRCA (Maryland Super-Read Celera Assembler) genome assembly software.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda masurca`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Assemble genome
**Args:** `masurca config.txt`
**Explanation:** Runs MaSuRCA assembler with configuration file.

