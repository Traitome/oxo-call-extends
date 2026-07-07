---
name: biopet-validatevcf
category: qc
description: Validate VCF files against reference genome
tags: [vcf, validation, variant-calling, quality-control]
author: oxo-call-community
source_url: "https://github.com/biopet/validatevcf"
---

## Concepts

- **Tool Overview**: ValidateVcf validates VCF files against a reference genome, checking positions, alleles, and format compliance.
- **Validation Checks**: Verifies that variant positions exist in reference, alleles match reference at those positions, and VCF format is valid.
- **Reference Comparison**: Compares variant calls against reference genome sequence.
- **Format Validation**: Checks VCF header, field types, and record structure.
- **Applications**: Variant call validation, VCF quality control, pipeline output verification.

## Pitfalls

- **Reference Match**: VCF contig names must match reference contig names exactly.
- **Reference Version**: Must use the same reference genome build used for variant calling.

## Examples

### Validate VCF against reference
**Args:** `java -jar ValidateVcf.jar -i variants.vcf -R reference.fa -o validation_report.txt`
**Explanation:** Validates VCF file against reference genome.

### Validate with specific contigs
**Args:** `java -jar ValidateVcf.jar -i variants.vcf -R reference.fa -c chr1,chr2 -o report.txt`
**Explanation:** Validates VCF only for specified contigs.

### Validate header only
**Args:** `java -jar ValidateVcf.jar -i variants.vcf --header-only -o header_report.txt`
**Explanation:** Validates only the VCF header without checking variant positions.