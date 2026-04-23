---
name: bpp-core
category: programming
description: Bio++ core C++ libraries for bioinformatics
tags: [bio++, cpp, library, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/BioPP/bpp-core"
---

## Concepts

- **Tool Overview**: bpp-core is the core library of the Bio++ C++ libraries for bioinformatics.
- **Core Function**: Provides foundational data structures, algorithms, and utilities for Bio++ tools.
- **Components**: Sequence handling, tree structures, numerical optimization, and statistical tools.
- **Usage**: Library dependency for other Bio++ packages (bpp-seq, bpp-phyl, bpp-popgen).
- **Installation**: Install via bioconda: `conda install -c bioconda bpp-core`

## Pitfalls

- **Library Only**: This is a C++ library, not a standalone command-line tool.
- **C++ Runtime**: Requires compatible C++ standard library.
- **Version Compatibility**: Must match versions with other Bio++ packages.
- **Compilation**: Required for building Bio++-based applications.

## Examples

### Check installation
**Args:** `pkg-config --libs bpp-core`
**Explanation:** Verifies library installation and shows linker flags.

### Display version
**Args:** `pkg-config --modversion bpp-core`
**Explanation:** Shows installed library version.
