---
name: reframed
category: containerization
description: Reframed is a metabolic modeling package for constraint-based reconstruction and analysis.
tags: [reframed, containerization, metabolic-modeling, constraint-based-analysis]
author: oxo-call-community
source_url: "https://github.com/cdanielmachado/reframed"
---

## Concepts

- **Tool Overview**: reframed models metabolism.
- **Core Function**: Metabolic modeling.
- **Algorithm**: Uses optimization methods.
- **Input Format**: Accepts model files.
- **Output**: Produces metabolic predictions.
- **Use Case**: Systems biology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large models require memory.
- **Model Quality**: Affects predictions.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reframed --help`
**Explanation:** Shows available options and usage instructions.

### Analyze model
**Args:** `reframed analyze -i model.xml -o results.txt`
**Explanation:** Analyzes metabolic model.

### With parameters
**Args:** `reframed analyze -i model.xml -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reframed -v analyze -i model.xml -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reframed -t 4 analyze -i model.xml -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With FBA
**Args:** `reframed analyze -i model.xml -m fba -o results.txt`
**Explanation:** Uses flux balance analysis.

### Generate report
**Args:** `reframed analyze -i model.xml -o results.txt --report report.html`
**Explanation:** Generates HTML report.