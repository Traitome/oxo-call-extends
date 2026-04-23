---
name: kled
category: variant-calling
description: An ultra-fast and sensitive structural variant detection tool for long-read sequencing data.
tags: [kled, variant-calling, alignment, variant]
author: oxo-call-community
source_url: "https://github.com/CoREse/kled"
---

## Concepts

- **Tool Overview**: kled v1.2.11 - Kled is designed to call SVs nicely and quickly using long-read sequencing data. It takes mapped reads file (bam) as input and reports SVs to the stdout in the VCF file format. Kled can yield precise and comprehensive SV detection results within minutes and can run on any modern computer without needing of any field knowledge of the user to perform the SV detection..
- **Core Function**: An ultra-fast and sensitive structural variant detection tool for long-read sequencing data.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda kled`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Detect SVs
**Args:** `kled -i input.bam -o output.vcf`
**Explanation:** Detects structural variants from long-read BAM file.

