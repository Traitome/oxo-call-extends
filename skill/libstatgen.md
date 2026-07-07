---
name: libstatgen
category: statistics
description: libStatGen - C++ library for statistical genetics
tags: [libstatgen, statistics, genetics, C++, bioinformatics]
author: oxo-call-community
source_url: "https://genome.sph.umich.edu/wiki/C++_Library:_libStatGen"
---

## Concepts

- **Statistical Genetics**: Statistical analysis of genetic data
- **Data Processing**: Processing and manipulation of genetic datasets
- **Statistical Tests**: Implementation of statistical tests
- **File Formats**: Support for various genetic file formats
- **Quality Control**: Genetic data quality control
- **Association Studies**: Tools for genetic association studies

## Pitfalls

- **Memory Management**: Manual memory handling required in C++
- **Data Quality**: Poor quality data affects statistical results
- **Multiple Testing**: Requires proper multiple testing correction
- **Performance**: May require optimization for large datasets
- **Version Compatibility**: API may change between versions
- **Error Handling**: Requires careful error checking

## Examples

### Read VCF file
**Args:** `statgen read -i data.vcf -o data.dat`
**Explanation:** Reads VCF file into internal format.

### Quality control
**Args:** `statgen qc -i data.dat -o qc_report.txt`
**Explanation:** Performs quality control on genetic data.

### Association test
**Args:** `statgen assoc -i data.dat -p phenotype.txt -o results.txt`
**Explanation:** Runs association test.

### Filter variants
**Args:** `statgen filter -i data.vcf -q 30 -o filtered.vcf`
**Explanation:** Filters variants by quality.

### Compute statistics
**Args:** `statgen stats -i data.dat -o stats.txt`
**Explanation:** Computes descriptive statistics.

### Convert format
**Args:** `statgen convert -i data.vcf -o data.bed`
**Explanation:** Converts VCF to BED format.