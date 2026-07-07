---
name: vcfdist
category: bioinformatics
description: vcfdist - VCF distance calculation tool.
tags: [vcfdist, vcf-processing, distance-calculation, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vcfdist/"
---

## Concepts

- **Tool Overview**: vcfdist - A tool for calculating distances between VCF records.
- **Core Function**: Computes genetic distances between variants.
- **Input**: VCF file.
- **Output**: Distance matrix.
- **Installation**: Install via pip or conda
- **Use Case**: Population genetics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Time**: May be slow for many samples.

## Examples

### Calculate distances
**Args:** `vcfdist -i input.vcf -o distances.txt`
**Explanation:** Calculate variant distances.

### With options
**Args:** `vcfdist -i input.vcf -o distances.txt -m euclidean`
**Explanation:** Use Euclidean distance.
