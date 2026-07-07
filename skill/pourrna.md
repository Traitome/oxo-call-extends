---
name: pourrna
category: utility
description: pourrna computes local minima and transition rates of RNA energy landscapes.
tags: [pourrna, utility, rna, energy-landscape]
author: oxo-call-community
source_url: "https://github.com/ViennaRNA/pourRNA"
---

## Concepts

- **Tool Overview**: pourrna analyzes RNA folding.
- **Core Function**: Energy landscape computation.
- **Algorithm**: Uses dynamic programming methods.
- **Input Format**: Accepts RNA sequence files.
- **Output**: Produces energy landscape data.
- **Use Case**: RNA structure prediction, folding analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex RNAs require memory.
- **Data Quality**: Results depend on sequence quality.
- **Computational Complexity**: May be computationally expensive.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pourRNA --help`
**Explanation:** Shows available options and usage instructions.

### Compute energy landscape
**Args:** `pourRNA -i rna.fasta -o energy.txt`
**Explanation:** Computes RNA energy landscape.

### With parameters
**Args:** `pourRNA -i rna.fasta -p params.yaml -o energy.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pourRNA -v -i rna.fasta -o energy.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pourRNA -t 4 -i rna.fasta -o energy.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pourRNA -i rna.fasta -o energy.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `pourRNA -i rna.fasta -o energy.txt --report report.html`
**Explanation:** Generates HTML report.