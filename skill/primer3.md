---
name: primer3
category: qc
description: primer3 designs PCR primers from DNA sequences.
tags: [primer3, qc, primers, pcr]
author: oxo-call-community
source_url: "https://github.com/primer3-org/primer3"
---

## Concepts

- **Tool Overview**: primer3 designs PCR primers.
- **Core Function**: Primer design.
- **Algorithm**: Uses thermodynamic calculations.
- **Input Format**: Accepts FASTA/sequence files.
- **Output**: Produces primer sequences.
- **Use Case**: PCR assay design, sequencing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **Data Quality**: Results depend on input quality.
- **Primer Specificity**: May have mispriming.
- **Runtime**: Design may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `primer3_core --help`
**Explanation:** Shows available options and usage instructions.

### Design primers
**Args:** `primer3_core -i input.txt -o output.txt`
**Explanation:** Designs primers from input sequence.

### With parameters
**Args:** `primer3_core -i input.txt -p params.txt -o output.txt`
**Explanation:** Uses parameter file.

### Verbose mode
**Args:** `primer3_core -v -i input.txt -o output.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `primer3_core -t 4 -i input.txt -o output.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `primer3_core -i input.txt -o output.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `primer3_core -i input.txt -o output.txt --report report.html`
**Explanation:** Generates HTML report.