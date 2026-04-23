---
name: libarbdb
category: alignment
description: ARB 6 Sequence Analysis Suite
tags: [libarbdb, alignment, alignment]
author: oxo-call-community
source_url: "http://www.arb-home.de"
---

## Concepts

- **Tool Overview**: libarbdb v6.0.6 - "ARB (ARBor, Latin: tree): A software environment for maintaining databases of molecular sequences and additional information, and for analyzing the sequence data, with emphasis on phylogeny reconstruction.  The programs have primarily been developed for ribosomal ribonucleic acid (rRNA) sequences and, therefore, contain special tools for alignment and analysis of these structures. However, other molecular sequence data can also be handled. Protein gene sequences and predicted protein primary structures as well as protein secondary structures can be stored in the same database.  The ARB package is designed for graphical user interface. Program control and data display are available in a hierarchical set of windows and subwindows. The majority of operations can be controlled using the mouse for moving the pointer and the left mouse button for initiating and performing operations".
- **Core Function**: ARB 6 Sequence Analysis Suite
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda libarbdb`

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
