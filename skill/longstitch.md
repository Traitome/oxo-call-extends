---
name: longstitch
category: assembly
description: LongStitch - Genome assembly correction and scaffolding using long reads
tags: [longstitch, assembly, scaffolding, genome-assembly, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/BirolLab/longstitch"
---

## Concepts

- **Assembly Correction**: Correcting draft genome assemblies
- **Scaffolding**: Ordering and orienting contigs
- **Long-read Data**: Using long reads for assembly improvement
- **Contig Integration**: Integrating short and long read assemblies
- **Gap Closing**: Closing gaps in assemblies
- **Quality Improvement**: Improving assembly quality

## Pitfalls

- **Read Quality**: Poor quality reads affect assembly
- **Contig Quality**: Poor quality contigs affect results
- **Memory Usage**: Memory-intensive for large genomes
- **Computational Time**: May be slow for large datasets
- **Parameter Tuning**: Requires careful parameter optimization
- **False Joins**: May produce incorrect scaffold joins

## Examples

### Run scaffolding
**Args:** `longstitch --contigs contigs.fasta --longreads reads.fastq --out scaffolded.fasta`
**Explanation:** Scaffolds contigs using long reads.

### Assembly correction
**Args:** `longstitch --contigs contigs.fasta --longreads reads.fastq --out corrected.fasta --correct`
**Explanation:** Corrects assembly errors.

### Threads
**Args:** `longstitch --contigs contigs.fasta --longreads reads.fastq --out scaffolded.fasta --threads 8`
**Explanation:** Uses 8 threads for parallel processing.

### Minimum length
**Args:** `longstitch --contigs contigs.fasta --longreads reads.fastq --out scaffolded.fasta --min-length 1000`
**Explanation:** Filters short contigs.

### Gap closing
**Args:** `longstitch --contigs contigs.fasta --longreads reads.fastq --out scaffolded.fasta --close-gaps`
**Explanation:** Closes gaps in assembly.

### Verbose output
**Args:** `longstitch --contigs contigs.fasta --longreads reads.fastq --out scaffolded.fasta --verbose`
**Explanation:** Provides detailed output.