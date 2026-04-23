---
name: atol-qc-annotation
category: qc
description: AToL QC Annotation - Run QC on GTF and GFF annotation files
tags: [annotation, qc, gtf, gff, validation]
author: oxo-call-community
source_url: "https://github.com/TomHarrop/atol-qc-annotation"
---

## Concepts

- **Tool Overview**: Quality control tool for validating GTF and GFF genome annotation files in AToL Genome Engine pipeline.

- **Format Validation**: Checks for proper GTF/GFF format compliance and syntax errors.

- **Biological Validation**: Validates gene models for biological plausibility (start/stop codons, splice sites, etc.).

- **Consistency Checks**: Ensures consistency between annotation and reference genome.

## Pitfalls

- **Format Versions**: GTF/GFF have multiple versions. Ensure correct version specification.

- **Coordinate Systems**: Check for off-by-one errors and coordinate system consistency (0-based vs 1-based).

- **Missing Features**: Some annotation tools omit certain feature types. Verify all required features present.

## Examples

### Basic annotation QC
**Args:** `atol-qc-annotation --annotation genes.gtf --genome genome.fasta --output qc_report.txt`
**Explanation:** Validates GTF annotation against reference genome.

### Check specific features
**Args:** `atol-qc-annotation --annotation genes.gtf --features gene,mRNA,exon,CDS --output report.txt`
**Explanation:** Validates only specified feature types in annotation.

### Fix common errors
**Args:** `atol-qc-annotation --annotation genes.gtf --fix-errors --output fixed.gtf`
**Explanation:** Attempts to automatically fix common annotation errors.

### Generate detailed report
**Args:** `atol-qc-annotation --annotation genes.gtf --genome genome.fasta --report report.html --output results/`
**Explanation:** Generates HTML report with detailed validation results and statistics.
