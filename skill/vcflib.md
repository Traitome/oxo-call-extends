---
name: vcflib
category: bioinformatics
description: vcflib - VCF manipulation library and tools.
tags: [vcflib, vcf-processing, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/vcflib/vcflib"
---

## Concepts

- **Tool Overview**: vcflib - A C++ library for parsing and manipulating VCF files.
- **Core Function**: Provides command-line utilities for VCF processing.
- **Input**: VCF file.
- **Output**: Modified VCF or derived data.
- **Installation**: Install via conda or source
- **Use Case**: VCF manipulation, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Complexity**: Many separate tools with different interfaces.

## Examples

### Filter VCF
**Args:** `vcffilter -f "QUAL > 30" input.vcf > filtered.vcf`
**Explanation:** Filter VCF by quality.

### Sort VCF
**Args:** `vcfstreamsort input.vcf > sorted.vcf`
**Explanation:** Sort VCF by position.
