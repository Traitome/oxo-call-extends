---
name: repermulize
category: utility
description: Repermulize performs gene-to-phenotype tests with permutation for association studies.
tags: [repermulize, utility, gene-phenotype, permutation-testing]
author: oxo-call-community
source_url: "https://github.com/pbradleylab/repermulize"
---

## Concepts

- **Tool Overview**: repermulize tests associations.
- **Core Function**: Gene-to-phenotype association testing.
- **Algorithm**: Uses permutation methods.
- **Input Format**: Accepts genotype-phenotype data.
- **Output**: Produces association results.
- **Use Case**: Genetic association studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Affects testing.
- **Parameters**: Must be configured.
- **Runtime**: Testing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `repermulize --help`
**Explanation:** Shows available options and usage instructions.

### Run association test
**Args:** `repermulize test -g genotypes.txt -p phenotypes.txt -o results.txt`
**Explanation:** Performs gene-to-phenotype association test.

### With parameters
**Args:** `repermulize test -g genotypes.txt -p phenotypes.txt -pa params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `repermulize -v test -g genotypes.txt -p phenotypes.txt -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `repermulize -t 4 test -g genotypes.txt -p phenotypes.txt -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With permutations
**Args:** `repermulize test -g genotypes.txt -p phenotypes.txt -n 10000 -o results.txt`
**Explanation:** Uses 10000 permutations.

### Generate report
**Args:** `repermulize test -g genotypes.txt -p phenotypes.txt -o results.txt --report report.html`
**Explanation:** Generates HTML report.