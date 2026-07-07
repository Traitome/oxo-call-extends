---
name: vcf2maf-umccr
category: bioinformatics
description: vcf2maf-umccr - UMCCR fork of vcf2maf.
tags: [vcf2maf-umccr, vcf-processing, maf, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/umccr/vcf2maf"
---

## Concepts

- **Tool Overview**: vcf2maf-umccr - UMCCR fork of vcf2maf with additional features.
- **Core Function**: Converts VCF files to Mutation Annotation Format.
- **Input**: VCF file.
- **Output**: MAF file.
- **Installation**: Install via conda or source
- **Use Case**: Format conversion, cancer genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Annotation**: Requires VEP for annotation.

## Examples

### Convert to MAF
**Args:** `vcf2maf.pl --input-vcf input.vcf --output-maf output.maf --ref-fasta ref.fasta`
**Explanation:** Convert VCF to MAF.

### With options
**Args:** `vcf2maf.pl --input-vcf input.vcf --output-maf output.maf --ref-fasta ref.fasta --vep-forks 8`
**Explanation:** Use 8 VEP forks.
