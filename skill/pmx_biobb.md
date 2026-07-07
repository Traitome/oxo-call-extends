---
name: pmx_biobb
category: utility
description: pmx_biobb is a toolkit for free-energy calculation and biomolecular structure handling.
tags: [pmx_biobb, utility, gromacs, molecular-dynamics]
author: oxo-call-community
source_url: "https://github.com/deGrootLab/pmx/tree/develop"
---

## Concepts

- **Tool Overview**: pmx_biobb handles molecular simulation setup.
- **Core Function**: Free-energy calculation and analysis.
- **Algorithm**: Uses GROMACS for molecular dynamics.
- **Input Format**: Accepts biomolecular structure files.
- **Output**: Produces simulation results and analysis.
- **Use Case**: Protein-ligand binding, molecular modeling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large systems require memory.
- **Data Quality**: Results depend on input structure quality.
- **Computation Time**: Simulations may take significant time.
- **Validation**: Results should be validated for correctness.
- **Dependencies**: Requires GROMACS installation.

## Examples

### Display help
**Args:** `pmx --help`
**Explanation:** Shows available options and usage instructions.

### Setup free-energy calculation
**Args:** `pmx mutate -i protein.pdb -o mutated.pdb -m A100G`
**Explanation:** Sets up mutation for free-energy calculation.

### With parameters
**Args:** `pmx analyze -i results/ -p params.yaml -o analysis.txt`
**Explanation:** Uses parameter configuration for analysis.

### Verbose mode
**Args:** `pmx -v mutate -i protein.pdb -o mutated.pdb -m A100G`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pmx -t 4 analyze -i results/ -o analysis.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pmx analyze -i results/ -o analysis.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pmx analyze -i results/ -o analysis.txt --report report.html`
**Explanation:** Generates HTML report.