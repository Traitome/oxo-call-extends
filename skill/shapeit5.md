---
name: shapeit5
category: variant-calling
description: shapeit5 - Fast and accurate haplotype phasing
tags: ["shapeit5", "variant-calling", "phasing", "haplotype"]
author: oxo-call-community
source_url: "https://odelaneau.github.io/shapeit5"
---

## Concepts

- **Tool Overview**: shapeit5 (v5.1.1) is a fast and accurate method for haplotype estimation.
- **Core Function**: Performs haplotype phasing from genotype data.
- **Algorithm**: Uses advanced statistical methods for accurate phasing.
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
**Args:** `shapeit5 --input input.vcf --output phased.vcf --reference reference.fasta`
**Explanation:** `--input` input VCF; `--output` phased output; `--reference` reference genome.

### With genetic map
**Args:** `shapeit5 --input input.vcf --output phased.vcf --map genetic_map.txt`
**Explanation:** `--map` genetic map file.

### Threaded mode
**Args:** `shapeit5 --input input.vcf --output phased.vcf --thread 8`
**Explanation:** `--thread 8` uses 8 threads.

### Verbose logging
**Args:** `shapeit5 -v --input input.vcf --output phased.vcf`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shapeit5 --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shapeit5 --version`
**Explanation:** Shows current version.

### Region phasing
**Args:** `shapeit5 --input input.vcf --output phased.vcf --region chr20:1000000-2000000`
**Explanation:** `--region` specifies genomic region to phase.