---
name: slivar
category: variant-calling
description: A fast and flexible tool for filtering and annotating variants in VCF/BCF format using simple expressions
tags: [slivar, variant-calling, vcf, annotation, filtering]
author: oxo-call-community
source_url: "https://github.com/brentp/slivar"
---

## Concepts

- **Tool Overview**: slivar (v0.3.3) - A command-line tool for variant filtering and annotation in VCF/BCF format
- **Core Function**: Filters and annotates variants using simple JavaScript-like expressions
- **Input/Output**: Accepts VCF/BCF files; outputs filtered VCF/BCF with annotations
- **Algorithm**: Uses powerful expression-based filtering with built-in variant annotations
- **Installation**: `conda install -c bioconda slivar`
- **Key Features**: Supports gVCF, multi-sample VCF, BED-based annotations, and customizable filters

## Pitfalls

- **Expression Syntax**: Requires learning slivar's expression syntax
- **VCF Format**: Input VCF must be properly formatted and indexed
- **Memory Usage**: Large VCF files may require significant memory
- **Annotation Files**: External annotation files need specific formats
- **Sample Names**: Case-sensitive sample name matching
- **Filter Order**: Filter order affects results; apply hard filters first

## Examples

### Display help
**Args:** `slivar --help`
**Explanation:** Shows available options and usage information.

### Basic filtering
**Args:** `slivar expr -v input.vcf -o filtered.vcf -e 'QUAL > 30 && DP > 10'`
**Explanation:** Filter variants with quality > 30 and depth > 10.

### Annotate with BED file
**Args:** `slivar expr -v input.vcf -o annotated.vcf --bed annotations.bed`
**Explanation:** Add annotations from BED file to variants.

### Multi-sample filtering
**Args:** `slivar expr -v input.vcf -o filtered.vcf -e 'AC > 0 && AN >= 2'`
**Explanation:** Filter variants with at least one alternate allele.

### De novo calling
**Args:** `slivar de-novo -v trio.vcf -o denovo.vcf`
**Explanation:** Identify de novo variants in trios.

### Mendelian error checking
**Args:** `slivar mendelian -v trio.vcf -o errors.vcf`
**Explanation:** Check for Mendelian inheritance errors.

### Combine multiple filters
**Args:** `slivar expr -v input.vcf -o filtered.vcf -e '(QUAL > 30 || (GQ > 20 && DP > 8)) && AF < 0.01'`
**Explanation:** Complex filtering with logical operators.