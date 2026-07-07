---
name: qhery
category: variant-calling
description: Qhery identifies mutations in SARS-CoV-2 associated with resistance to treatment.
tags: [qhery, variant-calling, sars-cov-2, mutations]
author: oxo-call-community
source_url: "http://github.com/mjsull/qhery/"
---

## Concepts

- **Tool Overview**: qhery detects resistance mutations.
- **Core Function**: Variant analysis.
- **Algorithm**: Uses pattern matching.
- **Input Format**: Accepts sequence files.
- **Output**: Produces mutation reports.
- **Use Case**: Viral analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Genome**: Must be correct.
- **Mutation Database**: Must be updated.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qhery --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `qhery analyze -i sequence.fasta -o mutations.txt`
**Explanation:** Identifies resistance mutations.

### With parameters
**Args:** `qhery analyze -i sequence.fasta -p params.yaml -o mutations.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qhery -v analyze -i sequence.fasta -o mutations.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qhery -t 4 analyze -i sequence.fasta -o mutations.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `qhery analyze -i sequence.fasta -r reference.fasta -o mutations.txt`
**Explanation:** Uses custom reference.

### Generate report
**Args:** `qhery analyze -i sequence.fasta -o mutations.txt --report report.html`
**Explanation:** Generates HTML report.