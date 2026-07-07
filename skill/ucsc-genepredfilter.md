---
name: ucsc-genepredfilter
category: utility
description: UCSC genePredFilter - Tool for filtering gene predictions.
tags: [ucsc-genepredfilter, ucsc, gene-prediction, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://genome.ucsc.edu/"
---

## Concepts

- **Tool Overview**: UCSC genePredFilter - A tool for filtering gene predictions.
- **Core Function**: Filters gene predictions based on various criteria.
- **Input**: Gene prediction file.
- **Output**: Filtered gene predictions.
- **Installation**: Part of UCSC utilities
- **Use Case**: Gene filtering, quality control, annotation refinement.

## Pitfalls

- **Filter Criteria**: Requires appropriate filter parameters.
- **Memory**: May require significant memory for large files.

## Examples

### Filter gene predictions
**Args:** `genePredFilter -minExons=3 genes.txt > filtered.txt`
**Explanation:** Filter by minimum exons.

### With multiple filters
**Args:** `genePredFilter -minExons=3 -minScore=100 genes.txt > filtered.txt`
**Explanation:** Multiple filter criteria.
