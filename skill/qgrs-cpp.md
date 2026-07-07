---
name: qgrs-cpp
category: alignment
description: QGRS-cpp is a C++ implementation of QGRS (Quadruplex G-Rich Sequence) mapping for nucleic acid analysis.
tags: [qgrs-cpp, alignment, qgrs, quadruplex]
author: oxo-call-community
source_url: "https://github.com/freezer333/qgrs-cpp"
---

## Concepts

- **Tool Overview**: qgrs-cpp maps G-quadruplex sequences.
- **Core Function**: QGRS detection.
- **Algorithm**: Uses pattern matching.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces QGRS positions.
- **Use Case**: Genomic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Pattern Parameters**: Must be configured.
- **Sequence Quality**: Affects detection.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qgrs-cpp --help`
**Explanation:** Shows available options and usage instructions.

### Run QGRS mapping
**Args:** `qgrs-cpp map -i sequence.fasta -o qgrs_positions.txt`
**Explanation:** Maps QGRS in sequences.

### With parameters
**Args:** `qgrs-cpp map -i sequence.fasta -p params.yaml -o qgrs_positions.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qgrs-cpp -v map -i sequence.fasta -o qgrs_positions.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qgrs-cpp -t 4 map -i sequence.fasta -o qgrs_positions.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Specific pattern
**Args:** `qgrs-cpp map -i sequence.fasta -p 3 -o qgrs_positions.txt`
**Explanation:** Uses specific pattern size.

### Generate report
**Args:** `qgrs-cpp map -i sequence.fasta -o qgrs_positions.txt --report report.html`
**Explanation:** Generates HTML report.