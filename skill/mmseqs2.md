---
name: mmseqs2
category: hpc
description: "MMseqs2: ultra fast and sensitive sequence search and clustering suite"
tags: [mmseqs2, hpc, alignment]
author: oxo-call-community
source_url: "https://github.com/soedinglab/mmseqs2"
---
## Concepts

- **Tool Overview**: MMseqs2 v18.8cc5c is an ultra-fast sequence search and clustering tool.
- **Core Function**: Performs fast and sensitive sequence homology search.
- **Sequence Clustering**: Supports efficient sequence clustering.
- **Performance**: Optimized for speed using SIMD instructions.
- **Input/Output**: Accepts sequence databases; outputs alignments or clusters.
- **Scalability**: Supports large-scale sequence analysis.

## Pitfalls

- **Database Requirements**: Requires pre-built sequence databases.
- **Memory Requirements**: Memory usage depends on database size.
- **Parameter Tuning**: May require parameter adjustment for sensitivity/speed tradeoff.
- **Data Quality**: Results depend on input sequence quality.
- **Index Building**: Requires time to build search indices.
- **Computational Resources**: Large-scale searches require significant resources.

## Examples

### Search sequences
**Args:** `mmseqs search query.fasta target.fasta result.m8 tmp/`
**Explanation:** Searches query sequences against target database.

### Create database
**Args:** `mmseqs createdb sequences.fasta db`
**Explanation:** Creates MMseqs2 database from FASTA file.

### Cluster sequences
**Args:** `mmseqs cluster db result tmp/`
**Explanation:** Clusters sequences in database.

### Align sequences
**Args:** `mmseqs align query.fasta target.fasta alignments.m8`
**Explanation:** Aligns query sequences to target.

### Batch processing
**Args:** `mmseqs search queries/ targets/ results/ tmp/`
**Explanation:** Processes multiple query files.