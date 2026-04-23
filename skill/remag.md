---
name: remag
category: assembly
description: Recovery of high-quality eukaryotic genomes from complex metagenomes
tags: ["remag", "assembly", "sam", "bed"]
author: oxo-call-community
source_url: "https://github.com/danielzmbp/remag"
---

## Concepts

- **Tool Overview**: Recovery of high-quality eukaryotic genomes from complex metagenomes (version 0.4.2)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda remag`

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

