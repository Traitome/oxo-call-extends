---
name: plast
category: utility
description: plast performs parallel local alignment search.
tags: [plast, utility, alignment, search]
author: oxo-call-community
source_url: "https://github.com/PLAST-software/plast-library"
---

## Concepts

- **Tool Overview**: plast performs high-performance sequence alignment.
- **Core Function**: Parallel local alignment search.
- **Algorithm**: Uses SIMD/multithreading optimization.
- **Input Format**: Accepts DNA/protein sequence files.
- **Output**: Produces alignment results.
- **Use Case**: Sequence comparison, homology search.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Alignment Accuracy**: May have alignment errors.
- **Runtime**: Search may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plast --help`
**Explanation:** Shows available options and usage instructions.

### Search sequences
**Args:** `plast search -i query.fasta -d database.fasta -o results.txt`
**Explanation:** Performs local alignment search.

### With parameters
**Args:** `plast search -i query.fasta -d database.fasta -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plast search -v -i query.fasta -d database.fasta -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plast search -t 4 -i query.fasta -d database.fasta -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plast search -i query.fasta -d database.fasta -o results.sam --sam`
**Explanation:** Outputs in SAM format.

### Generate report
**Args:** `plast search -i query.fasta -d database.fasta -o results.txt --report report.html`
**Explanation:** Generates HTML report.