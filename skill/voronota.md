---
name: voronota
category: qc
description: Compute Voronoi diagram vertices for macromolecular structures
tags: [voronota, qc]
author: oxo-call-community
source_url: "https://www.voronota.com/"
---

## Concepts

- **Tool Overview**: voronota (v1.29.4771) - The analysis of macromolecular structures often requires a comprehensive definition of atomic neighborhoods. Such a definition can be based on the Voronoi diagram of balls, where each ball represents an atom of some van der Waals radius. Voronota is a software tool for finding all the vertices of the Voronoi diagram of balls. Such vertices correspond to the centers of the empty tangent spheres defined by quadruples of balls. Voronota is especially suitable for processing three-dimensional structures of biological macromolecules such as proteins and RNA.  Since version 1.2 Voronota also uses the Voronoi vertices to construct inter-atom contact surfaces and solvent accessible surfaces. Voronota provides tools to query contacts, generate contacts graphics, compare contacts and evaluate quality of protein structural models using contacts.  Most of the new developments are happening in the expansions of Voronota: Voronota-JS, Voronota-LT and Voronota-GL.  Voronota and its expansions are developed by Kliment Olechnovic (https://www.kliment.lt).
- **Core Function**: Compute Voronoi diagram vertices for macromolecular structures
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda voronota`

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
