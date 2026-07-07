---
name: pysais
category: utility
description: PySAIS computes suffix arrays using the induced sorting algorithm for sequence analysis.
tags: [pysais, utility, suffix-array, sequence-analysis]
author: oxo-call-community
source_url: "https://bitbucket.org/alex-warwickvesztrocy/pysais"
---

## Concepts

- **Tool Overview**: pysais builds suffix arrays.
- **Core Function**: Suffix array computation.
- **Algorithm**: Uses induced sorting.
- **Input Format**: Accepts sequence files.
- **Output**: Produces suffix arrays.
- **Use Case**: Sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **Sequence Length**: May have limits.
- **Algorithm Choice**: Affects performance.
- **Runtime**: Computation may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pysais --help`
**Explanation:** Shows available options and usage instructions.

### Build suffix array
**Args:** `pysais build -i sequence.fasta -o suffix_array.txt`
**Explanation:** Computes suffix array.

### With parameters
**Args:** `pysais build -i sequence.fasta -p params.yaml -o suffix_array.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pysais -v build -i sequence.fasta -o suffix_array.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pysais -t 4 build -i sequence.fasta -o suffix_array.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Query suffix array
**Args:** `pysais query -i suffix_array.txt -p pattern.txt -o matches.txt`
**Explanation:** Searches pattern in suffix array.

### Generate report
**Args:** `pysais build -i sequence.fasta -o suffix_array.txt --report report.html`
**Explanation:** Generates HTML report.