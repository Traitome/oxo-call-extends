---
name: beagle
category: population-genomics
description: Beagle - Software for phasing genotypes and imputing ungenotyped markers
tags: [phasing, imputation, genotype-inference, population-genetics]
author: oxo-call-community
source_url: "http://faculty.washington.edu/browning/beagle/beagle.html"
---

## Concepts

- **Tool Overview**: Beagle is a software package for phasing genotypes and imputing ungenotyped markers using hidden Markov models.

- **Phasing**: Determines haplotype phase (which alleles are on same chromosome) from genotype data.

- **Imputation**: Infers ungenotyped markers using reference panels and linkage disequilibrium.

- **Reference Panels**: Uses reference haplotype panels for improved imputation accuracy.

- **Speed**: Optimized algorithms for fast processing of large datasets.

## Pitfalls

- **Reference Panel Quality**: Imputation accuracy depends on reference panel quality and representativeness.

- **Missing Data**: High missing data rates reduce phasing and imputation accuracy.

- **Population Mismatch**: Reference panels should match study population for best results.

- **Memory Requirements**: Large datasets require substantial memory and disk space.

## Examples

### Basic phasing
**Args:** `java -jar beagle.jar gt=input.vcf out=phased`
**Explanation:** Phases genotypes from input VCF file, outputs phased VCF.

### Imputation with reference panel
**Args:** `java -jar beagle.jar gt=study.vcf ref=reference.vcf.gz out=imputed`
**Explanation:** Imputes missing genotypes using reference panel.

### Window-based imputation
**Args:** `java -jar beagle.jar gt=input.vcf window=500000 overlap=200000 out=imputed`
**Explanation:** Performs imputation in sliding windows for large chromosomes.

### Specify effective population size
**Args:** `java -jar beagle.jar gt=input.vcf ne=10000 out=phased`
**Explanation:** Uses effective population size parameter for phasing model.

### Output posterior probabilities
**Args:** `java -jar beagle.jar gt=input.vcf out=phased gp=true`
**Explanation:** Outputs genotype posterior probabilities in addition to hard calls.

### Chromosome-specific analysis
**Args:** `java -jar beagle.jar gt=input.vcf chrom=chr1 out=chr1_phased`
**Explanation:** Processes only specified chromosome for faster analysis.

### Multiple threads
**Args:** `java -jar beagle.jar gt=input.vcf nthreads=8 out=phased`
**Explanation:** Uses 8 threads for parallel processing.
