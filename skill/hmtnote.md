---
name: hmtnote
category: variant-calling
description: HmtNote annotates human mitochondrial variants using the HmtVar database for comprehensive variant interpretation.
tags: [hmtnote, mitochondrial, variants, annotation]
author: oxo-call-community
source_url: "https://github.com/robertopreste/hmtnote"
---

## Concepts

- **Mitochondrial Variant Annotation**: Annotates VCF files with comprehensive information from the HmtVar database.
- **Multi-category Annotation**: Groups annotations into basic (location, gene), cross-reference (dbSNP, ClinVar), variability (population frequencies), and predictions (pathogenicity scores).
- **HmtVar Integration**: Accesses the HmtVar database containing over 40,000 human mitochondrial variants with curated pathogenicity assessments.
- **Offline Mode**: Supports offline annotation by downloading the HmtVar database locally.
- **VCF and CSV Output**: Generates annotated VCF files and optionally converts results to CSV format for easier analysis.
- **Python API**: Provides programmatic access for integration into custom bioinformatics pipelines.

## Pitfalls

- **Internet Dependency**: Requires internet connection for online database access unless offline database is downloaded.
- **VCF Format Requirements**: Expects properly formatted VCF files with standard mitochondrial variant representations.
- **Database Updates**: Local database may become outdated; regular updates recommended for accurate annotations.
- **Python Version**: Requires Python ≥ 3.6; incompatible with older Python versions.
- **Variant Normalization**: Variants must be properly normalized (left-aligned, parsimonious) for accurate matching.
- **Ambiguous Annotations**: Some variants may have conflicting pathogenicity predictions; manual review recommended for clinical applications.

## Examples

### Basic VCF annotation
**Args:** `hmtnote annotate input.vcf annotated.vcf`
**Explanation:** Annotates a VCF file with all available annotation categories from HmtVar.

### Select specific annotation categories
**Args:** `hmtnote annotate input.vcf annotated.vcf --basic --variab`
**Explanation:** Annotates VCF with only basic and variability annotations, excluding cross-references and predictions.

### Generate CSV output
**Args:** `hmtnote annotate input.vcf annotated.vcf --csv`
**Explanation:** Generates both annotated VCF and CSV files for easy spreadsheet analysis.

### Download offline database
**Args:** `hmtnote dump`
**Explanation:** Downloads the HmtVar annotation database for offline use.

### Offline annotation mode
**Args:** `hmtnote annotate input.vcf annotated.vcf --offline`
**Explanation:** Performs annotation using locally stored database without internet connection.

### Python API usage
**Args:** `python -c "from hmtnote import annotate; annotate('input.vcf', 'annotated.vcf', basic=True, predict=True)"`
**Explanation:** Integrates HmtNote annotation into Python scripts with selective annotation categories.