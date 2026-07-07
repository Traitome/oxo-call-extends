---
name: jannovar-cli
category: annotation
description: Java tool for performing annotation of VCF files with comprehensive variant effect prediction.
tags: [jannovar-cli, annotation, VCF, variant, effect-prediction]
author: oxo-call-community
source_url: "https://github.com/charite/jannovar"
---

## Concepts

- **Tool Overview**: jannovar-cli (v0.36) - A Java-based variant annotation tool that provides comprehensive effect prediction for VCF files.
- **Variant Effect Prediction**: Predicts the functional impact of variants including missense, nonsense, splice site, and regulatory effects.
- **HGVS Nomenclature**: Generates standardized HGVS variant descriptions.
- **Database Integration**: Integrates with Ensembl, RefSeq, and UCSC annotations.
- **Batch Processing**: Supports efficient processing of large VCF files.
- **Annotation Layers**: Provides multiple annotation layers including gene, transcript, protein, and regulatory annotations.

## Pitfalls

- **Memory Usage**: Large annotation databases require significant RAM.
- **Transcript Selection**: Multiple transcript isoforms can produce conflicting annotations.
- **Database Updates**: Outdated annotation databases may miss recent gene models.
- **Ambiguous Variants**: Complex variants (e.g., indels, MNPs) may have ambiguous annotations.
- **Performance**: Java-based implementation may be slower than native tools.
- **File Format**: Requires properly formatted VCF files with correct header information.

## Examples

### Basic VCF annotation
**Args:** `jannovar annotate -i input.vcf -o annotated.vcf -d hg38`
**Explanation:** Annotates VCF file using hg38 reference annotations.

### Use custom database
**Args:** `jannovar annotate -i input.vcf -o annotated.vcf -d custom_db/`
**Explanation:** Uses custom annotation database directory.

### Include regulatory annotations
**Args:** `jannovar annotate -i input.vcf -o annotated.vcf -d hg38 --regulatory`
**Explanation:** Includes regulatory region annotations.

### Output JSON format
**Args:** `jannovar annotate -i input.vcf -o annotated.json -d hg38 --format json`
**Explanation:** Outputs annotations in JSON format instead of VCF.

### Filter by effect type
**Args:** `jannovar annotate -i input.vcf -o annotated.vcf -d hg38 --filter missense`
**Explanation:** Only includes missense variants in output.

### Generate HTML report
**Args:** `jannovar annotate -i input.vcf -o annotated.vcf -d hg38 --report report.html`
**Explanation:** Generates HTML summary report of annotations.