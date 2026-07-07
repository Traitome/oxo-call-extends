---
name: prymer
category: genome-editing
description: prymer is a Python library for primer design and optimization.
tags: [prymer, genome-editing, primer-design, python]
author: oxo-call-community
source_url: "https://prymer.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: prymer designs PCR primers.
- **Core Function**: Primer design.
- **Algorithm**: Uses thermodynamic calculations.
- **Input Format**: Accepts DNA sequences.
- **Output**: Produces primer sequences.
- **Use Case**: PCR primer design.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **Data Quality**: Results depend on input quality.
- **Primer Specificity**: May affect PCR.
- **Runtime**: Design may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prymer --help`
**Explanation:** Shows available options and usage instructions.

### Design primers
**Args:** `prymer design -i target.fasta -o primers.txt`
**Explanation:** Designs PCR primers for target sequence.

### With parameters
**Args:** `prymer design -i target.fasta -p params.yaml -o primers.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prymer -v design -i target.fasta -o primers.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prymer -t 4 design -i target.fasta -o primers.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Primer optimization
**Args:** `prymer optimize -i primers.txt -o optimized.txt`
**Explanation:** Optimizes existing primers.

### Generate report
**Args:** `prymer design -i target.fasta -o primers.txt --report report.html`
**Explanation:** Generates HTML report.