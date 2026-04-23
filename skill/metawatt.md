---
name: metawatt
category: alignment
description: MetaWatt is a metagenomic binning tool
tags: [metawatt, alignment, sequence]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/metawatt/"
---

## Concepts

- **Tool Overview**: metawatt v3.5.3 - The Metawatt binner is a graphical binning tool that makes use of multivariate statistics of tetranucleotide frequencies and differential coverage based binning. It also performs taxonomic assessment of binning quality (via diamond BLASTx). Created bins can be edited and exported as fasta. The Metawatt is implemented in Java SWING and minimally depends on Diamond, HMMer3.1, BBMap, Prodigal and the Batik library for the export of SVG graphics..
- **Core Function**: MetaWatt is a metagenomic binning tool
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda metawatt`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Basic usage
**Args:** `<input_file>`
**Explanation:** Process input file with default parameters.
