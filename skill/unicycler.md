---
name: unicycler
category: assembly
description: Unicycler - Hybrid genome assembly tool.
tags: [unicycler, genome-assembly, hybrid, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/rrwick/Unicycler"
---

## Concepts

- **Tool Overview**: Unicycler - A tool for hybrid genome assembly using short and long reads.
- **Core Function**: Assembles genomes from Illumina and long-read sequencing data.
- **Input**: Short reads (FASTQ), long reads (FASTQ).
- **Output**: Assembled genome (FASTA).
- **Installation**: Install via conda or source
- **Use Case**: Genome assembly, microbial genomics, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large genomes.
- **Computation Time**: May be slow for complex genomes.

## Examples

### Assemble genome
**Args:** `unicycler -1 reads_1.fastq -2 reads_2.fastq -l long_reads.fastq -o assembly/`
**Explanation:** Assemble genome from short and long reads.

### With options
**Args:** `unicycler -1 reads_1.fastq -2 reads_2.fastq -l long_reads.fastq -o assembly/ --min_fasta_length 1000`
**Explanation:** Set minimum contig length.
