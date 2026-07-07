---
name: reseq2
category: qc
description: ReSeq2 simulates realistic Illumina paired-end sequencing data.
tags: [reseq2, qc, sequencing-simulation, illumina]
author: oxo-call-community
source_url: "https://berntpopp.github.io/ReSeq2"
---

## Concepts

- **Tool Overview**: reseq2 simulates sequencing.
- **Core Function**: Illumina read simulation.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts reference genome.
- **Output**: Produces FASTQ reads.
- **Use Case**: Sequencing testing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Error Models**: Affect simulation.
- **Parameters**: Must be configured.
- **Runtime**: Simulation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reseq2 --help`
**Explanation:** Shows available options and usage instructions.

### Simulate reads
**Args:** `reseq2 simulate -i reference.fasta -o reads.fastq`
**Explanation:** Simulates Illumina paired-end reads.

### With parameters
**Args:** `reseq2 simulate -i reference.fasta -p params.yaml -o reads.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reseq2 -v simulate -i reference.fasta -o reads.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reseq2 -t 4 simulate -i reference.fasta -o reads.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With coverage
**Args:** `reseq2 simulate -i reference.fasta -c 30 -o reads.fastq`
**Explanation:** Simulates 30x coverage.

### Generate report
**Args:** `reseq2 simulate -i reference.fasta -o reads.fastq --report report.html`
**Explanation:** Generates HTML report.