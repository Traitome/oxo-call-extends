---
name: pybascule
category: hpc
description: pybascule performs Bayesian NMF signatures deconvolution and Dirichlet Process clustering for cancer genomics.
tags: [pybascule, hpc, NMF, cancer-genomics]
author: oxo-call-community
source_url: "https://github.com/caravagnalab/pybascule"
---

## Concepts

- **Tool Overview**: pybascule analyzes mutational signatures.
- **Core Function**: Signature deconvolution.
- **Algorithm**: Uses Bayesian NMF.
- **Input Format**: Accepts mutation matrices.
- **Output**: Produces signature profiles.
- **Use Case**: Cancer mutational analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Parameter Tuning**: Requires careful configuration.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pybascule --help`
**Explanation:** Shows available options and usage instructions.

### Deconvolve signatures
**Args:** `pybascule deconvolve -i mutations.txt -o signatures.txt`
**Explanation:** Performs NMF signature deconvolution.

### With parameters
**Args:** `pybascule deconvolve -i mutations.txt -p params.yaml -o signatures.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pybascule -v deconvolve -i mutations.txt -o signatures.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pybascule -t 4 deconvolve -i mutations.txt -o signatures.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Cluster samples
**Args:** `pybascule cluster -i mutations.txt -o clusters.txt`
**Explanation:** Performs DP clustering on samples.

### Generate report
**Args:** `pybascule deconvolve -i mutations.txt -o signatures.txt --report report.html`
**Explanation:** Generates HTML report.