---
name: purge_dups
category: assembly
description: purge_dups is a package used to purge haplotigs and overlaps in an assembly based on read depth.
tags: ["purge_dups", "assembly"]
author: oxo-call-community
source_url: "https://github.com/dfguan/purge_dups/blob/v{[ version }}/README.md"
---

## Concepts

- **Tool Overview**: purge_dups is a package used to purge haplotigs and overlaps in an assembly based on read depth. (version 1.2.6)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda purge_dups`

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

