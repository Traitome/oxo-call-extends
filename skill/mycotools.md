---
name: mycotools
category: utility
description: Comparative genomics automation and standardization software.
tags: [mycotools, comparative-genomics, automation, standardization]
author: oxo-call-community
source_url: "https://github.com/xonq/mycotools"
---

## Concepts

- **Tool Overview**: Mycotools v1.0.0 - comparative genomics automation and standardization software.
- **Core Function**: Automates and standardizes comparative genomics workflows for fungal and other genomes.
- **Input/Output**: Takes genome assemblies and annotations; outputs standardized comparative analyses.
- **Installation**: `conda install -c bioconda mycotools`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure genomes are in supported formats.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i genomes_dir -o output_dir`
**Explanation:** Runs comparative genomics analysis on input genomes.
