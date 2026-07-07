---
name: seshat
category: annotation
description: seshat - VCF annotation with Seshat TP53 database
tags: ["seshat", "annotation", "VCF", "TP53"]
author: oxo-call-community
source_url: "https://github.com/clintval/tp53"
---

## Concepts

- **Tool Overview**: seshat (v0.10.0) annotates VCFs with the Seshat TP53 database.
- **Core Function**: Adds TP53-specific annotations to variant calls.
- **Algorithm**: Matches variants against TP53 mutation database.
- **Input/Output**: Accepts VCF files and produces annotated VCFs.
- **TP53 Annotation**: Focuses on TP53 variant annotation.
- **Applications**: Cancer genomics, mutation analysis, and TP53 research.

## Pitfalls

- **Memory Usage**: High memory requirements for large VCF files.
- **Database Requirements**: Requires Seshat TP53 database.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on VCF quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Annotate VCF
**Args:** `seshat annotate -i input.vcf -o annotated.vcf`
**Explanation:** `-i` input VCF; `-o` output annotated VCF.

### With database
**Args:** `seshat annotate -i input.vcf -d tp53.db -o annotated.vcf`
**Explanation:** `-d` specifies database file.

### Generate report
**Args:** `seshat report -i annotated.vcf -o report.html`
**Explanation:** Generates HTML report.

### Verbose logging
**Args:** `seshat -v annotate -i input.vcf -o annotated.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `seshat --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `seshat --version`
**Explanation:** Shows current version.

### Download database
**Args:** `seshat download`
**Explanation:** Downloads latest TP53 database.