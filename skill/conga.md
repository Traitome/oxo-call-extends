---
name: conga
category: variant-calling
description: Copy number variation genotyping for ancient and low-coverage genomes
tags: [conga, cnv, ancient-dna, low-coverage, genotyping]
author: oxo-call-community
source_url: "https://github.com/asylvz/CONGA"
---

## Concepts

- **Tool Overview**: CONGA is a specialized tool for genotyping copy number variations (CNVs) in ancient genomes and low-coverage sequencing data where standard methods may fail.
- **Core Function**: Genotypes known CNV loci using read depth and split-read signals optimized for low-coverage and degraded DNA samples.
- **Algorithm**: Uses Bayesian framework to integrate read depth, mapping quality, and fragment length information.
- **Input**: Aligned sequencing reads in BAM format, CNV locus definitions.
- **Output**: CNV genotypes with confidence scores and quality metrics.
- **Application**: Ancient DNA analysis, low-coverage population genomics, and CNV association studies.
- **Installation**: Install via bioconda: `conda install -c bioconda conga`

## Pitfalls

- **Coverage Requirements**: Designed for low coverage but extremely low coverage (<0.5x) may be insufficient.
- **Reference Bias**: Ancient DNA damage patterns may affect genotyping accuracy.
- **CNV Definition**: Requires pre-defined CNV loci for genotyping.
- **Damage Patterns**: May require ancient DNA damage correction for accurate results.
- **Population Specificity**: Reference CNV frequencies may not match all populations.

## Examples

### Genotype CNVs in ancient genome
**Args:** `conga -i ancient.bam -r reference.fasta -c cnv_regions.bed -o genotypes.txt`
**Explanation:** Genotypes CNVs in ancient DNA sample.

### With damage correction
**Args:** `conga -i ancient.bam -r reference.fasta -c cnv_regions.bed --ancient-dna -o genotypes.txt`
**Explanation:** Applies ancient DNA damage correction during genotyping.

### Set minimum coverage
**Args:** `conga -i sample.bam -r reference.fasta -c cnv_regions.bed --min-coverage 0.5 -o genotypes.txt`
**Explanation:** Sets minimum coverage threshold for genotyping.

### Display help
**Args:** `conga --help`
**Explanation:** Shows all available options and usage information.