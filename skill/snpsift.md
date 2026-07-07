---
name: snpsift
category: variant-analysis
description: SnpSift - Toolbox for filtering and manipulating annotated VCF files
tags: [snpsift, variant-analysis, vcf, filtering, annotation]
author: oxo-call-community
source_url: "http://snpeff.sourceforge.net/SnpSift.html"
---

## Concepts

- **Tool Overview**: snpsift (v5.4.0c) - A toolbox for VCF file manipulation
- **Core Function**: Filters, annotates, and manipulates variant files
- **Input/Output**: Accepts VCF files; outputs filtered/annotated VCF
- **Algorithm**: Provides multiple utilities for variant file processing
- **Installation**: `conda install -c bioconda snpsift`
- **Key Features**: Filtering, annotation, statistics, VCF manipulation

## Pitfalls

- **Input Requirements**: Requires properly formatted VCF files
- **Annotation Files**: Requires annotation databases for some operations
- **Filter Syntax**: Filter expressions require proper syntax
- **Memory Usage**: Large VCF files require significant memory
- **Field Names**: Field names must match VCF specifications
- **Output Format**: Multiple output formats available

## Examples

### Display help
**Args:** `SnpSift --help`
**Explanation:** Shows available options and usage information.

### Filter VCF
**Args:** `SnpSift filter "QUAL > 30" input.vcf > filtered.vcf`
**Explanation:** Filter variants by quality score.

### Filter by region
**Args:** `SnpSift filter "(POS >= 1000) && (POS <= 2000)" input.vcf > filtered.vcf`
**Explanation:** Filter variants by position range.

### Annotate VCF
**Args:** `SnpSift annotate annotations.txt input.vcf > annotated.vcf`
**Explanation:** Annotate VCF with external data.

### Extract fields
**Args:** `SnpSift extractFields input.vcf CHROM POS REF ALT QUAL > fields.txt`
**Explanation:** Extract specific fields from VCF.

### Calculate statistics
**Args:** `SnpSift stats input.vcf > statistics.txt`
**Explanation:** Calculate VCF statistics.

### Split VCF
**Args:** `SnpSift split input.vcf output_dir/`
**Explanation:** Split VCF by chromosome.

### Concordance check
**Args:** `SnpSift concordance vcf1.vcf vcf2.vcf > concordance.txt`
**Explanation:** Check concordance between VCF files.