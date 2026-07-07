---
name: recon-para
category: hpc
description: RECON-PARA is a performance-optimized fork of RECON for de novo repeat family identification on HPC systems.
tags: [recon-para, hpc, repeat-detection, parallel-computing]
author: oxo-call-community
source_url: "http://eddylab.org/software/recon/"
---

## Concepts

- **Tool Overview**: recon-para identifies repeats.
- **Core Function**: Parallel repeat detection.
- **Algorithm**: Uses clustering methods.
- **Input Format**: Accepts genomic sequences.
- **Output**: Produces repeat families.
- **Use Case**: HPC repeat analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Sequence Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Detection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `recon-para --help`
**Explanation:** Shows available options and usage instructions.

### Identify repeats
**Args:** `recon-para identify -i genome.fasta -o repeat_families.txt`
**Explanation:** Identifies repeat families in parallel.

### With parameters
**Args:** `recon-para identify -i genome.fasta -p params.yaml -o repeat_families.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `recon-para -v identify -i genome.fasta -o repeat_families.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `recon-para -t 4 identify -i genome.fasta -o repeat_families.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With MPI
**Args:** `recon-para identify -i genome.fasta -m mpi -o repeat_families.txt`
**Explanation:** Uses MPI for distributed computing.

### Generate report
**Args:** `recon-para identify -i genome.fasta -o repeat_families.txt --report report.html`
**Explanation:** Generates HTML report.