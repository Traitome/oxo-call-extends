---
name: pyscenic
category: expression
description: pySCENIC is a Python implementation of the SCENIC pipeline for transcription factor inference from single-cell transcriptomics data.
tags: [pyscenic, expression, transcription-factor, single-cell]
author: oxo-call-community
source_url: "https://scenic.aertslab.org"
---

## Concepts

- **Tool Overview**: pyscenic infers transcription factors.
- **Core Function**: TF inference.
- **Algorithm**: Uses gene regulatory networks.
- **Input Format**: Accepts expression matrices.
- **Output**: Produces TF targets.
- **Use Case**: Single-cell analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Reference Databases**: Must be available.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyscenic --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `pyscenic run -i expression.h5ad -o results/`
**Explanation:** Performs SCENIC analysis.

### With parameters
**Args:** `pyscenic run -i expression.h5ad -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyscenic -v run -i expression.h5ad -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyscenic -t 4 run -i expression.h5ad -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Build GRN
**Args:** `pyscenic grn -i expression.h5ad -o grn.csv`
**Explanation:** Builds gene regulatory network.

### Generate report
**Args:** `pyscenic run -i expression.h5ad -o results/ --report report.html`
**Explanation:** Generates HTML report.