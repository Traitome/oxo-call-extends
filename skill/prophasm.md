---
name: prophasm
category: assembly
description: prophasm compresses k-mer sets via assembling contigs for metagenomics.
tags: [prophasm, assembly, k-mer, metagenomics]
author: oxo-call-community
source_url: "https://github.com/prophyle/prophasm"
---

## Concepts

- **Tool Overview**: prophasm assembles k-mer sets.
- **Core Function**: K-mer compression via assembly.
- **Algorithm**: Uses de Bruijn graph methods.
- **Input Format**: Accepts k-mer files.
- **Output**: Produces contigs.
- **Use Case**: Metagenomics, sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **K-mer Size**: Affects assembly quality.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prophasm --help`
**Explanation:** Shows available options and usage instructions.

### Assemble k-mers
**Args:** `prophasm -i kmers.txt -o contigs.fasta`
**Explanation:** Assembles k-mer sets into contigs.

### With parameters
**Args:** `prophasm -i kmers.txt -p params.yaml -o contigs.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prophasm -v -i kmers.txt -o contigs.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prophasm -t 4 -i kmers.txt -o contigs.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prophasm -i kmers.txt -o contigs.gfa --gfa`
**Explanation:** Outputs in GFA format.

### Generate report
**Args:** `prophasm -i kmers.txt -o contigs.fasta --report report.html`
**Explanation:** Generates HTML report.