---
name: sigprofilermatrixgenerator
category: utility
description: SigProfilerMatrixGenerator - Generates mutational matrices
tags: ["sigprofilermatrixgenerator", "utility", "mutational-matrix", "generator"]
author: oxo-call-community
source_url: "https://github.com/AlexandrovLab/SigProfilerMatrixGenerator"
---

## Concepts

- **Tool Overview**: SigProfilerMatrixGenerator (v1.3.3) generates mutational matrices from VCF files.
- **Core Function**: Creates mutational catalogs for signature analysis.
- **Algorithm**: Counts mutations by type and context.
- **Input/Output**: Accepts VCF files and produces mutation count matrices.
- **Matrix Generation**: Specialized for creating mutational spectra.
- **Applications**: Mutational signature analysis, cancer genomics research.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Reference Genome**: Requires appropriate reference genome.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on VCF quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Generate matrix
**Args:** `sigprofilermatrixgenerator -i variants.vcf -g hg38 -o matrix.txt`
**Explanation:** `-i` input VCF; `-g` genome build; `-o` output matrix.

### Multiple VCFs
**Args:** `sigprofilermatrixgenerator -i vcf_list.txt -g hg38 -o matrices/`
**Explanation:** `-i` file with list of VCFs.

### With COSMIC context
**Args:** `sigprofilermatrixgenerator -i variants.vcf -g hg38 -c -o matrix.txt`
**Explanation:** `-c` use COSMIC mutation contexts.

### Help command
**Args:** `sigprofilermatrixgenerator --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `sigprofilermatrixgenerator --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `sigprofilermatrixgenerator -v -i variants.vcf -g hg38 -o matrix.txt`
**Explanation:** `-v` verbose output.

### Threaded mode
**Args:** `sigprofilermatrixgenerator -t 8 -i variants.vcf -g hg38 -o matrix.txt`
**Explanation:** `-t 8` uses 8 threads.
