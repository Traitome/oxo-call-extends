---
name: ilesta
category: assembly
description: De novo genome assembler for long-read sequencing data.
tags: [ilesta, genome assembly, long-read, PacBio, Nanopore]
author: oxo-call-community
source_url: "https://github.com/yvlaere/Ilesta"
---

## Concepts

- **Tool Overview**: Ilesta is a de novo genome assembler optimized for long-read sequencing data
- **Core Function**: Assembles raw long reads into contiguous sequences (contigs)
- **Input/Output**: Accepts FASTA/FASTQ long-read data; outputs assembled contigs
- **Installation**: `conda install -c bioconda ilesta`
- **Key Features**: Optimized for PacBio and Nanopore data, handles complex genomes, efficient memory usage

## Pitfalls

- **Read Quality**: Requires high-quality long reads for optimal results
- **Computational Resources**: Assembly of large genomes requires significant CPU and memory
- **Parameter Tuning**: Optimal parameters depend on read length and genome complexity
- **Error Correction**: Raw long reads may need preprocessing for error correction
- **Genome Size**: Estimating genome size correctly affects assembly performance

## Examples

### Basic de novo assembly
**Args:** `ilesta -i reads.fastq -o assembly`
**Explanation:** Assembles long reads into contigs with default parameters.

### Specify genome size estimate
**Args:** `ilesta -i reads.fastq -o assembly -g 3000000000`
**Explanation:** Provides estimated genome size (3GB) for improved assembly.

### Use multiple threads
**Args:** `ilesta -i reads.fastq -o assembly -t 16`
**Explanation:** Uses 16 threads for parallel processing.

### Include short reads for polishing
**Args:** `ilesta -i long_reads.fastq -s short_reads.fastq -o assembly`
**Explanation:** Incorporates short reads for assembly polishing.

### Set minimum contig length
**Args:** `ilesta -i reads.fastq -o assembly -m 1000`
**Explanation:** Filters out contigs shorter than 1000 bp.
