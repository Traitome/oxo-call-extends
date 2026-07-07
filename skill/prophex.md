---
name: prophex
category: utility
description: prophex creates and queries k-mer indexes for sequence analysis.
tags: [prophex, utility, k-mer, indexing]
author: oxo-call-community
source_url: "https://github.com/prophyle/prophex"
---

## Concepts

- **Tool Overview**: prophex manages k-mer indexes.
- **Core Function**: K-mer index creation and querying.
- **Algorithm**: Uses efficient indexing methods.
- **Input Format**: Accepts FASTA/k-mer files.
- **Output**: Produces index files.
- **Use Case**: Sequence search, metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large indexes require memory.
- **Data Quality**: Results depend on input quality.
- **K-mer Size**: Affects index performance.
- **Runtime**: Indexing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prophex --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `prophex build -i sequences.fasta -o index.phx`
**Explanation:** Builds k-mer index from sequences.

### With parameters
**Args:** `prophex build -i sequences.fasta -p params.yaml -o index.phx`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prophex -v build -i sequences.fasta -o index.phx`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prophex -t 4 build -i sequences.fasta -o index.phx`
**Explanation:** Uses 4 threads for parallel processing.

### Query index
**Args:** `prophex query -i index.phx -q query.fasta -o results.txt`
**Explanation:** Queries k-mer index.

### Generate report
**Args:** `prophex build -i sequences.fasta -o index.phx --report report.html`
**Explanation:** Generates HTML report.