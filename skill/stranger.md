---
name: stranger
category: variant-annotation
description: Annotate VCF files with STR variants with pathogenicity implications.
tags: [stranger, variant-annotation, str-variants, clinical-genomics]
author: oxo-call-community
source_url: "https://github.com/Clinical-Genomics/stranger/blob/v0.10.0/README.md"
---

## Concepts

- **Tool Overview**: stranger (v0.10.0) is a tool for annotating VCF files with STR variants and their pathogenicity implications.
- **Core Function**: Adds functional annotations and pathogenicity predictions to STR variants.
- **Algorithm**: Uses reference databases and predictive models to annotate STR variants.
- **Input/Output**: Input: VCF file with STR variants; Output: Annotated VCF with pathogenicity scores.
- **Applications**: Clinical genomics, variant interpretation, disease diagnosis.
- **Installation**: `conda install -c bioconda stranger` or download from GitHub.

## Pitfalls

- **Database Quality**: Outdated databases affect annotation accuracy.
- **Variant Quality**: Poor quality variants produce unreliable annotations.
- **Pathogenicity Prediction**: Predictions are probabilistic, not definitive.
- **Interpretation**: Requires clinical expertise for variant interpretation.
- **Memory Requirements**: Large VCF files require significant memory.
- **Computational Time**: Annotation of large datasets can be slow.

## Examples

### Display help
**Args:** `stranger --help`
**Explanation:** Shows available options and usage information.

### Basic annotation
**Args:** `stranger -i variants.vcf -o annotated.vcf`
**Explanation:** Annotate VCF file with STR variant information.

### With reference genome
**Args:** `stranger -i variants.vcf -r reference.fasta -o annotated.vcf`
**Explanation:** Use reference genome for better annotation.

### Verbose mode
**Args:** `stranger -i variants.vcf -o annotated.vcf -v`
**Explanation:** Run with detailed logging for debugging.

### Output HTML report
**Args:** `stranger -i variants.vcf -o annotated.vcf --html-report`
**Explanation:** Generate HTML report with variant annotations.

### Custom database
**Args:** `stranger -i variants.vcf -d custom_db/ -o annotated.vcf`
**Explanation:** Use custom annotation database.

### Batch processing
**Args:** `stranger -i batch/ -o results/`
**Explanation:** Process multiple VCF files together.

### Filter by quality
**Args:** `stranger -i variants.vcf -o annotated.vcf -q 20`
**Explanation:** Filter variants by quality score threshold.

### Include pathogenicity
**Args:** `stranger -i variants.vcf -o annotated.vcf --pathogenicity`
**Explanation:** Include pathogenicity predictions in annotations.
