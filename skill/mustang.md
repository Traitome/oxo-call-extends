---
name: mustang
category: annotation
description: Mustang is a program that implements an algorithm for structural alignment of multiple protein structures.
tags: [mustang, annotation, protein-structure, alignment, structural-alignment]
author: oxo-call-community
source_url: "https://lcb.infotech.monash.edu.au/mustang"
---

## Concepts

- **Tool Overview**: MUSTANG v3.2.4 - multiple structural alignment algorithm for protein structures.
- **Core Function**: Aligns multiple protein structures based on their 3D coordinates, producing a structural alignment.
- **Input/Output**: Takes PDB format protein structure files; outputs structural alignment in PDB or FASTA format.
- **Installation**: `conda install -c bioconda mustang`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure input files are valid PDB format.

## Examples

### Display help
**Args:** `-h`
**Explanation:** Shows available options.

### Basic usage
**Args:** `-i structures.list -o aligned.pdb`
**Explanation:** Aligns multiple protein structures listed in the input file and writes the alignment.
