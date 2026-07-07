---
name: ucsc-featurebits
category: utility
description: UCSC featureBits - Tool for manipulating feature bitmasks.
tags: [ucsc-featurebits, ucsc, features, bitmask, bioinformatics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC featureBits - A tool for manipulating feature bitmasks.
- **Core Function**: Creates and manipulates bitmask representations of features.
- **Input**: Feature file.
- **Output**: Bitmask file.
- **Installation**: Part of UCSC utilities
- **Use Case**: Feature analysis, genome annotation, bitwise operations.

## Pitfalls

- **Bitmask Size**: May require significant memory for large genomes.
- **Feature Format**: Requires proper feature format.

## Examples

### Create feature bits
**Args:** `featureBits -input=features.bed -output=bits.bb`
**Explanation:** Create feature bitmask.

### With options
**Args:** `featureBits -input=features.bed -mask=mask.bb -output=bits.bb`
**Explanation:** Create with masking.
