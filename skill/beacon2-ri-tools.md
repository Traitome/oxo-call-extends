---
name: beacon2-ri-tools
category: population-genomics
description: Package of tools designed to simplify the population of a Beacon v2 mongoDB database
tags: [beacon2-ri-tools, population-genomics, VCF]
author: oxo-call-community
source_url: "https://github.com/EGA-archive/beacon2-ri-tools-v2/tree/main"
---

## Concepts

- **Tool Overview**: beacon2-ri-tools (v2.0.6) - Package of tools designed to simplify the population of a Beacon v2 mongoDB database
- **Core Function**: Beacon2 RI Tools v2 is a software created with the main goal of generating BFF data from .csv or .vcf (and probably more types of datafiles in the future). This is based on the first beacon ri tools. ...
- **Input/Output**: VCF variant input/output
- **Installation**: `conda install -c bioconda beacon2-ri-tools`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i genotypes.vcf -o analysis_dir`
**Explanation:** Perform population genetics analysis
