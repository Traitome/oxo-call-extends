---
name: ksnp
category: variant-calling
description: k-mer based haplotype assembly
tags: [ksnp, variant-calling]
author: oxo-call-community
source_url: "https://github.com/zhouqiansolab/KSNP"
---

## Concepts

- **Tool Overview**: ksnp v1.0.3 - k-mer based haplotype assembly.
- **Core Function**: k-mer based haplotype assembly
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda ksnp`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Call SNPs
**Args:** `kSNP3 -in input.list -outdir output -k 21`
**Explanation:** Calls SNPs from assembled genomes using 21-mers.

