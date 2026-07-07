---
name: seq2hla
category: variant-analysis
description: seq2hla - HLA typing and expression from RNA sequencing data
tags: ["seq2hla", "variant-analysis", "HLA-typing", "RNA-seq"]
author: oxo-call-community
source_url: "https://github.com/TRON-Bioinformatics/seq2HLA"
---

## Concepts

- **Tool Overview**: seq2hla (v2.3) performs HLA typing and expression analysis from RNA-seq data.
- **Core Function**: Determines HLA alleles and expression levels from sequencing data.
- **Algorithm**: Uses mapping and variant calling for HLA typing.
- **Input/Output**: Accepts BAM/FASTQ files and produces HLA types with expression.
- **HLA Analysis**: Focuses on HLA allele identification and expression quantification.
- **Applications**: Immunogenomics, transplant matching, and disease association studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **HLA Reference**: Requires up-to-date HLA reference database.
- **RNA-seq Specific**: Designed for RNA-seq data, may not work with DNA data.

## Examples

### HLA typing
**Args:** `python seq2HLA.py -1 reads_1.fastq -2 reads_2.fastq -o output/`
**Explanation:** `-1/-2` paired-end reads; `-o` output directory.

### From BAM
**Args:** `python seq2HLA.py -b input.bam -o output/`
**Explanation:** `-b` input BAM file.

### Verbose logging
**Args:** `python seq2HLA.py -1 reads_1.fastq -2 reads_2.fastq -v -o output/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `python seq2HLA.py --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `python seq2HLA.py --version`
**Explanation:** Shows current version.

### Output format
**Args:** `python seq2HLA.py -1 reads_1.fastq -2 reads_2.fastq -f json -o output/`
**Explanation:** `-f json` outputs in JSON format.

### Expression only
**Args:** `python seq2HLA.py -b input.bam -e -o output/`
**Explanation:** `-e` only outputs expression data.