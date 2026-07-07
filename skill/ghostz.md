---
name: ghostz
category: homology-search
description: ghostz - Highly efficient remote homologue detection tool.
tags: [ghostz, homology-search, sequence-analysis, bioinformatics]
author: oxo-call-community
source_url: "http://www.bi.cs.titech.ac.jp/ghostz"
---

## Concepts
- **Remote Homologue Detection**: Detects distant homologues.
- **Efficient Algorithm**: Uses efficient search algorithm.
- **Sequence Comparison**: Compares sequences.
- **Database Search**: Searches sequence databases.
- **Similarity Scoring**: Computes similarity scores.

## Pitfalls
- **Database Quality**: Requires high-quality database.
- **Parameter Selection**: Requires parameter optimization.
- **Computational Resources**: Requires computational resources.
- **Result Validation**: Results should be validated.
- **Memory Usage**: Large databases require memory.

## Examples
### Search homologues
**Args:** `ghostz search -d database.fasta -q query.fasta -o results.txt`
**Explanation:** Searches for homologues.

### With options
**Args:** `ghostz search -d database.fasta -q query.fasta -e 1e-10 -o results.txt`
**Explanation:** Uses e-value threshold.

### Build database
**Args:** `ghostz make -d sequences.fasta -o database`
**Explanation:** Creates search database.

### Batch search
**Args:** `ghostz search -d database -l queries.txt -o ./results/`
**Explanation:** Searches multiple queries.

### Generate report
**Args:** `ghostz search -d database -q query.fasta -r -o report.html`
**Explanation:** Generates search report.