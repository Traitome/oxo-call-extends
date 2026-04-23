---
name: ptgaul
category: assembly
description: Plastid Genome Assembly Using long-read data (ptGAUL)
tags: ["ptgaul", "assembly"]
author: oxo-call-community
source_url: "https://github.com/Bean061/ptgaul"
---

## Concepts

- **Tool Overview**: Plastid Genome Assembly Using long-read data (ptGAUL) (version 1.0.5)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda ptgaul`

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

