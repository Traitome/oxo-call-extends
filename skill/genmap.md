---
name: genmap
category: alignment
description: GenMap - Ultra-fast computation of genome mappability.
tags: [genmap, mappability, genome-analysis, sequencing]
author: oxo-call-community
source_url: "https://github.com/cpockrandt/genmap/blob/genmap-v1.3.0/README.rst"
---

## Concepts
- **Mappability Calculation**: Computes genome mappability scores.
- **Read Mapping**: Determines how uniquely reads map to genome.
- **Genome Analysis**: Analyzes genome sequence for mappability.
- **Ultra-fast Computation**: Uses optimized algorithms for speed.
- **Coverage Analysis**: Supports coverage analysis.

## Pitfalls
- **Memory Usage**: Large genomes require significant memory.
- **Parameter Sensitivity**: Results depend on k-mer size and other parameters.
- **Computational Time**: Still requires time for large genomes.
- **Output Size**: Mappability files can be large.
- **Format Compatibility**: Requires specific input/output formats.

## Examples
### Compute mappability
**Args:** `genmap map -g genome.fasta -o mappability.bw`
**Explanation:** Computes mappability for genome.

### With custom k-mer size
**Args:** `genmap map -g genome.fasta -k 100 -o mappability.bw`
**Explanation:** Uses k-mer size of 100.

### Generate coverage
**Args:** `genmap coverage -g genome.fasta -o coverage.bw`
**Explanation:** Computes coverage track.

### Generate report
**Args:** `genmap map -g genome.fasta -r report.txt -o mappability.bw`
**Explanation:** Generates mappability report.

### Batch processing
**Args:** `genmap map -g ./genomes/ -o ./mappability/`
**Explanation:** Processes multiple genomes in batch.