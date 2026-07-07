---
name: vcf2maf
category: bioinformatics
description: vcf2maf - VCF to MAF format converter.
tags: [vcf2maf, vcf-processing, maf, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/mskcc/vcf2maf"
---

## Concepts

- **Tool Overview**: vcf2maf - A tool for converting VCF to MAF format.
- **Core Function**: Converts VCF files to Mutation Annotation Format.
- **Input**: VCF file.
- **Output**: MAF file.
- **Installation**: Install via conda or source
- **Use Case**: Format conversion, TCGA analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Annotation**: Requires VEP for annotation.

## Examples

### Convert to MAF
**Args:** `vcf2maf.pl --input-vcf input.vcf --output-maf output.maf --ref-fasta ref.fasta`
**Explanation:** Convert VCF to MAF.

### With options
**Args:** `vcf2maf.pl --input-vcf input.vcf --output-maf output.maf --ref-fasta ref.fasta --vep-path vep`
**Explanation:** Specify VEP path.
