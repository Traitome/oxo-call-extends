---
name: savvy
category: variant-calling
description: Interface to various variant calling formats for VCF manipulation
tags: ["savvy", "variant-calling", "VCF", "format-conversion"]
author: oxo-call-community
source_url: "https://github.com/statgen/savvy"
---

## Concepts

- **Tool Overview**: Savvy (v2.2.0) is a versatile interface to various variant calling formats, providing tools for VCF manipulation, conversion, and analysis.
- **Core Function**: Handles VCF file operations including filtering, merging, splitting, and format conversion.
- **Algorithm**: Uses efficient parsing and manipulation of VCF data structures.
- **Input/Output**: Accepts VCF files and produces modified VCF or other variant formats.
- **Format Support**: Supports VCF, BCF, and other variant calling formats.
- **Applications**: Variant data preprocessing, quality control, and format conversion.

## Pitfalls

- **Format Specific**: Designed for VCF/BCF formats, may not handle other variant formats.
- **Memory Usage**: High memory consumption for large VCF files.
- **Complex Headers**: May struggle with non-standard VCF headers.
- **Performance**: Processing very large VCF files can be slow.
- **Dependency Issues**: Requires specific version of htslib for BCF support.
- **Documentation**: Limited documentation for advanced features.

## Examples

### Basic VCF filtering
**Args:** `savvy filter -i input.vcf -o filtered.vcf -q 30`
**Explanation:** `-i` input VCF; `-o` output VCF; `-q 30` filters by quality >= 30.

### Convert VCF to BCF
**Args:** `savvy convert -i input.vcf -o output.bcf -f bcf`
**Explanation:** `-f bcf` converts VCF to compressed BCF format.

### Merge VCF files
**Args:** `savvy merge -i vcf1.vcf vcf2.vcf -o merged.vcf`
**Explanation:** Merges multiple VCF files into a single output.

### Split multi-allelic sites
**Args:** `savvy split -i input.vcf -o split.vcf`
**Explanation:** Splits multi-allelic variants into separate records.

### Extract specific chromosomes
**Args:** `savvy extract -i input.vcf -c chr1,chr2 -o extracted.vcf`
**Explanation:** `-c` extracts only specified chromosomes.

### Quality statistics
**Args:** `savvy stats -i input.vcf -o stats.txt`
**Explanation:** Generates quality statistics report for VCF file.

### Subset samples
**Args:** `savvy subset -i input.vcf -s sample1,sample2 -o subset.vcf`
**Explanation:** `-s` extracts only specified samples from multi-sample VCF.