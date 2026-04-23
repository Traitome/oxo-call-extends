---
name: asqcan
category: assembly
description: A combined pipeline for bacterial genome assembly, quality control and annotation
tags: [asqcan, assembly]
author: oxo-call-community
source_url: "https://github.com/bogemad/asqcan"
---

## Concepts

- **Tool Overview**: asqcan (v0.4) - A combined pipeline for bacterial genome assembly, quality control and annotation
- **Core Function**: A combined pipeline for bacterial genome assembly, quality control and annotation
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda asqcan`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i reads.fastq -o assembly_dir`
**Explanation:** Assemble reads into contigs
