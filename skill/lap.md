---
name: lap
category: assembly
description: De novo genome assembly evaluation tool
tags: [lap, assembly, genome-evaluation, assembly-quality, QC]
author: oxo-call-community
source_url: "https://github.com/TheSEGA/lap"
---

## Concepts

- **Assembly Evaluation**: Evaluates quality of de novo assemblies
- **Contig Assessment**: Assesses contiguity and completeness
- **Reference-free QC**: Can evaluate assemblies without reference
- **Quality Metrics**: Provides various quality metrics
- **Genome Coverage**: Estimates genome coverage
- **Assembly Comparison**: Compares multiple assemblies

## Pitfalls

- **Reference Dependency**: Some metrics require reference genome
- **Assembly Quality**: Low-quality assemblies give unreliable results
- **Parameter Selection**: Default parameters may not suit all genomes
- **Data Format**: Requires correct input format
- **Contamination**: Contamination affects evaluation accuracy
- **Species Specificity**: Parameters may need adjustment for different species

## Examples

### Evaluate assembly
**Args:** `lap -i assembly.fasta -o evaluation.txt`
**Explanation:** Evaluates genome assembly quality.

### Compare assemblies
**Args:** `lap compare -a assembly1.fasta -b assembly2.fasta -o comparison.txt`
**Explanation:** Compares two genome assemblies.

### Set reference
**Args:** `lap -i assembly.fasta -r reference.fasta -o results.txt`
**Explanation:** Uses reference genome for evaluation.

### Specify genome size
**Args:** `lap -i assembly.fasta -g 3000000000 -o results.txt`
**Explanation:** Specifies expected genome size in bp.

### Export metrics
**Args:** `lap -i assembly.fasta -o results.txt --format CSV`
**Explanation:** Exports evaluation metrics in CSV format.

### Batch evaluation
**Args:** `lap batch -d assemblies/ -o results/`
**Explanation:** Evaluates multiple assemblies.