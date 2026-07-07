---
name: seqmagick
category: utility
description: seqmagick - Tools for converting and modifying sequence files
tags: ["seqmagick", "utility", "FASTA", "formatting"]
author: oxo-call-community
source_url: "http://github.com/fhcrc/seqmagick"
---

## Concepts

- **Tool Overview**: seqmagick (v0.8.6) provides tools for converting and modifying sequence files.
- **Core Function**: Converts between sequence formats and manipulates sequences.
- **Algorithm**: Implements efficient sequence parsing and transformation.
- **Input/Output**: Accepts various sequence formats and produces converted files.
- **Format Conversion**: Focuses on sequence file format conversion.
- **Applications**: Sequence data processing, format conversion, and sequence manipulation.

## Pitfalls

- **Memory Usage**: High memory requirements for large sequence files.
- **Input Format**: Requires correct input format.
- **Performance**: May be slow for extremely large files.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Convert format
**Args:** `seqmagick convert input.fasta output.fastq`
**Explanation:** Converts FASTA to FASTQ.

### Trim sequences
**Args:** `seqmagick convert --trim input.fasta output.fasta`
**Explanation:** Trims leading/trailing gaps.

### Filter by length
**Args:** `seqmagick convert --min-length 100 input.fasta output.fasta`
**Explanation:** Filters sequences >= 100bp.

### Verbose logging
**Args:** `seqmagick convert -v input.fasta output.fasta`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seqmagick --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seqmagick --version`
**Explanation:** Shows current version.

### Stats
**Args:** `seqmagick info input.fasta`
**Explanation:** Shows sequence statistics.