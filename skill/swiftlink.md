---
name: swiftlink
category: population-genomics
description: A multipoint parametric linkage analysis tool for large consanguineous pedigrees and is primarily targeted at pedigrees that cannot be analysed by a Lander-Green algorithm based program, i.e. many markers, but larger pedigrees.
tags: [swiftlink, population-genomics]
author: oxo-call-community
source_url: "https://github.com/ajm/swiftlink"
---

## Concepts

- **Tool Overview**: swiftlink (v1.0) - A multipoint parametric linkage analysis tool for large consanguineous pedigrees and is primarily targeted at pedigrees that cannot be analysed by a Lander-Green algorithm based program, i.e. many markers, but larger pedigrees.
- **Core Function**: A multipoint parametric linkage analysis tool for large consanguineous pedigrees and is primarily targeted at pedigrees that cannot be analysed by a Lander-Green algorithm based program, i.e. many markers, but larger pedigrees.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda swiftlink`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `swiftlink -i <input.vcf> -o <output_dir>`
**Explanation:** Run swiftlink with typical input and output options.
