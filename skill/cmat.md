---
name: cmat
category: alignment
description: ClinVar Mapping and Annotation Toolkit
tags: [cmat, clinvar, variant-annotation, bioinformatics, genetics]
author: oxo-call-community
source_url: "https://github.com/EBIvariation/CMAT/blob/v3.4.3/README.md"
---

## Concepts

- **Tool Overview**: CMAT (ClinVar Mapping and Annotation Toolkit) is a tool for mapping and annotating genetic variants against ClinVar database.
- **Core Function**: Maps variants to ClinVar records and provides comprehensive annotation for clinical interpretation.
- **Algorithm**: Uses variant normalization and mapping algorithms to match variants against ClinVar reference data.
- **Input**: Variant files (VCF format) containing genetic variants.
- **Output**: Annotated variants with ClinVar information and clinical significance.
- **Application**: Clinical variant analysis, variant classification, and genetic diagnostics.
- **Installation**: Install via bioconda: `conda install -c bioconda cmat`

## Pitfalls

- **VCF Format**: Requires properly formatted VCF files.
- **ClinVar Version**: Results depend on ClinVar database version used.
- **Variant Normalization**: Requires proper variant normalization for accurate mapping.
- **Database Updates**: ClinVar database should be regularly updated.
- **Interpretation**: Clinical significance annotations require careful interpretation.

## Examples

### Annotate variants with ClinVar
**Args:** `cmat -i variants.vcf -o annotated.vcf`
**Explanation:** Annotates VCF variants with ClinVar information.

### Update ClinVar database
**Args:** `cmat update -o clinvar.db`
**Explanation:** Updates local ClinVar database.

### Map variants
**Args:** `cmat map -i variants.vcf -d clinvar.db -o mapped.txt`
**Explanation:** Maps variants against local ClinVar database.

### Display help
**Args:** `cmat --help`
**Explanation:** Shows all available options and usage information.