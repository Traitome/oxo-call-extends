---
name: blasr_libcpp
category: programming
description: Support library used by BLASR and other PacBio tools
tags: [blasr, pacbio, library, c++]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/blasr_libcpp"
---

## Concepts

- **Tool Overview**: blasr_libcpp is the C++ support library for BLASR and other PacBio tools.
- **Core Function**: Provides core data structures and algorithms for PacBio long-read alignment.
- **Components**: Sequence data structures, alignment algorithms, and file I/O.
- **Usage**: Primarily a library dependency; not typically used directly by end users.
- **Installation**: Install via bioconda: `conda install -c bioconda blasr_libcpp`

## Pitfalls

- **Library Only**: This is a support library, not a standalone tool.
- **Build Dependency**: Required for compiling BLASR from source.
- **Version Compatibility**: Must match BLASR version for proper operation.
- **C++ Runtime**: Requires compatible C++ standard library.

## Examples

### Check installation
**Args:** `pkg-config --libs blasr_libcpp`
**Explanation:** Verifies library installation and shows linker flags.

### Display version
**Args:** `pkg-config --modversion blasr_libcpp`
**Explanation:** Shows installed library version.
