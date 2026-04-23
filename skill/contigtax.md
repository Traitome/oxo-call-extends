---
name: contigtax
category: assembly
description: Assign taxonomy to metagenomic contigs (previously know as tango)
tags: [contigtax, assembly]
author: oxo-call-community
source_url: "https://github.com/NBISweden/contigtax"
---

## Concepts

- **Tool Overview**: contigtax (v0.5.10) - Assign taxonomy to metagenomic contigs (previously know as tango)
- **Core Function**: Assign taxonomy to metagenomic contigs (previously know as tango)
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda contigtax`

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
