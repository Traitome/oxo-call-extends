---
name: rapidshapes
category: programming
description: RapidShapes computes a thermodynamic matcher (TDM) using runtime heuristics for probabilistic RNA shape analysis.
tags: [rapidshapes, programming, rna-structure, shape-analysis]
author: oxo-call-community
source_url: "https://bibiserv.cebitec.uni-bielefeld.de/rapidshapes"
---

## Concepts

- **Tool Overview**: rapidshapes analyzes RNA shapes.
- **Core Function**: RNA shape analysis.
- **Algorithm**: Uses thermodynamic methods.
- **Input Format**: Accepts RNA sequences.
- **Output**: Produces shape predictions.
- **Use Case**: RNA structure.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **Sequence Length**: Affects analysis.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rapidshapes --help`
**Explanation:** Shows available options and usage instructions.

### Analyze shapes
**Args:** `rapidshapes analyze -i rna.fasta -o shapes.txt`
**Explanation:** Analyzes RNA shapes.

### With parameters
**Args:** `rapidshapes analyze -i rna.fasta -p params.yaml -o shapes.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rapidshapes -v analyze -i rna.fasta -o shapes.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rapidshapes -t 4 analyze -i rna.fasta -o shapes.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With temperature
**Args:** `rapidshapes analyze -i rna.fasta -T 37 -o shapes.txt`
**Explanation:** Uses specific temperature.

### Generate report
**Args:** `rapidshapes analyze -i rna.fasta -o shapes.txt --report report.html`
**Explanation:** Generates HTML report.