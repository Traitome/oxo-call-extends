---
name: moni
category: alignment
description: A Pangenomics Index for Finding MEMs
tags: [moni, alignment, pangenomics]
author: oxo-call-community
source_url: "https://github.com/maxrossi91/moni"
---

## Concepts

- **Tool Overview**: MONI v0.2.2 is a pangenomics index for finding Maximal Exact Matches.
- **Core Function**: Identifies MEMs across multiple genomes efficiently.
- **Pangenomics**: Designed for multi-genome analysis.
- **MEM Detection**: Finds maximal exact matches between sequences.
- **BWT-based**: Uses Burrows-Wheeler Transform for indexing.
- **Input/Output**: Accepts genome sequences; outputs MEMs.

## Pitfalls

- **Pangenomics Specific**: Designed for multiple genome analysis.
- **Memory Requirements**: Memory usage depends on genome complexity.
- **Parameter Tuning**: May require parameter adjustment for optimal performance.
- **Data Quality**: Results depend on sequence quality.
- **Index Building**: Requires time to build pangenome index.
- **Computational Resources**: Large pangenomes may require significant resources.

## Examples

### Build index
**Args:** `moni build -i genomes.fasta -o index/`
**Explanation:** Builds pangenome index from multiple genomes.

### Find MEMs
**Args:** `moni find -i index/ -q query.fasta -o mems.txt`
**Explanation:** Finds maximal exact matches in pangenome.

### With minimum length
**Args:** `moni find -i index/ -q query.fasta -m 50 -o mems.txt`
**Explanation:** Finds MEMs with minimum length of 50.

### Batch query
**Args:** `moni find -i index/ -q queries/ -o results/`
**Explanation:** Processes multiple query files.

### Index statistics
**Args:** `moni stats -i index/`
**Explanation:** Shows index statistics.