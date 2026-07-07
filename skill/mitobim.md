---
name: mitobim
category: alignment
description: mitochondrial baiting and iterative mapping
tags: [mitobim, alignment, mitochondrial]
author: oxo-call-community
source_url: "https://github.com/chrishah/MITObim"
---

## Concepts

- **Tool Overview**: MITObim v1.9.1 performs mitochondrial baiting and iterative mapping.
- **Core Function**: Assembles mitochondrial genomes using baiting approach.
- **Baiting Strategy**: Uses reference sequences to 'bait' reads.
- **Iterative Mapping**: Iteratively maps reads to extend assembly.
- **Input/Output**: Accepts sequencing reads; outputs assembled mtDNA.
- **Mitochondrial Genomics**: Supports mitochondrial genome assembly.

## Pitfalls

- **Mitochondrial Specific**: Designed for mitochondrial assembly.
- **Computational Resources**: Processing may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal assembly.
- **Data Quality**: Results depend on input data quality.
- **Reference Dependence**: Requires appropriate bait sequences.

## Examples

### Assemble mitochondrial genome
**Args:** `mitobim --end1 reads_1.fastq --end2 reads_2.fastq --bait bait.fasta --output mito_assembly/`
**Explanation:** Runs mitochondrial assembly with baiting.

### With iterations
**Args:** `mitobim --end1 reads_1.fastq --end2 reads_2.fastq --bait bait.fasta --output mito_assembly/ --iterations 10`
**Explanation:** Specifies number of mapping iterations.

### Verbose output
**Args:** `mitobim --end1 reads_1.fastq --end2 reads_2.fastq --bait bait.fasta --output mito_assembly/ --verbose`
**Explanation:** Shows detailed assembly progress.

### Batch processing
**Args:** `mitobim --end1 fastq/*_1.fastq --end2 fastq/*_2.fastq --bait bait.fasta --output assemblies/`
**Explanation:** Processes multiple paired-end files.

### Generate report
**Args:** `mitobim --end1 reads_1.fastq --end2 reads_2.fastq --bait bait.fasta --output mito_assembly/ --report report.html`
**Explanation:** Generates assembly report.