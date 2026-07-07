---
name: cansam
category: library
description: C++ binding for SAM/BAM file processing
tags: [cansam, cpp, library, sam, bam, alignment]
author: oxo-call-community
source_url: "https://github.com/jmarshall/cansam/"
---

## Concepts

- **Tool Overview**: cansam is a C++ library for reading and writing SAM/BAM alignment files.
- **Core Function**: Provides C++ API for SAM/BAM file manipulation.
- **Features**: Supports reading, writing, and indexing SAM/BAM files.
- **Application**: Building bioinformatics tools in C++.
- **Installation**: Install via bioconda: `conda install -c bioconda cansam`

## Pitfalls

- **C++ Library**: Not a command-line tool; requires C++ programming.
- **API Changes**: API may change between versions.
- **Dependencies**: Requires htslib or similar BAM library.

## Examples

### Use in C++ code
**Args:** `#include <cansam/SAM.hpp>`
**Explanation:** Include cansam header in C++ code.

### Read BAM file
**Args:** `cansam::SAMfile in("aligned.bam");`
**Explanation:** Opens BAM file for reading in C++.

### Write SAM file
**Args:** `cansam::SAMfile out("output.sam", "w");`
**Explanation:** Opens SAM file for writing in C++.