---
name: shape_it
category: alignment
description: shape_it - Shape alignment against a database of molecules
tags: ["shape_it", "alignment", "molecular-shape", "cheminformatics"]
author: oxo-call-community
source_url: "http://silicos-it.be.s3-website-eu-west-1.amazonaws.com/software/shape-it/1.0.1/shape-it.html"
---

## Concepts

- **Tool Overview**: shape_it (v1.0.1) performs shape alignment against a database of molecules.
- **Core Function**: Aligns molecular shapes for structural comparison.
- **Algorithm**: Uses shape-based alignment algorithms.
- **Input/Output**: Accepts molecular structure files and produces alignments.
- **Shape Alignment**: Focuses on comparing molecular 3D structures.
- **Applications**: Cheminformatics, drug discovery, and structural biology.

## Pitfalls

- **Memory Usage**: High memory requirements for complex structures.
- **Input Format**: Requires correct molecular structure format.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Computational Resources**: May require significant compute resources.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Align molecules
**Args:** `shape_it -i input.sdf -d database.sdf -o alignment.txt`
**Explanation:** `-i` input structure; `-d` database; `-o` output alignment.

### With options
**Args:** `shape_it -i input.sdf -d database.sdf -r RMSD -o alignment.txt`
**Explanation:** `-r RMSD` uses RMSD scoring.

### Verbose logging
**Args:** `shape_it -v -i input.sdf -d database.sdf -o alignment.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shape_it --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shape_it --version`
**Explanation:** Shows current version.

### Batch processing
**Args:** `shape_it -i structures_dir/ -d database.sdf -o results/`
**Explanation:** Processes multiple input structures.