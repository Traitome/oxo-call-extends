---
name: pbsim
category: qc
description: PBSIM simulates PacBio sequencing reads.
tags: [pbsim, qc, simulator, pacbio]
author: oxo-call-community
source_url: "https://code.google.com/archive/p/pbsim"
---

## Concepts

- **Tool Overview**: PBSIM simulates PacBio reads.
- **Core Function**: Generates synthetic PacBio sequencing data.
- **Algorithm**: Uses error profile simulation.
- **Input Format**: Accepts reference sequences.
- **Output**: Produces simulated FASTQ reads.
- **Use Case**: Benchmarking, method development.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Model Accuracy**: Simulated reads differ from real data.
- **Parameter Selection**: Requires proper parameter tuning.
- **Runtime**: Simulation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbsim --help`
**Explanation:** Shows available options and usage instructions.

### Simulate reads
**Args:** `pbsim --reference reference.fasta --prefix simulated`
**Explanation:** Simulates reads from reference.

### With depth
**Args:** `pbsim --reference reference.fasta --depth 20 --prefix simulated`
**Explanation:** Sets sequencing depth to 20x.

### Verbose mode
**Args:** `pbsim -v --reference reference.fasta --prefix simulated`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbsim --thread 4 --reference reference.fasta --prefix simulated`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pbsim --reference reference.fasta --prefix simulated --format fastq`
**Explanation:** Outputs in FASTQ format.

### Simulate CCS
**Args:** `pbsim --reference reference.fasta --prefix simulated --model-type ccs`
**Explanation:** Simulates CCS reads.