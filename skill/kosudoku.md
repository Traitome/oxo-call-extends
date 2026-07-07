---
name: kosudoku
category: genetics
description: Suite for creating whole genome knockout collections in microorganisms
tags: [kosudoku, genetics, knockout, transposon, microbial-genetics]
author: oxo-call-community
source_url: "https://github.com/tuncK/kosudoku"
---

## Concepts

- **Whole Genome Knockout**: Creates comprehensive knockout collections
- **Transposon Mutagenesis**: Uses transposon-based approaches
- **Microbial Genetics**: Specialized for microorganisms
- **High-throughput**: Enables large-scale knockout screening
- **Sequencing Analysis**: Integrates with sequencing analysis
- **Fitness Profiling**: Supports fitness profiling of mutants

## Pitfalls

- **Insertion Bias**: Transposon insertion has sequence biases
- **Essential Genes**: Essential genes cannot be knocked out
- **Growth Conditions**: Knockout fitness depends on conditions
- **Library Complexity**: Large libraries require careful QC
- **Mapping Accuracy**: Accurate insertion site mapping is critical
- **Statistical Analysis**: Requires proper statistical methods

## Examples

### Create knockout library
**Args:** `kosudoku create -i genome.fasta -o library/`
**Explanation:** Creates whole genome knockout library.

### Specify transposon
**Args:** `kosudoku create -i genome.fasta -tTn5 -o library/`
**Explanation:** Uses Tn5 transposon for mutagenesis.

### Analyze insertions
**Args:** `kosudoku analyze -i library.saf -o results/`
**Explanation:** Analyzes transposon insertion sites.

### Fitness profiling
**Args:** `kosudoku fitness -i library/ -c conditions.txt -o fitness.tsv`
**Explanation:** Profiles fitness under different conditions.

### Map insertions
**Args:** `kosudoku map -i reads.fastq -g genome.fasta -o insertions.bed`
**Explanation:** Maps transposon insertion locations.

### Batch analysis
**Args:** `kosudoku batch -d libraries/ -o results/`
**Explanation:** Processes multiple knockout libraries.