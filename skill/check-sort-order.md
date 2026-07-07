---
name: check-sort-order
category: utility
description: Check sort-order of genomic files according to a genomefile
tags: [check-sort-order, genomic-files, sort-order, validation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/gogetdata/ggd-utils"
---

## Concepts

- **Tool Overview**: check-sort-order validates that genomic files are sorted according to a specified genome reference order.
- **Core Function**: Verifies the sort order of genomic data files (BED, VCF, BAM, etc.) against a genome chromosome order file.
- **Features**: Supports multiple genomic formats, checks coordinate ordering, and provides validation reports.
- **Input**: Genomic data file and genome file defining chromosome order.
- **Output**: Validation status indicating whether file is properly sorted.
- **Application**: Quality control for genomic data processing pipelines.
- **Installation**: Install via bioconda: `conda install -c bioconda check-sort-order`

## Pitfalls

- **Genome File Format**: Requires specific genome file format defining chromosome order.
- **File Format**: Only supports certain genomic file formats.
- **Sorting Standards**: Different tools may use different sorting conventions.
- **Case Sensitivity**: Chromosome names must match exactly between files.

## Examples

### Check sort order
**Args:** `check-sort-order -i data.bed -g genome.txt`
**Explanation:** Checks if BED file is sorted according to genome order.

### With VCF file
**Args:** `check-sort-order -i variants.vcf -g genome.txt`
**Explanation:** Validates VCF file sorting against genome order.

### Output detailed report
**Args:** `check-sort-order -i data.bed -g genome.txt -v`
**Explanation:** Runs validation with verbose output.

### Display help
**Args:** `check-sort-order --help`
**Explanation:** Shows all available options and usage information.