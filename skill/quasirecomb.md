---
name: quasirecomb
category: utility
description: QuasiRecomb infers quasispecies subjected to recombination from sequencing data.
tags: [quasirecomb, utility, quasispecies, recombination]
author: oxo-call-community
source_url: "https://github.com/cbg-ethz/QuasiRecomb"
---

## Concepts

- **Tool Overview**: quasirecomb infers quasispecies recombination.
- **Core Function**: Recombination analysis.
- **Algorithm**: Uses phylogenetic methods.
- **Input Format**: Accepts sequence alignments.
- **Output**: Produces recombination events.
- **Use Case**: Viral evolution.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Alignment Quality**: Must be high.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quasirecomb --help`
**Explanation:** Shows available options and usage instructions.

### Run inference
**Args:** `quasirecomb infer -i alignment.fasta -o recombination.txt`
**Explanation:** Infers recombination events.

### With parameters
**Args:** `quasirecomb infer -i alignment.fasta -p params.yaml -o recombination.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quasirecomb -v infer -i alignment.fasta -o recombination.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quasirecomb -t 4 infer -i alignment.fasta -o recombination.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With tree
**Args:** `quasirecomb infer -i alignment.fasta -t tree.newick -o recombination.txt`
**Explanation:** Uses provided tree.

### Generate report
**Args:** `quasirecomb infer -i alignment.fasta -o recombination.txt --report report.html`
**Explanation:** Generates HTML report.