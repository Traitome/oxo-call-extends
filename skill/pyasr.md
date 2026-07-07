---
name: pyasr
category: programming
description: pyasr performs ancestral sequence reconstruction using Python for evolutionary analysis.
tags: [pyasr, programming, ancestral-reconstruction, phylogenetics]
author: oxo-call-community
source_url: "https://github.com/Zsailer/pyasr"
---

## Concepts

- **Tool Overview**: pyasr reconstructs ancestral sequences.
- **Core Function**: Ancestral sequence reconstruction.
- **Algorithm**: Uses phylogenetic methods.
- **Input Format**: Accepts alignments and trees.
- **Output**: Produces ancestral sequences.
- **Use Case**: Evolutionary biology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Tree Topology**: Affects reconstruction.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyasr --help`
**Explanation:** Shows available options and usage instructions.

### Reconstruct ancestors
**Args:** `pyasr reconstruct -i alignment.fasta -t tree.nwk -o ancestors.fasta`
**Explanation:** Reconstructs ancestral sequences.

### With parameters
**Args:** `pyasr reconstruct -i alignment.fasta -t tree.nwk -p params.yaml -o ancestors.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyasr -v reconstruct -i alignment.fasta -t tree.nwk -o ancestors.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyasr -t 4 reconstruct -i alignment.fasta -t tree.nwk -o ancestors.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Marginal reconstruction
**Args:** `pyasr marginal -i alignment.fasta -t tree.nwk -o marginal_probs.txt`
**Explanation:** Computes marginal probabilities.

### Generate report
**Args:** `pyasr reconstruct -i alignment.fasta -t tree.nwk -o ancestors.fasta --report report.html`
**Explanation:** Generates HTML report.