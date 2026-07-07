---
name: newmap
category: alignment
description: NewMap creates mappability data for reference sequences to assess read mapping uniqueness.
tags: [newmap, alignment, mappability, genomics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/hoffmangroup/newmap"
---

## Concepts

- **Tool Overview**: NewMap generates mappability tracks for reference genomes.
- **Core Function**: Creates mappability data to identify uniquely mappable regions.
- **Algorithm**: Uses k-mer based approach to assess mapping uniqueness.
- **Input Format**: Accepts reference genome FASTA files.
- **Output**: Produces mappability tracks in various formats.
- **Use Case**: Variant calling quality control, read mapping assessment, and genome analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Requirements**: Requires indexed reference genome.
- **Computational Cost**: Large genomes require significant computation.
- **Memory Usage**: Processing large genomes requires memory.
- **k-mer Size**: Results depend on k-mer size parameter.
- **Output Size**: Mappability tracks can be large.

## Examples

### Display help
**Args:** `newmap --help`
**Explanation:** Shows available options and usage instructions.

### Generate mappability
**Args:** `newmap -r reference.fasta -k 36 -o mappability.bw`
**Explanation:** Generates mappability track with 36-mer.

### Multiple k-mer sizes
**Args:** `newmap -r reference.fasta -k 20,36,50 -o mappability/`
**Explanation:** Generates mappability for multiple k-mer sizes.

### BED output
**Args:** `newmap -r reference.fasta -k 36 --bed -o mappability.bed`
**Explanation:** Outputs mappability in BED format.

### BigWig output
**Args:** `newmap -r reference.fasta -k 36 --bigwig -o mappability.bw`
**Explanation:** Outputs mappability in BigWig format.

### Mask low mappability
**Args:** `newmap -r reference.fasta -k 36 -t 0.5 -o filtered.bw`
**Explanation:** Filters regions with mappability below 0.5.

### Threads
**Args:** `newmap -r reference.fasta -k 36 -t 8 -o mappability.bw`
**Explanation:** Uses 8 threads for parallel processing.