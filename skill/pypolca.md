---
name: pypolca
category: programming
description: PyPOLCA is a Python re-implementation of the POLCA genome assembly polisher from MaSuRCA.
tags: [pypolca, programming, assembly, polishing]
author: oxo-call-community
source_url: "https://github.com/gbouras13/pypolca"
---

## Concepts

- **Tool Overview**: pypolca polishes assemblies.
- **Core Function**: Genome polishing.
- **Algorithm**: Uses read alignment.
- **Input Format**: Accepts FASTA/BAM files.
- **Output**: Produces polished assembly.
- **Use Case**: Assembly improvement.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Read Coverage**: Affects polishing.
- **Read Quality**: Affects results.
- **Runtime**: Polishing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pypolca --help`
**Explanation:** Shows available options and usage instructions.

### Polish assembly
**Args:** `pypolca polish -i assembly.fasta -r reads.fastq -o polished.fasta`
**Explanation:** Polishes genome assembly.

### With parameters
**Args:** `pypolca polish -i assembly.fasta -p params.yaml -o polished.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pypolca -v polish -i assembly.fasta -o polished.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pypolca -t 4 polish -i assembly.fasta -o polished.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Multiple rounds
**Args:** `pypolca polish -i assembly.fasta -r reads.fastq -n 3 -o polished.fasta`
**Explanation:** Runs 3 polishing rounds.

### Generate report
**Args:** `pypolca polish -i assembly.fasta -o polished.fasta --report report.html`
**Explanation:** Generates HTML report.