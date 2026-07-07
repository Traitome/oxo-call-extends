---
name: primedrpa
category: genome-editing
description: primedrpa designs primers and probes for RPA assays.
tags: [primedrpa, genome-editing, rpa, primers]
author: oxo-call-community
source_url: "https://github.com/MatthewHiggins2017/bioconda-PrimedRPA"
---

## Concepts

- **Tool Overview**: primedrpa designs RPA reagents.
- **Core Function**: RPA primer/probe design.
- **Algorithm**: Uses RPA-specific methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces primer/probe sets.
- **Use Case**: Isothermal amplification, diagnostics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **Data Quality**: Results depend on input quality.
- **Assay Efficiency**: May require optimization.
- **Runtime**: Design may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `primedrpa --help`
**Explanation:** Shows available options and usage instructions.

### Design RPA primers
**Args:** `primedrpa -i target.fasta -o rpa_primers.txt`
**Explanation:** Designs RPA primers and probes.

### With parameters
**Args:** `primedrpa -i target.fasta -p params.yaml -o rpa_primers.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `primedrpa -v -i target.fasta -o rpa_primers.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `primedrpa -t 4 -i target.fasta -o rpa_primers.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `primedrpa -i target.fasta -o rpa_primers.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `primedrpa -i target.fasta -o rpa_primers.txt --report report.html`
**Explanation:** Generates HTML report.