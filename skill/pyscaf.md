---
name: pyscaf
category: assembly
description: Genome assembly scaffolding using information from paired-end/mate-pair libraries, long reads, and synteny to closely related species.
tags: ["pyscaf", "assembly"]
author: oxo-call-community
source_url: "https://github.com/lpryszcz/pyScaf"
---

## Concepts

- **Tool Overview**: Genome assembly scaffolding using information from paired-end/mate-pair libraries, long reads, and synteny to closely related species. (version 0.12a4)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda pyscaf`

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

