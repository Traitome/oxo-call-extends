---
name: pyrovelocity
category: utility
description: PyroVelocity performs probabilistic RNA velocity analysis for cell fate uncertainty estimation.
tags: [pyrovelocity, utility, rna-velocity, single-cell]
author: oxo-call-community
source_url: "https://pyrovelocity.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: pyrovelocity estimates cell fate.
- **Core Function**: RNA velocity analysis.
- **Algorithm**: Uses probabilistic modeling.
- **Input Format**: Accepts scRNA-seq data.
- **Output**: Produces velocity estimates.
- **Use Case**: Single-cell analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Computational Cost**: May be expensive.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyrovelocity --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `pyrovelocity run -i counts.h5ad -o velocity_results/`
**Explanation:** Performs RNA velocity analysis.

### With parameters
**Args:** `pyrovelocity run -i counts.h5ad -p params.yaml -o velocity_results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyrovelocity -v run -i counts.h5ad -o velocity_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyrovelocity -t 4 run -i counts.h5ad -o velocity_results/`
**Explanation:** Uses 4 threads for parallel processing.

### Plot results
**Args:** `pyrovelocity plot -i velocity_results/ -o plot.pdf`
**Explanation:** Generates visualization.

### Generate report
**Args:** `pyrovelocity run -i counts.h5ad -o velocity_results/ --report report.html`
**Explanation:** Generates HTML report.