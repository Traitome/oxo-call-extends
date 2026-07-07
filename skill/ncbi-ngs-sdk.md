---
name: ncbi-ngs-sdk
category: alignment
description: NCBI NGS SDK provides a domain-specific API for accessing reads, alignments and pileups from Next Generation Sequencing data.
tags: [ncbi-ngs-sdk, alignment, ngs, sequencing, api]
author: oxo-call-community
source_url: "https://github.com/ncbi/ngs"
---

## Concepts

- **Tool Overview**: NCBI NGS SDK is a software development kit for accessing next-generation sequencing data.
- **Core Function**: Provides a unified API for reading sequencing reads, alignments, and pileups from various formats.
- **Algorithm**: Implements efficient parsing and indexing of sequencing data for fast access.
- **Input Format**: Supports BAM, FASTQ, SAM, and other common sequencing data formats.
- **Output**: Provides programmatic access to sequencing data through C++ and Java APIs.
- **Use Case**: Developing bioinformatics tools, accessing sequencing data programmatically, pipeline integration.

## Pitfalls

- **API Complexity**: Requires understanding of the NGS API structure.
- **Version Compatibility**: API may change between versions.
- **Build Requirements**: May require compilation from source.
- **Memory Usage**: Can consume significant memory for large datasets.
- **Platform Specific**: Some features may be platform-specific.
- **Documentation**: Requires careful reading of API documentation.

## Examples

### Display help
**Args:** `ngs-tools --help`
**Explanation:** Shows available options and usage instructions.

### Basic API usage (C++)
**Args:** `#include <ngs/ReadCollection.hpp>`
**Explanation:** Includes NGS SDK header for C++ development.

### Basic API usage (Java)
**Args:** `import gov.nih.nlm.ncbi.ngs.NGS;`
**Explanation:** Imports NGS SDK package for Java development.

### Open read collection
**Args:** `ReadCollection run = NGS.openReadCollection("reads.bam");`
**Explanation:** Opens BAM file for read access.

### Get read count
**Args:** `long count = run.getReadCount();`
**Explanation:** Returns total number of reads in collection.

### Iterate reads
**Args:** `for (ReadIterator it = run.getReads(); it.hasNext(); )`
**Explanation:** Iterates through reads in collection.