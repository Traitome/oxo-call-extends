---
name: pbsim3
category: qc
description: PBSIM3 simulates PacBio and ONT long reads with advanced models.
tags: [pbsim3, qc, simulator, pacbio, ont]
author: oxo-call-community
source_url: "https://github.com/yukiteruono/pbsim3"
---

## Concepts

- **Tool Overview**: PBSIM3 simulates all long-read types.
- **Core Function**: Generates synthetic PacBio and ONT reads.
- **Algorithm**: Uses advanced error and quality models.
- **Input Format**: Accepts reference sequences.
- **Output**: Produces simulated FASTQ reads.
- **Use Case**: Benchmarking, method development.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Model Accuracy**: Simulated reads differ from real data.
- **Platform Selection**: Requires proper platform choice.
- **Runtime**: Simulation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pbsim3 --help`
**Explanation:** Shows available options and usage instructions.

### Simulate reads
**Args:** `pbsim3 --reference reference.fasta --prefix simulated`
**Explanation:** Simulates reads from reference.

### Simulate PacBio
**Args:** `pbsim3 --reference reference.fasta --prefix simulated --platform pacbio`
**Explanation:** Simulates PacBio HiFi reads.

### Simulate ONT
**Args:** `pbsim3 --reference reference.fasta --prefix simulated --platform ont`
**Explanation:** Simulates Oxford Nanopore reads.

### With depth
**Args:** `pbsim3 --reference reference.fasta --depth 50 --prefix simulated`
**Explanation:** Sets sequencing depth to 50x.

### Number of threads
**Args:** `pbsim3 --thread 8 --reference reference.fasta --prefix simulated`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pbsim3 --reference reference.fasta --prefix simulated --format fastq`
**Explanation:** Outputs in FASTQ format.