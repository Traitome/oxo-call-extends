---
name: regain-cli
category: population-genomics
description: Regain-CLI is a Bayesian-network pipeline for ARG/virulence co-occurrence analysis.
tags: [regain-cli, population-genomics, bayesian-network, arg-analysis]
author: oxo-call-community
source_url: "https://github.com/ERBringHorvath/regain_CLI"
---

## Concepts

- **Tool Overview**: regain-cli analyzes co-occurrence.
- **Core Function**: ARG/virulence analysis.
- **Algorithm**: Uses Bayesian methods.
- **Input Format**: Accepts genomic data.
- **Output**: Produces co-occurrence results.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Affects analysis.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `regain-cli --help`
**Explanation:** Shows available options and usage instructions.

### Analyze co-occurrence
**Args:** `regain-cli analyze -i genomic_data.txt -o co_occurrence_results.txt`
**Explanation:** Analyzes ARG/virulence co-occurrence.

### With parameters
**Args:** `regain-cli analyze -i genomic_data.txt -p params.yaml -o co_occurrence_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `regain-cli -v analyze -i genomic_data.txt -o co_occurrence_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `regain-cli -t 4 analyze -i genomic_data.txt -o co_occurrence_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With network
**Args:** `regain-cli analyze -i genomic_data.txt -n network.pkl -o co_occurrence_results.txt`
**Explanation:** Uses pre-trained network.

### Generate report
**Args:** `regain-cli analyze -i genomic_data.txt -o co_occurrence_results.txt --report report.html`
**Explanation:** Generates HTML report.