---
name: pbwt
category: formatting
description: pbwt provides Positional Burrows-Wheeler Transform for genome variation data.
tags: [pbwt, formatting, bwt, variation]
author: oxo-call-community
source_url: "https://github.com/richarddurbin/pbwt"
---

## Concepts

- **Tool Overview**: pbwt processes genome variation data.
- **Core Function**: Stores and computes on variation data.
- **Algorithm**: Uses positional BWT algorithm.
- **Input Format**: Accepts VCF/variation files.
- **Output**: Produces compressed variation data.
- **Use Case**: Population genetics, variation analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Format**: Requires proper variation format.
- **Computational Cost**: Analysis can be computationally intensive.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbwt --help`
**Explanation:** Shows available options and usage instructions.

### Build PBWT
**Args:** `pbwt build variants.vcf output.pbwt`
**Explanation:** Builds PBWT from VCF file.

### Query PBWT
**Args:** `pbwt query output.pbwt -o results.txt`
**Explanation:** Queries PBWT structure.

### Verbose mode
**Args:** `pbwt -v build variants.vcf output.pbwt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbwt -t 4 build variants.vcf output.pbwt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pbwt build variants.vcf output.pbwt --format binary`
**Explanation:** Outputs in binary format.

### Find matches
**Args:** `pbwt match output.pbwt -o matches.txt`
**Explanation:** Finds matching haplotypes.