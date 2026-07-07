---
name: sigmut
category: utility
description: sigmut - Wrapper for SigProfiler mutational signature analysis
tags: ["sigmut", "utility", "mutational-signature", "sigprofiler"]
author: oxo-call-community
source_url: "https://github.com/artbio/sigmut"
---

## Concepts

- **Tool Overview**: sigmut (v1.0) is a wrapper for SigProfiler mutational signature analysis.
- **Core Function**: Identifies mutational signatures from sequencing data.
- **Algorithm**: Uses non-negative matrix factorization for signature extraction.
- **Input/Output**: Accepts VCF/MAF files and produces signature profiles.
- **Mutational Signatures**: Specialized for identifying mutational processes.
- **Applications**: Cancer genomics, mutational signature analysis, and evolutionary studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **SigProfiler Dependency**: Requires SigProfiler installation.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on mutation calling quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Extract signatures
**Args:** `sigmut -i mutations.maf -o signatures/`
**Explanation:** `-i` input MAF file; `-o` output directory.

### With VCF input
**Args:** `sigmut -i variants.vcf -g hg38 -o signatures/`
**Explanation:** `-g` genome build.

### With signature number
**Args:** `sigmut -i mutations.maf -n 5 -o signatures/`
**Explanation:** `-n 5` number of signatures to extract.

### Help command
**Args:** `sigmut --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sigmut --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sigmut -v -i mutations.maf -o signatures/`
**Explanation:** `-v` verbose output.

### Plot signatures
**Args:** `sigmut -i mutations.maf -p -o plots/`
**Explanation:** `-p` generate plots.
