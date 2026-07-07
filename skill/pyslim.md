---
name: pyslim
category: utility
description: PySLiM manipulates tree sequences produced by the SLiM forward-time population genetics simulator.
tags: [pyslim, utility, population-genetics, tree-sequence]
author: oxo-call-community
source_url: "https://pyslim.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: pyslim manipulates tree sequences.
- **Core Function**: Tree sequence processing.
- **Algorithm**: Uses tskit.
- **Input Format**: Accepts .trees files.
- **Output**: Produces modified trees.
- **Use Case**: Population genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large trees require memory.
- **Tree Format**: Must be correct.
- **Time Units**: Must be consistent.
- **Runtime**: Processing may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyslim --help`
**Explanation:** Shows available options and usage instructions.

### Load tree
**Args:** `pyslim load -i simulation.trees -o output.trees`
**Explanation:** Loads and processes tree sequence.

### With parameters
**Args:** `pyslim load -i simulation.trees -p params.yaml -o output.trees`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyslim -v load -i simulation.trees -o output.trees`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyslim -t 4 load -i simulation.trees -o output.trees`
**Explanation:** Uses 4 threads for parallel processing.

### Simplify trees
**Args:** `pyslim simplify -i simulation.trees -o simplified.trees`
**Explanation:** Simplifies tree sequence.

### Generate report
**Args:** `pyslim load -i simulation.trees -o output.trees --report report.html`
**Explanation:** Generates HTML report.