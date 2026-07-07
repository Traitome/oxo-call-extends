---
name: scg
category: population-genomics
description: SCG - Single Cell Genotyper for clonal genotype and population structure inference
tags: ["scg", "population-genomics", "single-cell", "genotyping"]
author: oxo-call-community
source_url: "https://bitbucket.org/aroth85/scg/wiki/Home"
---

## Concepts

- **Tool Overview**: SCG (v0.3.1) is the Single Cell Genotyper for clonal genotype and population structure inference from single-cell tumor sequencing.
- **Core Function**: Identifies clonal genotypes and infers population structure from single-cell sequencing data.
- **Algorithm**: Uses statistical models to call genotypes and infer clonal relationships.
- **Input/Output**: Accepts variant data and produces clonal genotypes and population structure.
- **Single-Cell Genotyping**: Specifically designed for single-cell tumor sequencing data.
- **Applications**: Cancer genomics, clonal evolution analysis, and population structure inference.

## Pitfalls

- **Amplification Bias**: WGA artifacts can affect genotyping.
- **Allelic Dropout**: May miss heterozygous variants due to dropout.
- **Read Depth**: Requires sufficient sequencing depth per cell.
- **Computational Resources**: High memory and CPU requirements.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **False Positives**: May report false genotypes from amplification errors.

## Examples

### Basic genotyping
**Args:** `scg -i variants.vcf -o genotypes.txt`
**Explanation:** `-i` input VCF with variants; `-o` output genotypes.

### With reference genome
**Args:** `scg -i variants.vcf -r reference.fasta -o genotypes.txt`
**Explanation:** `-r` reference genome for genotype calling.

### Population structure
**Args:** `scg -i variants.vcf --structure -o structure.txt`
**Explanation:** `--structure` infers population structure.

### Clonal analysis
**Args:** `scg -i variants.vcf --clones -o clones.txt`
**Explanation:** `--clones` identifies clonal genotypes.

### Verbose logging
**Args:** `scg -i variants.vcf -v -o genotypes.txt`
**Explanation:** `-v` enables verbose output for debugging.

### Quality filtering
**Args:** `scg -i variants.vcf -q 20 -o genotypes.txt`
**Explanation:** `-q 20` filters variants with quality below 20.

### Output JSON
**Args:** `scg -i variants.vcf -f json -o genotypes.json`
**Explanation:** `-f json` outputs results in JSON format.