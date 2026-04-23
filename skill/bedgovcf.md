---
name: bedgovcf
category: formatting
description: A simple tool to convert BED files to VCF files
tags: [bed, vcf, format-conversion]
author: oxo-call-community
source_url: "https://github.com/nvnieuwk/bedgovcf"
---

## Concepts
- **Tool Overview**: bedgovcf is a simple command-line tool for converting BED format files to VCF (Variant Call Format) files. It is useful when genomic regions stored in BED format need to be represented as variant records in VCF format.
- **BED Format**: BED files describe genomic intervals with chrom, start, end, and optional additional columns.
- **VCF Format**: VCF is a text-based format for storing gene sequence variations. It includes meta-information lines, a header line, and data lines each containing information about a position in the genome.
- **Use Case**: Converting BED regions to VCF format is useful for integrating region-based annotations with variant calling pipelines.

## Pitfalls
- **Coordinate System**: BED uses 0-based half-open coordinates while VCF uses 1-based coordinates. bedgovcf handles this conversion.
- **Missing VCF Fields**: BED files lack many VCF-required fields (ID, REF, ALT, QUAL, FILTER, INFO). bedgovcf fills these with placeholder values.
- **Reference Allele**: Without a reference genome, bedgovcf cannot determine the actual reference allele at each position.

## Examples
### Basic BED to VCF conversion
**Args:** `bedgovcf -i input.bed -o output.vcf`
**Explanation:** Converts input.bed to VCF format with placeholder values for REF, ALT, and other VCF-specific fields.

### Convert with reference genome
**Args:** `bedgovcf -i regions.bed -r reference.fa -o regions.vcf`
**Explanation:** Converts BED regions to VCF using the reference genome to determine actual REF alleles.
