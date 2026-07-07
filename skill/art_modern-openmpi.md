---
name: art_modern-openmpi
category: qc
description: ART_Morden with OpenMPI - Parallelized read simulator for diverse NGS platforms
tags: [art_modern-openmpi, qc, read-simulator, ngs, mpi, parallel]
author: oxo-call-community
source_url: "https://github.com/YU-Zhejian/art_modern/releases/download/1.4.0/art_modern.pdf"
---

## Concepts

- **Tool Overview**: ART_Morden with OpenMPI is a parallelized version of ART_Morden read simulator using Message Passing Interface for distributed computing. Version 1.4.0.
- **Core Function**: Simulates sequencing reads with realistic error models using multiple CPU cores or compute nodes for faster processing.
- **MPI Parallelization**: Uses OpenMPI to distribute simulation workload across multiple processors or nodes.
- **Platform Support**: Supports multiple NGS platforms including Illumina, PacBio, and Oxford Nanopore.
- **Scalability**: Scales performance with number of available cores. Suitable for large-scale simulations.
- **Error Modeling**: Incorporates platform-specific error profiles, quality score distributions, and read characteristics.
- **Input/Output**: Accepts reference genome FASTA and outputs simulated reads in FASTQ format.
- **Installation**: `conda install -c bioconda art_modern-openmpi` or compile with OpenMPI support.

## Pitfalls

- **MPI Configuration**: Requires properly configured OpenMPI environment. Check MPI installation and settings.
- **Core Allocation**: Performance depends on optimal core allocation. Too many cores may cause overhead.
- **Memory Scaling**: Parallel processing increases memory usage proportionally to core count.
- **File I/O**: Multiple processes writing to same file may cause contention. Use appropriate output strategy.
- **Cluster Requirements**: Designed for MPI-enabled clusters. May not provide benefits on single-core systems.

## Examples

### Display help
**Args:** `mpirun -n 4 art_morden_openmpi --help`
**Explanation:** Shows all available command-line options using 4 MPI processes.

### Parallel Illumina simulation
**Args:** `mpirun -n 8 art_morden_openmpi -i genome.fasta -p -l 150 -f 30 -m 200 -s 10 -o illumina_reads`
**Explanation:** Simulates paired-end Illumina reads using 8 MPI processes for parallel processing.

### Parallel PacBio simulation
**Args:** `mpirun -n 16 art_morden_openmpi -i genome.fasta -l 10000 -f 30 -ss HSII -o pacbio_reads`
**Explanation:** Simulates PacBio long reads using 16 MPI processes for improved performance.

### Specify read count with MPI
**Args:** `mpirun -n 4 art_morden_openmpi -i genome.fasta -c 1000000 -l 150 -o reads`
**Explanation:** Generates 1 million reads distributed across 4 MPI processes.

### Set quality score range
**Args:** `mpirun -n 8 art_morden_openmpi -i genome.fasta -l 150 -f 30 -qs 20 -qe 35 -o reads`
**Explanation:** Simulates reads with quality score range 20-35 using 8 processes.

### Add sequencing errors
**Args:** `mpirun -n 4 art_morden_openmpi -i genome.fasta -l 150 -f 30 -ir 0.001 -dr 0.0005 -sr 0.0002 -o reads`
**Explanation:** Simulates reads with specified error rates using 4 MPI processes.

### Use fixed random seed
**Args:** `mpirun -n 8 art_morden_openmpi -i genome.fasta -l 150 -f 30 -rs 12345 -o reproducible_reads`
**Explanation:** Uses fixed random seed for reproducible results across parallel runs.

### Cluster node allocation
**Args:** `mpirun -n 32 -host node1,node2,node3 art_morden_openmpi -i genome.fasta -l 150 -f 30 -o cluster_reads`
**Explanation:** Distributes simulation across 32 processes on multiple cluster nodes.