---
name: bpp-popgen
category: programming
description: Bio++ C++ library for population genetics analysis
tags: [bio++, population-genetics, cpp, library]
author: oxo-call-community
source_url: "https://github.com/BioPP/bpp-popgen"
---

## Concepts

- **Tool Overview**: bpp-popgen provides population genetics analysis tools as part of the Bio++ C++ library suite.
- **Core Function**: Population genetics statistics, diversity measures, and coalescent simulations.
- **Features**: Nucleotide diversity, F-statistics, and demographic inference.
- **Dependencies**: Requires bpp-core and bpp-seq libraries.
- **Installation**: Install via bioconda: `conda install -c bioconda bpp-popgen`

## Pitfalls

- **Library Only**: C++ library, not a standalone command-line tool.
- **Dependencies**: Requires bpp-core and bpp-seq to be installed.
- **Version Matching**: Must use compatible versions of all Bio++ packages.

## Examples

### Check installation
**Args:** `pkg-config --libs bpp-popgen`
**Explanation:** Verifies library installation and shows linker flags.

### Display version
**Args:** `pkg-config --modversion bpp-popgen`
**Explanation:** Shows installed library version.
