---
name: pbsim2
category: qc
description: PBSIM2 simulates long read sequencers with novel quality score models.
tags: [pbsim2, qc, simulator, long-reads]
author: oxo-call-community
source_url: "https://github.com/yukiteruono/pbsim2"
---

## Concepts

- **Tool Overview**: PBSIM2 simulates long reads.
- **Core Function**: Generates synthetic long-read data.
- **Algorithm**: Uses novel quality score generation model.
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
**Args:** `pbsim2 --help`
**Explanation:** Shows available options and usage instructions.

### Simulate reads
**Args:** `pbsim2 --reference reference.fasta --prefix simulated`
**Explanation:** Simulates reads from reference.

### With depth
**Args:** `pbsim2 --reference reference.fasta --depth 30 --prefix simulated`
**Explanation:** Sets sequencing depth to 30x.

### Verbose mode
**Args:** `pbsim2 -v --reference reference.fasta --prefix simulated`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pbsim2 --thread 8 --reference reference.fasta --prefix simulated`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `pbsim2 --reference reference.fasta --prefix simulated --format fastq`
**Explanation:** Outputs in FASTQ format.

### Simulate PacBio
**Args:** `pbsim2 --reference reference.fasta --prefix simulated --model-type pacbio`
**Explanation:** Simulates PacBio-style reads.