---
name: pywgsim
category: utility
description: PyWgsim is a Python wrapper for the wgsim short-read simulator.
tags: [pywgsim, utility, simulation, sequencing]
author: oxo-call-community
source_url: "https://github.com/ialbert/pywgsim"
---

## Concepts

- **Tool Overview**: pywgsim simulates sequencing reads.
- **Core Function**: Read simulation.
- **Algorithm**: Uses wgsim.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces simulated reads.
- **Use Case**: Data simulation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Parameters**: Must be configured.
- **Seed**: Affects reproducibility.
- **Runtime**: Simulation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pywgsim --help`
**Explanation:** Shows available options and usage instructions.

### Simulate reads
**Args:** `pywgsim simulate -i reference.fasta -o reads.fastq`
**Explanation:** Simulates sequencing reads.

### With parameters
**Args:** `pywgsim simulate -i reference.fasta -p params.yaml -o reads.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pywgsim -v simulate -i reference.fasta -o reads.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pywgsim -t 4 simulate -i reference.fasta -o reads.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Paired-end reads
**Args:** `pywgsim simulate -i reference.fasta -l 150 -o reads.fastq --paired`
**Explanation:** Generates paired-end reads.

### Generate report
**Args:** `pywgsim simulate -i reference.fasta -o reads.fastq --report report.html`
**Explanation:** Generates HTML report.