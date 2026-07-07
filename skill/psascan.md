---
name: psascan
category: hpc
description: psascan is a parallel external memory suffix array construction algorithm for large sequences.
tags: [psascan, hpc, suffix-array, parallel-processing]
author: oxo-call-community
source_url: "https://www.cs.helsinki.fi/group/pads/pSAscan.html"
---

## Concepts

- **Tool Overview**: psascan builds suffix arrays.
- **Core Function**: Suffix array construction.
- **Algorithm**: Uses parallel external memory.
- **Input Format**: Accepts sequence files.
- **Output**: Produces suffix arrays.
- **Use Case**: Sequence indexing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **Data Quality**: Results depend on input quality.
- **Parallel Scaling**: May have overhead.
- **Runtime**: Construction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psascan --help`
**Explanation:** Shows available options and usage instructions.

### Build suffix array
**Args:** `psascan -i sequence.fasta -o suffix_array.txt`
**Explanation:** Constructs suffix array.

### With parameters
**Args:** `psascan -i sequence.fasta -p params.txt -o suffix_array.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psascan -v -i sequence.fasta -o suffix_array.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psascan -t 4 -i sequence.fasta -o suffix_array.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Memory mode
**Args:** `psascan --mem -i sequence.fasta -o suffix_array.txt`
**Explanation:** Runs in memory mode.

### Generate report
**Args:** `psascan -i sequence.fasta -o suffix_array.txt --report report.html`
**Explanation:** Generates HTML report.