---
name: pmmrcalculator
category: programming
description: pmmrcalculator computes pairwise mismatch rates in EigenStrat datasets.
tags: [pmmrcalculator, programming, eigenstrat, genetics]
author: oxo-call-community
source_url: "https://github.com/TCLamnidis/pMMRCalculator"
---

## Concepts

- **Tool Overview**: pmmrcalculator calculates mismatch rates.
- **Core Function**: Pairwise mismatch rate computation.
- **Algorithm**: Uses statistical computation methods.
- **Input Format**: Accepts EigenStrat dataset files.
- **Output**: Produces mismatch rate matrix.
- **Use Case**: Population genetics, ancient DNA analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Computation Accuracy**: May have calculation errors.
- **Runtime**: Calculation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pmmrcalculator --help`
**Explanation:** Shows available options and usage instructions.

### Calculate mismatch rates
**Args:** `pmmrcalculator -i dataset -o mismatch.txt`
**Explanation:** Computes pairwise mismatch rates.

### With parameters
**Args:** `pmmrcalculator -i dataset -p params.yaml -o mismatch.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pmmrcalculator -v -i dataset -o mismatch.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pmmrcalculator -t 4 -i dataset -o mismatch.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pmmrcalculator -i dataset -o mismatch.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `pmmrcalculator -i dataset -o mismatch.txt --report report.html`
**Explanation:** Generates HTML report.