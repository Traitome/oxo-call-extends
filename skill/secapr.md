---
name: secapr
category: sequence-analysis
description: secapr - Process sequence-capture FASTQ files into alignments for phylogenetic analyses
tags: ["secapr", "sequence-analysis", "phylogenetics", "FASTQ"]
author: oxo-call-community
source_url: "https://github.com/AntonelliLab/seqcap_processor"
---

## Concepts

- **Tool Overview**: secapr (v2.2.8) processes sequence-capture FASTQ files into alignments for phylogenetic analyses.
- **Core Function**: Converts raw sequencing data into phylogenetic alignments with allele phasing.
- **Algorithm**: Implements quality filtering, trimming, mapping, and phasing for sequence capture data.
- **Input/Output**: Accepts FASTQ files and produces multiple sequence alignments.
- **Allele Phasing**: Integrates allele phasing for heterozygous sites.
- **Applications**: Phylogenetic analysis, population genetics, and evolutionary biology.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Data Quality**: Results depend on sequencing depth and quality.
- **Reference Genome**: Requires suitable reference genome for mapping.
- **Phasing Quality**: Phasing results may vary.

## Examples

### Basic processing
**Args:** `secapr process -i fastq/ -r reference.fasta -o output/`
**Explanation:** `-i` input FASTQ directory; `-r` reference genome; `-o` output directory.

### With phasing
**Args:** `secapr process -i fastq/ -r reference.fasta --phase -o output/`
**Explanation:** `--phase` enables allele phasing.

### Quality filtering
**Args:** `secapr process -i fastq/ -r reference.fasta -q 20 -o output/`
**Explanation:** `-q 20` filters reads with quality below 20.

### Verbose logging
**Args:** `secapr process -i fastq/ -r reference.fasta -v -o output/`
**Explanation:** `-v` enables verbose output for debugging.

### Threads
**Args:** `secapr process -i fastq/ -r reference.fasta -t 8 -o output/`
**Explanation:** `-t 8` uses 8 threads for parallel processing.

### Generate report
**Args:** `secapr report -i output/ -o report.pdf`
**Explanation:** Generates summary report.

### Help command
**Args:** `secapr --help`
**Explanation:** Shows available commands and options.