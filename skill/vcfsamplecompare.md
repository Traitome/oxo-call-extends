---
name: vcfsamplecompare
category: variant-calling
description: This script sorts and (optionally) filters the rows/variants of a VCF file (containing data for 2 or more samples) based on the differences in the variant data between samples or sample groups. Degree of "difference" is determined by either the best possible degree of separation of sample groups by genotype calls or the difference in average allelic frequency of each sample or sample group (with a gap size threshold). The pair of samples or sample groups used to represent the difference for a variant row is the one leading to the greatest difference in consistent genotype or average allelic frequencies (i.e. observation ratios, e.g. AO/DP) of the same variant state. If sample groups are not specified, the pair of samples leading to the greatest difference is greedily discovered and chosen to represent the variant/row.
tags: [vcfsamplecompare, variant-calling, vcf]
author: oxo-call-community
source_url: "https://github.com/hepcat72/vcfSampleCompare"
---

## Concepts

- **Tool Overview**: vcfsamplecompare (v2.013) - This script sorts and (optionally) filters the rows/variants of a VCF file (containing data for 2 or more samples) based on the differences in the variant data between samples or sample groups. Degree of "difference" is determined by either the best possible degree of separation of sample groups by genotype calls or the difference in average allelic frequency of each sample or sample group (with a gap size threshold). The pair of samples or sample groups used to represent the difference for a variant row is the one leading to the greatest difference in consistent genotype or average allelic frequencies (i.e. observation ratios, e.g. AO/DP) of the same variant state. If sample groups are not specified, the pair of samples leading to the greatest difference is greedily discovered and chosen to represent the variant/row.
- **Core Function**: This script sorts and (optionally) filters the rows/variants of a VCF file (containing data for 2 or more samples) based on the differences in the variant data between samples or sample groups. Degree of "difference" is determined by either the best possible degree of separation of sample groups by genotype calls or the difference in average allelic frequency of each sample or sample group (with a gap size threshold). The pair of samples or sample groups used to represent the difference for a variant row is the one leading to the greatest difference in consistent genotype or average allelic frequencies (i.e. observation ratios, e.g. AO/DP) of the same variant state. If sample groups are not specified, the pair of samples leading to the greatest difference is greedily discovered and chosen to represent the variant/row.
- **Input/Output**: Depends on specific tool functionality.
- **Installation**: `conda install -c bioconda vcfsamplecompare`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with `--help`.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `<input_file> -o <output_file>`
**Explanation:** Standard input/output pattern for most bioinformatics tools.
