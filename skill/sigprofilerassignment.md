---
name: sigprofilerassignment
category: variant-analysis
description: SigProfilerAssignment - Assignment of mutational signatures to samples and mutations
tags: ["sigprofilerassignment", "variant-analysis", "mutational-signature", "assignment"]
author: oxo-call-community
source_url: "https://github.com/AlexandrovLab/SigProfilerAssignment"
---

## Concepts

- **Tool Overview**: SigProfilerAssignment (v1.1.3) assigns known mutational signatures to samples and mutations.
- **Core Function**: Decomposes mutation catalogs into known mutational signatures.
- **Algorithm**: Uses non-negative least squares for signature assignment.
- **Input/Output**: Accepts VCF/MAF files and produces signature attribution results.
- **Signature Analysis**: Specialized for mutational signature decomposition.
- **Applications**: Cancer genomics, mutational signature research, and precision medicine.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Signature Database**: Requires comprehensive signature database.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on mutation calling quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Assign signatures
**Args:** `sigprofilerassignment -i mutations.maf -o assignment_results/`
**Explanation:** `-i` input MAF file; `-o` output directory.

### With signature database
**Args:** `sigprofilerassignment -i mutations.maf -d signatures.db -o results/`
**Explanation:** `-d` signature database file.

### Per-mutation assignment
**Args:** `sigprofilerassignment -i mutations.maf -m -o results/`
**Explanation:** `-m` assign signatures to individual mutations.

### Help command
**Args:** `sigprofilerassignment --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sigprofilerassignment --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sigprofilerassignment -v -i mutations.maf -o results/`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sigprofilerassignment -t 8 -i mutations.maf -o results/`
**Explanation:** `-t 8` uses 8 threads.
