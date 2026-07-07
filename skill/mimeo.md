---
name: mimeo
category: utility
description: Scan genomes for internally repeated sequences, elements which are repetitive in another species, or high-identity HGT candidate regions between species.
tags: [mimeo, utility, hgt]
author: oxo-call-community
source_url: "https://github.com/Adamtaranto/mimeo"
---

## Concepts

- **Tool Overview**: mimeo v1.2.1 scans genomes for repeated sequences and HGT candidates.
- **Core Function**: Identifies repeated sequences and horizontal gene transfer candidates.
- **Repeat Detection**: Finds internally repeated sequences in genomes.
- **HGT Detection**: Identifies high-identity HGT candidate regions.
- **Input/Output**: Accepts genome sequences; outputs repeat and HGT predictions.
- **Comparative Genomics**: Supports comparative genomic analysis.

## Pitfalls

- **Computational Resources**: Processing large genomes may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal detection.
- **Data Quality**: Detection accuracy depends on input sequence quality.
- **Runtime**: Analysis of large genomes can be time-consuming.
- **False Positives**: May produce false positive HGT candidates.

## Examples

### Scan for repeats
**Args:** `mimeo -i genome.fasta -o repeats.txt`
**Explanation:** Scans genome for internally repeated sequences.

### Detect HGT candidates
**Args:** `mimeo -i genome.fasta -r reference.fasta -o hgt.txt`
**Explanation:** Identifies HGT candidates between species.

### With custom threshold
**Args:** `mimeo -i genome.fasta -o repeats.txt -t 0.95`
**Explanation:** Uses identity threshold of 0.95.

### Batch processing
**Args:** `mimeo -i fasta/ -o results/`
**Explanation:** Processes multiple genome files in batch mode.

### Detailed output
**Args:** `mimeo -i genome.fasta -o repeats.txt -v`
**Explanation:** Generates detailed repeat analysis report.