---
name: fuc
category: formatting
description: Frequently used commands in bioinformatics.
tags: [fuc, bioinformatics, utilities, command-line]
author: oxo-call-community
source_url: "https://github.com/sbslee/fuc"
---

## Concepts
- **Bioinformatics Utilities**: Collection of frequently used bioinformatics commands.
- **File Format Conversion**: Converts between common bioinformatics formats.
- **Sequence Manipulation**: Tools for sequence analysis and manipulation.
- **Variant Analysis**: Utilities for variant calling and analysis.
- **Quality Control**: Basic QC tools for sequencing data.

## Pitfalls
- **Format Specific**: Designed for specific bioinformatics formats.
- **Dependency Requirements**: May require other bioinformatics tools.
- **Output Compatibility**: Output may need conversion for some tools.
- **Memory Usage**: Large files may require significant memory.
- **Parameter Complexity**: Some commands have many options.

## Examples
### Convert VCF to CSV
**Args:** `fuc vcf2csv input.vcf -o output.csv`
**Explanation:** Converts VCF file to CSV format.

### Filter VCF by quality
**Args:** `fuc filter-vcf -i input.vcf -q 30 -o filtered.vcf`
**Explanation:** Filters VCF to keep only variants with quality >= 30.

### Extract sequences from FASTA
**Args:** `fuc extract-seq -i genome.fasta -r chr1:1-1000 -o region.fasta`
**Explanation:** Extracts sequence from specified region.

### Count reads in FASTQ
**Args:** `fuc count-reads -i reads.fastq`
**Explanation:** Counts number of reads in FASTQ file.

### Merge BED files
**Args:** `fuc merge-bed -i file1.bed file2.bed -o merged.bed`
**Explanation:** Merges multiple BED files.