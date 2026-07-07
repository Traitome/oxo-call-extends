---
name: pirs
category: utility
description: pirs simulates Illumina paired-end reads.
tags: [pirs, utility, simulation, illumina]
author: oxo-call-community
source_url: "https://github.com/galaxy001/pirs"
---

## Concepts

- **Tool Overview**: pirs simulates Illumina PE reads.
- **Core Function**: Read simulation for sequencing data.
- **Algorithm**: Uses read simulation methods.
- **Input Format**: Accepts reference genome files.
- **Output**: Produces simulated FASTQ reads.
- **Use Case**: Read simulation, benchmarking.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Reference Quality**: Results depend on reference quality.
- **Simulation Accuracy**: May have simulation errors.
- **Runtime**: Simulation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pirs --help`
**Explanation:** Shows available options and usage instructions.

### Simulate reads
**Args:** `pirs -i reference.fasta -o simulated_reads.fastq`
**Explanation:** Simulates Illumina paired-end reads.

### With parameters
**Args:** `pirs -i reference.fasta -p params.yaml -o simulated_reads.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pirs -v -i reference.fasta -o simulated_reads.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pirs -t 4 -i reference.fasta -o simulated_reads.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pirs -i reference.fasta -o simulated_reads.fastq --paired`
**Explanation:** Outputs paired-end reads.

### Generate report
**Args:** `pirs -i reference.fasta -o simulated_reads.fastq --report report.html`
**Explanation:** Generates HTML report.