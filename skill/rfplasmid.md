---
name: rfplasmid
category: assembly
description: RFPlasmid predicts plasmid contigs from assemblies using single copy marker genes, plasmid genes, and kmers.
tags: ["rfplasmid", "assembly"]
author: oxo-call-community
source_url: "https://github.com/aldertzomer/RFPlasmid"
---

## Concepts

- **Tool Overview**: RFPlasmid predicts plasmid contigs from assemblies using single copy marker genes, plasmid genes, and kmers. (version 0.0.18)
- **Core Function**: Processes bioinformatics data related to assembly
- **Input/Output**: Standard bioinformatics formats
- **Installation**: `conda install -c bioconda rfplasmid`

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

