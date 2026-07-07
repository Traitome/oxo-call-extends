---
name: hapsolo
category: bioinformatics
description: HapSolo removes secondary haplotigs during diploid genome assembly and scaffolding.
tags: [hapsolo, genome-assembly, haplotigs, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/esolares/HapSolo"
---

## Concepts

- **Haplotig Removal**: HapSolo removes secondary haplotigs from assemblies.

- **Diploid Assembly**: Optimized for diploid genome assembly.

- **Scaffolding**: Aids in genome scaffolding process.

- **Assembly Optimization**: Optimizes genome assembly quality.

- **Haplotype Resolution**: Resolves haplotype-specific sequences.

- **Duplicate Removal**: Removes redundant haplotype sequences.

## Pitfalls

- **Assembly Quality**: Results depend on input assembly quality.

- **Haplotype Diversity**: High diversity may complicate analysis.

- **Parameter Tuning**: Requires careful parameter optimization.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large assemblies may require significant memory.

## Examples

### Remove haplotigs
**Args:** `hapsolo --assembly assembly.fasta --output cleaned.fasta`
**Explanation:** Removes secondary haplotigs from assembly.

### With read alignment
**Args:** `hapsolo --assembly assembly.fasta --bam alignments.bam --output cleaned.fasta`
**Explanation:** Uses read alignments for improved haplotig detection.

### Batch processing
**Args:** `for f in *.fasta; do hapsolo --assembly $f --output ${f%.fasta}_cleaned.fasta; done`
**Explanation:** Processes multiple assembly files.

### Generate statistics
**Args:** `hapsolo --assembly assembly.fasta --stats --output stats.txt`
**Explanation:** Generates assembly statistics.

### Quality filtering
**Args:** `hapsolo --assembly assembly.fasta --min-length 1000 --output cleaned.fasta`
**Explanation:** Filters contigs by minimum length.

### Visualization
**Args:** `hapsolo --assembly assembly.fasta --plot --output plot.pdf`
**Explanation:** Generates visualization of haplotig removal.

### Help command
**Args:** `hapsolo --help`
**Explanation:** Shows available options and usage information.