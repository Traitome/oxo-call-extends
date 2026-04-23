---
name: mash
category: utility
description: Fast sequence distance estimator that uses MinHash.
tags: [mash, utility]
author: oxo-call-community
source_url: "https://github.com/marbl/Mash"
---

## Concepts

- **Tool Overview**: mash v2.3 - Fast sequence distance estimator that uses MinHash..
- **Core Function**: Fast sequence distance estimator that uses MinHash.
- **Input/Output**: Depends on tool function. Check documentation for details.
- **Installation**: `conda install -c bioconda mash`

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Format**: Ensure correct input format for your data.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows available options.

### Sketch genome
**Args:** `mash sketch -o output.msh input.fasta`
**Explanation:** Creates MinHash sketch of genome sequences.

### Compare genomes
**Args:** `mash dist sketch1.msh sketch2.msh`
**Explanation:** Computes Mash distance between two sketches.

