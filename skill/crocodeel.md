---
name: crocodeel
category: metagenomics
description: CroCoDeEL is a tool that detects cross-sample contamination in shotgun metagenomic data
tags: [crocodeel, metagenomics, SAM]
author: oxo-call-community
source_url: "https://github.com/metagenopolis/crocodeel"
---

## Concepts

- **Tool Overview**: crocodeel (v1.2.1) - CroCoDeEL is a tool that detects cross-sample contamination in shotgun metagenomic data
- **Core Function**: CroCoDeEL is a tool that detects cross-sample (aka well-to-well) contamination in shotgun metagenomic data. It accurately identifies contaminated samples but also pinpoints contamination sources and e...
- **Input/Output**: BAM/SAM alignment input/output
- **Installation**: `conda install -c bioconda crocodeel`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i contigs.fasta -o bins_dir`
**Explanation:** Perform metagenomic analysis
