---
name: plmc
category: utility
description: plmc infers couplings in proteins and RNAs from sequence variation.
tags: [plmc, utility, protein, rna, coupling]
author: oxo-call-community
source_url: "https://github.com/debbiemarkslab/plmc"
---

## Concepts

- **Tool Overview**: plmc infers residue couplings.
- **Core Function**: Coupling inference from sequences.
- **Algorithm**: Uses statistical inference methods.
- **Input Format**: Accepts FASTA sequence files.
- **Output**: Produces coupling scores.
- **Use Case**: Protein structure prediction, RNA analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on alignment quality.
- **Inference Accuracy**: May have prediction errors.
- **Runtime**: Inference may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plmc --help`
**Explanation:** Shows available options and usage instructions.

### Infer couplings
**Args:** `plmc -i sequences.fasta -o couplings.txt`
**Explanation:** Infers couplings from sequence variation.

### With parameters
**Args:** `plmc -i sequences.fasta -p params.yaml -o couplings.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plmc -v -i sequences.fasta -o couplings.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plmc -t 4 -i sequences.fasta -o couplings.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plmc -i sequences.fasta -o couplings.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `plmc -i sequences.fasta -o couplings.txt --report report.html`
**Explanation:** Generates HTML report.