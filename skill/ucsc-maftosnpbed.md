---
name: ucsc-maftosnpbed
category: utility
description: UCSC mafToSnpBed - Tool for converting MAF to SNP BED.
tags: [ucsc-maftosnpbed, ucsc, maf, snp, bed, format-conversion]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC mafToSnpBed - A tool for converting MAF to SNP BED format.
- **Core Function**: Extracts SNPs from MAF alignments into BED format.
- **Input**: MAF file.
- **Output**: SNP BED file.
- **Installation**: Part of UCSC utilities
- **Use Case**: SNP analysis, variant calling, genomics.

## Pitfalls

- **Memory**: May require significant memory for large files.
- **Format Requirements**: Requires proper MAF format.

## Examples

### Convert MAF to SNP BED
**Args:** `mafToSnpBed input.maf > snps.bed`
**Explanation:** Extract SNPs from MAF to BED.

### With options
**Args:** `mafToSnpBed -minScore=100 input.maf > snps.bed`
**Explanation:** Minimum alignment score filter.
