---
name: simple_sv_annotation
category: variant-analysis
description: simple_sv_annotation - Simplify snpEff annotations
tags: ["simple_sv_annotation", "variant-analysis", "annotation", "snpeff"]
author: oxo-call-community
source_url: "https://github.com/AstraZeneca-NGS/simple_sv_annotation"
---

## Concepts

- **Tool Overview**: simple_sv_annotation (v2019.02.18) simplifies snpEff annotations.
- **Core Function**: Processes and filters snpEff annotation output.
- **Algorithm**: Parses VCF annotations and extracts key information.
- **Input/Output**: Accepts VCF files and produces simplified annotations.
- **Variant Annotation**: Specialized for snpEff output processing.
- **Applications**: Variant filtering, annotation analysis, clinical genetics.

## Pitfalls

- **Memory Usage**: High memory requirements for large VCF files.
- **snpEff Dependency**: Requires snpEff annotations in VCF.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on annotation quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Limited documentation available.

## Examples

### Simplify annotations
**Args:** `simple_sv_annotation -i annotated.vcf -o simplified.vcf`
**Explanation:** `-i` input VCF; `-o` output simplified VCF.

### Filter by impact
**Args:** `simple_sv_annotation -i annotated.vcf -I HIGH -o filtered.vcf`
**Explanation:** `-I HIGH` keep only high impact variants.

### Extract gene names
**Args:** `simple_sv_annotation -i annotated.vcf -g -o genes.txt`
**Explanation:** `-g` extract gene names only.

### Help command
**Args:** `simple_sv_annotation --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `simple_sv_annotation --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `simple_sv_annotation -v -i annotated.vcf -o simplified.vcf`
**Explanation:** `-v` verbose output.

### With config
**Args:** `simple_sv_annotation -i annotated.vcf -c config.yaml -o output.vcf`
**Explanation:** `-c` configuration file.
