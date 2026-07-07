---
name: links
category: assembly
description: LINKS - Long Interval Nucleotide K-mer Scaffolder
tags: [links, assembly, scaffolding, k-mer, genome-assembly, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/BirolLab/LINKS"
---

## Concepts

- **Genome Scaffolding**: Scaffolding contigs into larger sequences
- **K-mer Matching**: Uses k-mer matching for scaffold construction
- **Long-range Information**: Incorporates long-range sequencing data
- **Contig Ordering**: Orders contigs based on k-mer overlaps
- **Gap Estimation**: Estimates gaps between contigs
- **Scaffold Improvement**: Improves existing scaffolds

## Pitfalls

- **K-mer Selection**: K-mer size affects scaffolding quality
- **Repeat Regions**: Repeat sequences may cause misassembly
- **Coverage Depth**: Requires sufficient sequencing coverage
- **Memory Usage**: Memory-intensive for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **Computational Time**: May be slow for large genomes

## Examples

### Scaffold assembly
**Args:** `LINKS -f contigs.fasta -k 21 -b output_prefix`
**Explanation:** Scaffolds contigs using k-mer size 21.

### Multiple k-mer sizes
**Args:** `LINKS -f contigs.fasta -k 21,31,41 -b output_prefix`
**Explanation:** Uses multiple k-mer sizes for scaffolding.

### Long reads
**Args:** `LINKS -f contigs.fasta -l long_reads.fasta -k 21 -b output_prefix`
**Explanation:** Incorporates long reads for scaffolding.

### Threads
**Args:** `LINKS -f contigs.fasta -k 21 -b output_prefix -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum overlap
**Args:** `LINKS -f contigs.fasta -k 21 -b output_prefix -m 5`
**Explanation:** Sets minimum k-mer overlap to 5.

### Output statistics
**Args:** `LINKS -f contigs.fasta -k 21 -b output_prefix -s`
**Explanation:** Outputs scaffolding statistics.