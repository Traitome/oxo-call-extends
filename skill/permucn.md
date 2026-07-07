---
name: permucn
category: utility
description: permucn tests copy-number and binary trait association.
tags: [permucn, utility, copy-number, association]
author: oxo-call-community
source_url: "https://github.com/mkrg01/permucn"
---

## Concepts

- **Tool Overview**: permucn tests CNV associations.
- **Core Function**: Performs permutation-based testing.
- **Algorithm**: Uses permutation statistical methods.
- **Input Format**: Accepts CNV and trait data.
- **Output**: Produces association test results.
- **Use Case**: CNV analysis, association testing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **CNV Quality**: Results depend on CNV quality.
- **Permutation Number**: Requires sufficient permutations.
- **Runtime**: Testing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `permucn --help`
**Explanation:** Shows available options and usage instructions.

### Test association
**Args:** `permucn -i cnv_data.txt -t traits.txt -o results.txt`
**Explanation:** Tests CNV-trait association.

### With permutations
**Args:** `permucn -i cnv_data.txt -t traits.txt -n 1000 -o results.txt`
**Explanation:** Uses 1000 permutations for testing.

### Verbose mode
**Args:** `permucn -v -i cnv_data.txt -t traits.txt -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `permucn -t 4 -i cnv_data.txt -t traits.txt -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `permucn -i cnv_data.txt -t traits.txt -o results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `permucn -i cnv_data.txt -t traits.txt -o results.txt --report report.html`
**Explanation:** Generates HTML report.