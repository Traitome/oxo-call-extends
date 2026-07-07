---
name: recmpox
category: alignment
description: RecMpox flags potential recombination events in monkeypox consensus genomes for outbreak analysis.
tags: [recmpox, alignment, monkeypox, recombination-detection]
author: oxo-call-community
source_url: "https://github.com/DaanJansen94/RecMpox/blob/main/README.md"
---

## Concepts

- **Tool Overview**: recmpox detects recombination.
- **Core Function**: Recombination detection.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts monkeypox genomes.
- **Output**: Produces recombination flags.
- **Use Case**: Outbreak analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Genome Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Detection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `recmpox --help`
**Explanation:** Shows available options and usage instructions.

### Detect recombination
**Args:** `recmpox detect -i monkeypox_genomes.fasta -o recombination_flags.txt`
**Explanation:** Detects recombination events.

### With parameters
**Args:** `recmpox detect -i monkeypox_genomes.fasta -p params.yaml -o recombination_flags.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `recmpox -v detect -i monkeypox_genomes.fasta -o recombination_flags.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `recmpox -t 4 detect -i monkeypox_genomes.fasta -o recombination_flags.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `recmpox detect -i monkeypox_genomes.fasta -r reference.fasta -o recombination_flags.txt`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `recmpox detect -i monkeypox_genomes.fasta -o recombination_flags.txt --report report.html`
**Explanation:** Generates HTML report.