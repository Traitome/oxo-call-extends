---
name: randfold
category: utility
description: RandFold performs minimum free energy folding randomization tests for RNA structure analysis.
tags: [randfold, utility, rna-structure, folding]
author: oxo-call-community
source_url: "http://bioinformatics.psb.ugent.be/software/details/Randfold"
---

## Concepts

- **Tool Overview**: randfold tests RNA structures.
- **Core Function**: Structure randomization.
- **Algorithm**: Uses folding methods.
- **Input Format**: Accepts RNA sequences.
- **Output**: Produces structure statistics.
- **Use Case**: RNA analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **Sequence Length**: Affects analysis.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `randfold --help`
**Explanation:** Shows available options and usage instructions.

### Run randomization
**Args:** `randfold randomize -i rna.fasta -o results.txt`
**Explanation:** Performs folding randomization.

### With parameters
**Args:** `randfold randomize -i rna.fasta -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `randfold -v randomize -i rna.fasta -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `randfold -t 4 randomize -i rna.fasta -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With iterations
**Args:** `randfold randomize -i rna.fasta -n 1000 -o results.txt`
**Explanation:** Uses 1000 randomizations.

### Generate report
**Args:** `randfold randomize -i rna.fasta -o results.txt --report report.html`
**Explanation:** Generates HTML report.