---
name: bpp-seq
category: programming
description: Bio++ C++ library for sequence analysis
tags: [bio++, sequence, cpp, library, alignment]
author: oxo-call-community
source_url: "https://github.com/BioPP/bpp-seq"
---

## Concepts

- **Tool Overview**: bpp-seq provides sequence analysis functionality as part of the Bio++ C++ library suite.
- **Core Function**: Sequence data structures, alignment handling, and file I/O.
- **Features**: FASTA/GenBank parsing, sequence manipulation, and alphabet handling.
- **Dependencies**: Requires bpp-core library.
- **Installation**: Install via bioconda: `conda install -c bioconda bpp-seq`

## Pitfalls

- **Library Only**: C++ library, not a standalone command-line tool.
- **Dependencies**: Requires bpp-core to be installed.
- **Version Matching**: Must use compatible versions of all Bio++ packages.

## Examples

### Check installation
**Args:** `pkg-config --libs bpp-seq`
**Explanation:** Verifies library installation and shows linker flags.

### Display version
**Args:** `pkg-config --modversion bpp-seq`
**Explanation:** Shows installed library version.
