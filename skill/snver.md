---
name: snver
category: utility
description: SNVer is a statistical tool for calling common and rare variants in analysis of pool or individual next-generation sequencing data. It reports one single overall p-value for evaluating the significance of a candidate locus being a variant, based on which multiplicity control can be obtained. Loci with any (low) coverage can be tested and depth of coverage will be quantitatively factored into final significance calculation. SNVer runs very fast, making it feasible for analysis of whole-exome sequencing data, or even whole-genome sequencing data.
tags: [snver, utility]
author: oxo-call-community
source_url: "http://snver.sourceforge.net/"
---

## Concepts

- **Tool Overview**: snver (v0.5.3) - SNVer is a statistical tool for calling common and rare variants in analysis of pool or individual next-generation sequencing data. It reports one single overall p-value for evaluating the significance of a candidate locus being a variant, based on which multiplicity control can be obtained. Loci with any (low) coverage can be tested and depth of coverage will be quantitatively factored into final significance calculation. SNVer runs very fast, making it feasible for analysis of whole-exome sequencing data, or even whole-genome sequencing data.
- **Core Function**: SNVer is a statistical tool for calling common and rare variants in analysis of pool or individual next-generation sequencing data. It reports one single overall p-value for evaluating the significance of a candidate locus being a variant, based on which multiplicity control can be obtained. Loci with any (low) coverage can be tested and depth of coverage will be quantitatively factored into final significance calculation. SNVer runs very fast, making it feasible for analysis of whole-exome sequencing data, or even whole-genome sequencing data.
- **Input/Output**: Depends on tool configuration and input data format.
- **Installation**: `conda install -c bioconda snver`

## Pitfalls

- **Version Differences**: Options may vary between versions; always check with --help.
- **Input Format**: Ensure correct input format before running.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options and usage information.

### Basic usage
**Args:** `snver -i <input_file> -o <output_file>`
**Explanation:** Run snver with typical input and output options.
