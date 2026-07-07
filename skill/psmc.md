---
name: psmc
category: population-genomics
description: psmc infers population size history from diploid sequences using the Pairwise Sequentially Markovian Coalescent model.
tags: [psmc, population-genomics, coalescent-theory, demography]
author: oxo-call-community
source_url: "https://github.com/lh3/psmc"
---

## Concepts

- **Tool Overview**: psmc analyzes population history.
- **Core Function**: Population size inference.
- **Algorithm**: Uses PSMC model.
- **Input Format**: Accepts consensus sequences.
- **Output**: Produces demographic history.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **Data Quality**: Results depend on input quality.
- **Model Assumptions**: May affect accuracy.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psmc --help`
**Explanation:** Shows available options and usage instructions.

### Infer population history
**Args:** `psmc -i consensus.fa -o psmc_results.txt`
**Explanation:** Infers population size history.

### With parameters
**Args:** `psmc -i consensus.fa -p "4+25*2+4+6" -o psmc_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psmc -v -i consensus.fa -o psmc_results.txt`
**Explanation:** Runs with verbose output.

### Number of iterations
**Args:** `psmc -i consensus.fa -n 100 -o psmc_results.txt`
**Explanation:** Uses 100 iterations.

### Bootstrap
**Args:** `psmc -i consensus.fa -b -o psmc_results.txt`
**Explanation:** Performs bootstrap analysis.

### Generate report
**Args:** `psmc -i consensus.fa -o psmc_results.txt --report report.html`
**Explanation:** Generates HTML report.