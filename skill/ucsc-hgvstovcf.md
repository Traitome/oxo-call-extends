---
name: ucsc-hgvstovcf
category: utility
description: UCSC hgVSToVcf - Tool for converting VS to VCF format.
tags: [ucsc-hgvstovcf, ucsc, vcf, format-conversion, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC hgVSToVcf - A tool for converting variation tables to VCF.
- **Core Function**: Converts variation data to VCF format.
- **Input**: Variation table.
- **Output**: VCF file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Variant calling, format conversion, genomics.

## Pitfalls

- **Database Access**: Requires database credentials.
- **Memory**: May require significant memory for large datasets.

## Examples

### Convert to VCF
**Args:** `hgVSToVcf -db=hg38 -table=snp155 > snps.vcf`
**Explanation:** Convert variation table to VCF.

### With options
**Args:** `hgVSToVcf -db=hg38 -table=snp155 -verbose > snps.vcf`
**Explanation:** Convert with verbose output.
