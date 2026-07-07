---
name: clam
category: population-genomics
description: Classification of callable loci intervals and population genetic statistics estimation
tags: [clam, population-genomics, variant-analysis, statistics]
author: oxo-call-community
source_url: "https://github.com/cademirch/clam"
---

## Concepts

- **Tool Overview**: CLAM is a tool for classification of callable loci intervals and accurate estimation of population genetic statistics from sequencing data.
- **Core Function**: Identifies callable genomic regions and calculates population genetic metrics from variant data.
- **Features**: Callable region identification, population statistics calculation, and variant filtering.
- **Input**: VCF files with genotype calls and BAM alignment files.
- **Output**: Callable region intervals and population genetic statistics.
- **Application**: Population genetics, variant quality control, and genomic analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda clam`

## Pitfalls

- **VCF Quality**: Requires high-quality genotype calls for accurate statistics.
- **Reference Genome**: Must match the reference used for alignment.
- **Coverage Requirements**: Depends on sufficient sequencing coverage.
- **Filtering Parameters**: Appropriate thresholds must be set.
- **Memory Usage**: May require significant memory for large datasets.

## Examples

### Identify callable regions
**Args:** `clam callable -b alignments.bam -o callable_regions.bed`
**Explanation:** Identifies callable genomic regions from BAM file.

### Calculate population statistics
**Args:** `clam stats -v genotypes.vcf -o statistics.txt`
**Explanation:** Calculates population genetic statistics from VCF.

### Filter variants by callability
**Args:** `clam filter -v genotypes.vcf -c callable.bed -o filtered.vcf`
**Explanation:** Filters variants based on callable regions.

### Display help
**Args:** `clam --help`
**Explanation:** Shows all available options and usage information.