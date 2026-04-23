---
name: abyss
category: assembly
description: Assembly By Short Sequences - a de novo, parallel, paired-end short read sequence assembler.
tags: [abyss, assembly, de-novo, genome, parallel, mpi]
author: oxo-call-community
source_url: "https://github.com/BirolLab/abyss"
---

## Concepts

- **Tool Overview**: A de novo parallel paired-end short read sequence assembler for large genomes using distributed de Bruijn graphs. Version 2.3.10.
- **Core Function**: Assembles large genomes from short reads using a parallel MPI-based implementation of de Bruijn graph assembly.
- **Input/Output**: Input is FASTA/FASTQ reads (paired-end, mate-pair, linked-reads); output is contigs and scaffolds (FASTA).
- **Installation**: Install via bioconda: `conda install -c bioconda abyss`
- **Platform Support**: Linux (x86_64, ARM64) and macOS (Intel, Apple Silicon)
- **Main Command**: `abyss-pe` is the primary driver script implemented as a Makefile.
- **MPI Parallelization**: Uses MPI for distributed memory parallelism across multiple nodes/cores.
- **Bloom Filter Mode**: Supports Bloom filter assembly for memory-efficient large genome assembly.
- **Multiple Library Types**: Supports paired-end, mate-pair, linked-read, and long-read data for scaffolding.

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **K-mer Selection**: K-mer size (k parameter) critically affects assembly quality. Test multiple k-mer values.
- **Memory Requirements**: Large genomes require substantial memory. Use Bloom filter mode (`B` parameter) for memory efficiency.
- **MPI Configuration**: For multi-node runs, ensure MPI is properly configured. Use `np` parameter for single-node parallelization.
- **Temporary Space**: Assembly creates large temporary files. Set `TMPDIR` environment variable if /tmp is limited.
- **K-mer Coverage**: Low k-mer coverage leads to fragmented assemblies. Check coverage before assembly.

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available parameters and configuration options.

### Basic paired-end assembly
**Args:** `k=96 name=ecoli B=2G in='reads1.fa reads2.fa'`
**Explanation:** Assembles paired-end reads using 96-mers with 2GB Bloom filter memory budget. Output files are prefixed with 'ecoli'.

### Assembly with multiple libraries
**Args:** `k=96 B=2G name=sample lib='pe1 pe2' mp='mp1' pe1='pe1_1.fa pe1_2.fa' pe2='pe2_1.fa pe2_2.fa' mp1='mp1_1.fa mp1_2.fa'`
**Explanation:** Uses paired-end libraries (pe1, pe2) for contig assembly and mate-pair library (mp1) for scaffolding.

### Assembly with linked reads
**Args:** `k=96 B=2G name=sample pe='lra' pea='lra.fastq.gz' lr='lra' lra='lra.fastq.gz'`
**Explanation:** Uses linked-read data (10x Genomics) for improved scaffolding with barcode information.

### Assembly with specific k-mer and coverage threshold
**Args:** `k=64 kc=3 name=sample B=4G in='reads.fa'`
**Explanation:** Uses 64-mers with minimum k-mer count threshold of 3 to filter sequencing errors. Higher kc reduces errors but may miss low-coverage regions.

### Run with multiple threads on single node
**Args:** `k=96 name=sample np=8 j=4 in='reads1.fa reads2.fa'`
**Explanation:** Uses 8 MPI processes (`np=8`) with 4 threads per process (`j=4`) for parallel assembly on a single multi-core machine.

### Assembly statistics
**Args:** `abyss-fac sample-contigs.fa sample-scaffolds.fa`
**Explanation:** Calculates assembly contiguity statistics (N50, NG50, total length) for contigs and scaffolds.

### Test multiple k-mer values
**Args:** `-C k64 k=64 in='reads.fa' && -C k72 k=72 in='reads.fa' && -C k80 k=80 in='reads.fa'`
**Explanation:** Runs assemblies with different k-mer sizes in separate directories. Use `abyss-fac` to compare results and select best k-mer.
