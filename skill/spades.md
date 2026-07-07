---
name: spades
category: assembly
description: SPAdes (St. Petersburg genome assembler) is intended for both standard isolates and single-cell MDA bacteria assemblies.
tags: [spades, assembly, genome, de-novo, sequencing]
author: oxo-call-community
source_url: "https://ablab.github.io/spades"
---

## Concepts

- **Tool Overview**: SPAdes (v4.2.0+) is a de novo genome assembler designed for standard isolates, single-cell MDA bacteria, and metagenomic assemblies. It uses an iterative de Bruijn graph approach with multiple k-mer sizes.
- **Core Function**: Assembles raw sequencing reads into contiguous sequences (contigs) and scaffolds using a multi-k-mer de Bruijn graph strategy.
- **Input/Output**: Input: FASTQ reads (paired-end, single-end, mate-pair). Output: Assembled contigs (contigs.fasta), scaffolds (scaffolds.fasta), and assembly graphs.
- **Algorithm**: Uses multiple k-mer sizes to handle different coverage depths and repeat regions, with graph simplification and error correction steps.
- **Key Features**: Supports Illumina, Ion Torrent, and PacBio reads; handles single-cell data; performs hybrid assembly; includes error correction.
- **Installation**: `conda install -c bioconda spades`

## Pitfalls

- **Memory Requirements**: SPAdes requires significant memory, especially for large genomes. Use `--memory` flag to limit memory usage.
- **K-mer Selection**: Choosing appropriate k-mer sizes is critical. SPAdes automatically selects k-mers based on read length, but manual selection may improve results.
- **Input Data**: Mixed read types require specific flags (--pe1, --pe2 for paired-end; --mp1 for mate-pair).
- **Runtime**: Assembly can be time-consuming for large datasets. Consider using `--threads` to parallelize.
- **Assembly Quality**: Check assembly statistics with QUAST or BUSCO after assembly.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Basic single-end assembly
**Args:** `-1 reads.fastq -o output_dir`
**Explanation:** Assembles single-end reads into contigs using default k-mer sizes.

### Paired-end assembly
**Args:** `-1 reads_1.fastq -2 reads_2.fastq -o output_dir`
**Explanation:** Assembles paired-end Illumina reads with automatic k-mer selection.

### Assembly with multiple k-mer sizes
**Args:** `-1 reads_1.fastq -2 reads_2.fastq -k 21,33,55 -o output_dir`
**Explanation:** Specifies custom k-mer sizes (21, 33, 55) for assembly, useful for complex genomes.

### Single-cell assembly
**Args:** `--sc -1 reads_1.fastq -2 reads_2.fastq -o output_dir`
**Explanation:** Runs SPAdes in single-cell mode optimized for MDA (Multiple Displacement Amplification) data.

### Metagenomic assembly
**Args:** `--meta -1 reads_1.fastq -2 reads_2.fastq -o output_dir`
**Explanation:** Runs SPAdes in metagenomic mode for assembling mixed microbial communities.

### Hybrid assembly with long reads
**Args:** `-1 short_1.fastq -2 short_2.fastq --pacbio long_reads.fastq -o output_dir`
**Explanation:** Combines short Illumina reads with long PacBio reads for improved contiguity.

### Assembly with memory limit
**Args:** `-1 reads_1.fastq -2 reads_2.fastq -o output_dir --memory 64`
**Explanation:** Limits SPAdes to 64GB of memory, useful for resource-constrained environments.

### Error correction only
**Args:** `--only-error-correction -1 reads_1.fastq -2 reads_2.fastq -o output_dir`
**Explanation:** Performs only error correction on reads without assembly, outputting corrected reads.