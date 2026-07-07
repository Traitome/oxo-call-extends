---
name: biopet-validateannotation
category: qc
description: Validate annotation files (GTF/GFF/RefFlat) against reference genome
tags: [annotation, validation, GTF, GFF, RefFlat]
author: oxo-call-community
source_url: "https://github.com/biopet/validateannotation"
---

## Concepts

- **Tool Overview**: ValidateAnnotation validates whether annotation files (GTF, GFF, or RefFlat format) are correct and consistent with a reference genome.
- **Validation Checks**: Verifies that all annotated contigs/chromosomes exist in the reference, checks feature coordinates are valid, and validates gene structure consistency.
- **Format Support**: Supports GTF, GFF, and RefFlat annotation formats.
- **Applications**: Annotation quality control, pipeline validation, reference genome compatibility checking.

## Pitfalls

- **Reference Match**: Annotation and reference genome must be from the same build/assembly.
- **Format Requirements**: Annotation files must follow standard format specifications.

## Examples

### Validate GTF annotation
**Args:** `java -jar ValidateAnnotation.jar -i annotation.gtf -R reference.fa -o report.txt`
**Explanation:** Validates GTF annotation against reference genome.

### Validate RefFlat format
**Args:** `java -jar ValidateAnnotation.jar -i genes.refflat -R reference.fa --format refflat`
**Explanation:** Validates RefFlat annotation file against reference.

### Check specific contigs
**Args:** `java -jar ValidateAnnotation.jar -i annotation.gtf -R reference.fa -c chr1,chr2,chr3`
**Explanation:** Validates annotation only for specified contigs.