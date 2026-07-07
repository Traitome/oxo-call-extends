---
name: shapeit4
category: population-genomics
description: shapeit4 - Fast and accurate haplotype phasing
tags: ["shapeit4", "population-genomics", "phasing", "haplotype"]
author: oxo-call-community
source_url: "https://odelaneau.github.io/shapeit4/"
---

## Concepts

- **Tool Overview**: shapeit4 (v4.2.2) is a fast and accurate method for haplotype estimation.
- **Core Function**: Performs haplotype phasing from genotype data.
- **Algorithm**: Uses hidden Markov models and statistical phasing approaches.
- **Input/Output**: Accepts VCF files and produces phased haplotypes.
- **Haplotype Phasing**: Focuses on inferring haplotype phase from genotypes.
- **Applications**: Population genetics, imputation, and association studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on genotype data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Phase genotypes
**Args:** `shapeit4 --input input.vcf --output phased.vcf --reference reference.fasta`
**Explanation:** `--input` input VCF; `--output` phased output; `--reference` reference genome.

### With genetic map
**Args:** `shapeit4 --input input.vcf --output phased.vcf --map genetic_map.txt`
**Explanation:** `--map` genetic map file.

### Threaded mode
**Args:** `shapeit4 --input input.vcf --output phased.vcf --thread 8`
**Explanation:** `--thread 8` uses 8 threads.

### Verbose logging
**Args:** `shapeit4 -v --input input.vcf --output phased.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shapeit4 --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shapeit4 --version`
**Explanation:** Shows current version.

### Region phasing
**Args:** `shapeit4 --input input.vcf --output phased.vcf --region chr20:1000000-2000000`
**Explanation:** `--region` specifies genomic region to phase.