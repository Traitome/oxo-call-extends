---
name: samestr
category: metagenomics
description: Identify shared strains between metagenomic samples using SNV profiles
tags: ["samestr", "metagenomics", "strains", "SNV", "comparative analysis"]
author: oxo-call-community
source_url: "https://github.com/danielpodlesny/samestr/"
---

## Concepts

- **Tool Overview**: SameStr (v1.2025.111) is a tool for identifying shared bacterial strains between pairs of metagenomic samples based on the similarity of their SNV (Single Nucleotide Variant) profiles.
- **Core Function**: Compares SNV profiles across metagenomic samples to determine if they share common strains, enabling tracking of bacterial populations across samples.
- **Algorithm**: Uses SNV similarity metrics to quantify strain sharing, implements statistical methods to distinguish true shared strains from random matches.
- **Input Format**: SNV profiles (VCF format), metagenomic abundance profiles.
- **Output Format**: Strain sharing matrix, similarity scores, visualization data.
- **Use Case**: Metagenomic strain tracking, outbreak investigation, longitudinal studies, microbial ecology.

## Pitfalls

- **SNV calling quality**: Results depend on accurate SNV calling from metagenomic data.
- **Reference genome**: Requires good reference genomes for SNV detection.
- **Coverage depth**: Low coverage may miss true variants.
- **Strain diversity**: Highly diverse populations may complicate strain identification.
- **Computational resources**: Large datasets require significant memory and CPU.
- **False positives**: May detect spurious strain sharing due to sequencing errors.

## Examples

### Basic strain comparison
**Args:** `samestr -i sample1.vcf sample2.vcf -o comparison.txt`
**Explanation:** `-i` input VCF files; `-o` output comparison results.

### Multiple samples
**Args:** `samestr -i *.vcf -o matrix.txt`
**Explanation:** Compares all VCF files in directory.

### Threshold setting
**Args:** `samestr -i sample1.vcf sample2.vcf -o comparison.txt -t 0.8`
**Explanation:** `-t` similarity threshold (default: 0.7).

### Output matrix
**Args:** `samestr -i *.vcf -o matrix.txt --matrix`
**Explanation:** `--matrix` outputs pairwise similarity matrix.

### Visualization
**Args:** `samestr -i *.vcf -o plot.pdf --plot`
**Explanation:** `--plot` generates visualization of strain sharing.

### Abundance filtering
**Args:** `samestr -i sample1.vcf sample2.vcf -o comparison.txt -m 0.01`
**Explanation:** `-m` minimum abundance threshold.

### Verbose output
**Args:** `samestr -i sample1.vcf sample2.vcf -o comparison.txt -v`
**Explanation:** `-v` verbose output with detailed statistics.