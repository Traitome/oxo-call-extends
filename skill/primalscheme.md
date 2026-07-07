---
name: primalscheme
category: genome-editing
description: primalscheme designs primer panels for multiplex PCR.
tags: [primalscheme, genome-editing, primers, pcr]
author: oxo-call-community
source_url: "https://github.com/aresti/primalscheme"
---

## Concepts

- **Tool Overview**: primalscheme designs primers.
- **Core Function**: Primer panel design.
- **Algorithm**: Uses thermodynamic methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces primer sets.
- **Use Case**: Multiplex PCR, amplicon sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on sequence quality.
- **Primer Specificity**: May have off-target binding.
- **Runtime**: Design may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `primalscheme --help`
**Explanation:** Shows available options and usage instructions.

### Design primers
**Args:** `primalscheme design -i target.fasta -o primers.csv`
**Explanation:** Designs primer panel for target region.

### With parameters
**Args:** `primalscheme design -i target.fasta -p params.yaml -o primers.csv`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `primalscheme -v design -i target.fasta -o primers.csv`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `primalscheme -t 4 design -i target.fasta -o primers.csv`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `primalscheme design -i target.fasta -o primers.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `primalscheme design -i target.fasta -o primers.csv --report report.html`
**Explanation:** Generates HTML report.