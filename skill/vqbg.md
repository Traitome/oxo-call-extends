---
name: vqbg
category: bioinformatics
description: VQBG - Variant quality benchmarking.
tags: [vqbg, variant-analysis, quality-control, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vqbg/"
---

## Concepts

- **Tool Overview**: VQBG - Variant quality benchmarking tool.
- **Core Function**: Evaluates variant calling quality.
- **Input**: VCF file.
- **Output**: Quality metrics.
- **Installation**: Install via pip or conda
- **Use Case**: Variant analysis, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Ground Truth**: Requires truth dataset.

## Examples

### Benchmark variants
**Args:** `vqbg -i calls.vcf -t truth.vcf -o metrics.txt`
**Explanation:** Benchmark variant calls.

### With options
**Args:** `vqbg -i calls.vcf -t truth.vcf -o metrics.txt -m sensitivity`
**Explanation:** Calculate sensitivity metrics.
