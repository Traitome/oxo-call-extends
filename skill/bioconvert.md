---
name: bioconvert
category: formatting
description: Convert between bioinformatics file formats
tags: [format-conversion, bioinformatics, file-formats]
author: oxo-call-community
source_url: "https://github.com/bioconvert/bioconvert"
---

## Concepts
- **Tool Overview**: bioconvert is a comprehensive tool for converting between bioinformatics file formats. It supports 50+ format conversions including BAM, SAM, CRAM, BED, GFF, FASTQ, FASTA, VCF, and more.
- **Format Support**: Sequencing data (FASTQ, BAM, SAM, CRAM), annotation (BED, GFF, GTF), variant data (VCF, BCF), and others.
- **Conversion Methods**: Uses best-in-class tools (samtools, bcftools, bedtools) for each conversion.
- **Quality Preservation**: Maintains data integrity during format conversion.

## Pitfalls
- **Information Loss**: Some format conversions may lose format-specific information (e.g., VCF to BED loses genotype data).
- **Index Requirement**: Some conversions require indexed input files.

## Examples
### Convert BAM to FASTQ
**Args:** `bioconvert bam2fastq input.bam output.fastq`
**Explanation:** Converts BAM alignment to FASTQ format.

### Convert GFF to BED
**Args:** `bioconvert gff2bed input.gff output.bed`
**Explanation:** Converts GFF annotation to BED format.

### Convert VCF to BCF
**Args:** `bioconvert vcf2bcf input.vcf output.bcf`
**Explanation:** Converts VCF to binary BCF format.

### List available conversions
**Args:** `bioconvert --help`
**Explanation:** Shows all supported format conversions.
