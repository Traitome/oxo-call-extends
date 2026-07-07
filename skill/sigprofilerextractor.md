---
name: sigprofilerextractor
category: utility
description: SigProfilerExtractor - Extracts mutational signatures from catalogues
tags: ["sigprofilerextractor", "utility", "mutational-signature", "extraction"]
author: oxo-call-community
source_url: "https://github.com/AlexandrovLab/SigProfilerExtractor"
---

## Concepts

- **Tool Overview**: SigProfilerExtractor (v1.2.6) extracts mutational signatures from catalogs.
- **Core Function**: Identifies novel mutational signatures from mutation data.
- **Algorithm**: Uses non-negative matrix factorization for signature extraction.
- **Input/Output**: Accepts VCF/MAF files and produces signature profiles.
- **Signature Discovery**: Specialized for de novo signature identification.
- **Applications**: Cancer genomics, mutational process characterization.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Parameter Tuning**: Requires careful adjustment of signature number.
- **Input Quality**: Results depend on mutation calling quality.
- **Computational Resources**: May require significant compute resources.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Extract signatures
**Args:** `sigprofilerextractor -i mutations.maf -o signatures/`
**Explanation:** `-i` input MAF file; `-o` output directory.

### With signature number
**Args:** `sigprofilerextractor -i mutations.maf -n 5 -o signatures/`
**Explanation:** `-n 5` extract 5 signatures.

### With COSMIC signatures
**Args:** `sigprofilerextractor -i mutations.maf -c -o signatures/`
**Explanation:** `-c` use COSMIC reference signatures.

### Help command
**Args:** `sigprofilerextractor --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sigprofilerextractor --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sigprofilerextractor -v -i mutations.maf -o signatures/`
**Explanation:** `-v` verbose output.

### Bootstrap mode
**Args:** `sigprofilerextractor -i mutations.maf -b -o signatures/`
**Explanation:** `-b` enable bootstrap analysis.
