---
name: dsh-bio
category: formatting
description: "Tools for BED, FASTA, FASTQ, GAF, GFA1/2, GFF3, PAF, SAM, and VCF files"
tags: [dsh-bio, formatting, file-conversion, bioinformatics-formats]
author: oxo-call-community
source_url: "https://github.com/heuermh/dishevelled-bio"
---

## Concepts

- **Tool Overview**: dsh-bio is a collection of command-line tools for working with various bioinformatics file formats.
- **Core Function**: Provides utilities for converting, filtering, and manipulating BED, FASTA, FASTQ, GAF, GFA, GFF3, PAF, SAM, and VCF files.
- **Input/Output**: Input/Output: Various bioinformatics formats (BED, FASTA, FASTQ, GAF, GFA, GFF3, PAF, SAM, VCF).
- **Algorithm**: Uses streaming parsers for efficient processing of large files.
- **Key Features**: Format conversion, filtering, sorting, statistics, validation.
- **Installation**: `conda install -c bioconda dsh-bio`

## Pitfalls

- **Format Versions**: Different format versions may have incompatible features.
- **Memory Usage**: Some operations may require loading entire files into memory.
- **Character Encoding**: Ensure proper encoding for sequence data.
- **Coordinate Systems**: Different formats may use different coordinate systems.
- **Header Handling**: Preserve headers during format conversion.

## Examples

### Convert BED to GFF3
**Args:** `bed-to-gff3 input.bed output.gff3`
**Explanation:** Converts BED file to GFF3 format.

### Filter FASTA sequences
**Args:** `filter-fasta input.fa output.fa --min-length 100`
**Explanation:** Filters FASTA sequences with minimum length of 100bp.

### Convert SAM to BAM
**Args:** `sam-to-bam input.sam output.bam`
**Explanation:** Converts SAM file to binary BAM format.

### Extract VCF statistics
**Args:** `vcf-statistics input.vcf output.txt`
**Explanation:** Generates statistics from VCF file.

### Sort GFF3 file
**Args:** `sort-gff3 input.gff3 output.gff3`
**Explanation:** Sorts GFF3 file by chromosome and position.