---
name: bpp-phyl
category: programming
description: Bio++ C++ library for phylogenetic analysis
tags: [bio++, phylogenetics, cpp, library, tree]
author: oxo-call-community
source_url: "https://github.com/BioPP/bpp-phyl"
---

## Concepts

- **Tool Overview**: bpp-phyl provides phylogenetic analysis algorithms as part of the Bio++ C++ library suite.
- **Core Function**: Maximum likelihood, Bayesian, and distance-based phylogenetic methods.
- **Features**: Tree likelihood computation, model optimization, and ancestral state reconstruction.
- **Dependencies**: Requires bpp-core and bpp-seq libraries.
- **Installation**: Install via bioconda: `conda install -c bioconda bpp-phyl`

## Pitfalls

- **Library Only**: C++ library, not a standalone command-line tool.
- **Dependencies**: Requires bpp-core and bpp-seq to be installed.
- **Version Matching**: Must use compatible versions of all Bio++ packages.

## Examples

### Check installation
**Args:** `pkg-config --libs bpp-phyl`
**Explanation:** Verifies library installation and shows linker flags.

### Display version
**Args:** `pkg-config --modversion bpp-phyl`
**Explanation:** Shows installed library version.
