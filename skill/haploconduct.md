---
name: haploconduct
category: utility
description: HaploConduct is a package designed for reconstruction of individual haplotypes from next generation sequencing data, in particular Illumina. It provides two methods, SAVAGE and POLYTE, which can be run through the haploconduct wrapper.
tags: [haploconduct, utility]
author: oxo-call-community
source_url: "https://github.com/HaploConduct/HaploConduct"
---

## Concepts

- **Tool Overview**: haploconduct (v0.2.1) - HaploConduct is a package designed for reconstruction of individual haplotypes from next generation sequencing data, in particular Illumina. It provides two methods, SAVAGE and POLYTE, which can be run through the haploconduct wrapper.
- **Core Function**: Provides functionality for utility tasks.
- **Input/Output**: Standard bioinformatics formats supported.
- **Installation**: `conda install -c bioconda haploconduct`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Process input file and generate output.
