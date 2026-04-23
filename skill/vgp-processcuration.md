---
name: vgp-processcuration
category: alignment
description: ProcessCurated - Toolkit for processing manually curated genome assemblies
tags: [vgp-processcuration, alignment]
author: oxo-call-community
source_url: "https://github.com/vgl-hub/vgl-curation/blob/postcuration_1.0/README.md"
---

## Concepts

- **Tool Overview**: vgp-processcuration (v1.1) - ProcessCurated is a toolkit for processing manually curated genome assemblies. It reconciles AGP files manually curated in PretextView to rename, reorient, and sort assemblies in preparation for submission. The tool performs three main operations: correcting and splitting AGP files while assigning unlocalized sequences, assigning chromosome names to scaffolds, and reorienting and renaming sequences based on MashMap alignment data.
- **Core Function**: ProcessCurated - Toolkit for processing manually curated genome assemblies
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vgp-processcuration`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
