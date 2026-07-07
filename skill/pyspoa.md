---
name: pyspoa
category: programming
description: PySpoa is the Python binding to the spoa library for sequence alignment and consensus generation.
tags: [pyspoa, programming, alignment, consensus]
author: oxo-call-community
source_url: "https://github.com/nanoporetech/spoa"
---

## Concepts

- **Tool Overview**: pyspoa aligns sequences.
- **Core Function**: Sequence alignment.
- **Algorithm**: Uses POA.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces alignments.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Count**: May have limits.
- **Alignment Quality**: Depends on parameters.
- **Runtime**: Alignment may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyspoa --help`
**Explanation:** Shows available options and usage instructions.

### Align sequences
**Args:** `pyspoa align -i sequences.fasta -o alignment.fasta`
**Explanation:** Aligns sequences.

### With parameters
**Args:** `pyspoa align -i sequences.fasta -p params.yaml -o alignment.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyspoa -v align -i sequences.fasta -o alignment.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyspoa -t 4 align -i sequences.fasta -o alignment.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Generate consensus
**Args:** `pyspoa consensus -i sequences.fasta -o consensus.fasta`
**Explanation:** Generates consensus sequence.

### Generate report
**Args:** `pyspoa align -i sequences.fasta -o alignment.fasta --report report.html`
**Explanation:** Generates HTML report.