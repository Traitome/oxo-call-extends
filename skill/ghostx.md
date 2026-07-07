---
name: ghostx
category: homology-search
description: ghostx - Fast homology search tool using suffix arrays, 100x faster than BLAST.
tags: [ghostx, homology-search, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "http://www.bi.cs.titech.ac.jp/ghostx/"
---

## Concepts
- **Homology Detection**: Detects remote homologues.
- **Suffix Arrays**: Uses suffix array algorithm.
- **Fast Search**: 100x faster than BLAST.
- **BLAST-like Output**: Produces BLAST-style output.
- **Sequence Alignment**: Aligns sequences.

## Pitfalls
- **Database Size**: Large databases require memory.
- **Index Building**: Index building is time-consuming.
- **Parameter Tuning**: Requires parameter optimization.
- **Sensitivity**: May miss very divergent homologues.
- **Memory Usage**: Requires significant memory.

## Examples
### Build index
**Args:** `ghostx index -d database.fasta -o database`
**Explanation:** Builds suffix array index.

### Search homologues
**Args:** `ghostx search -d database -q query.fasta -o results.txt`
**Explanation:** Searches for homologues.

### With options
**Args:** `ghostx search -d database -q query.fasta -e 1e-5 -o results.txt`
**Explanation:** Uses e-value threshold.

### Batch search
**Args:** `ghostx search -d database -l queries.txt -o ./results/`
**Explanation:** Searches multiple queries.

### Generate report
**Args:** `ghostx search -d database -q query.fasta -r -o report.html`
**Explanation:** Generates search report.