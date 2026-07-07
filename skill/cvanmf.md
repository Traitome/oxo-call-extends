---
name: cvanmf
category: utility
description: Bi-cross validation of NMF and signature generation and analysis
tags: [cvanmf, utility, NMF, matrix-factorization, signature-analysis]
author: oxo-call-community
source_url: "https://github.com/apduncan/cvanmf"
---

## Concepts

- **Tool Overview**: cvanmf (v1.0.0+) is a tool for bi-cross validation of Non-negative Matrix Factorization (NMF) and signature generation analysis.
- **Core Function**: Performs bi-cross validation to assess NMF model quality and generates signatures from high-dimensional data.
- **Input/Output**: Input: Gene expression matrices, mutation profiles. Output: Signature matrices, validation metrics, clustering results.
- **Algorithm**: Implements bi-cross validation for robust NMF model selection and signature extraction.
- **Key Features**: Model validation, signature generation, visualization of factorization results.
- **Installation**: `conda install -c bioconda cvanmf`

## Pitfalls

- **Parameter Tuning**: Requires careful tuning of NMF parameters for optimal results.
- **Matrix Dimensions**: Large matrices may require significant computational resources.
- **Convergence**: NMF may require many iterations to converge.
- **Interpretation**: Signature interpretation requires domain knowledge.
- **Validation**: Cross-validation results should be interpreted with caution.

## Examples

### Run NMF with bi-cross validation
**Args:** `cvanmf -i expression_matrix.txt -k 5 -o signatures.txt`
**Explanation:** Perform NMF with 5 components and bi-cross validation.

### Generate signatures with specific rank
**Args:** `cvanmf -i data_matrix.txt -k 3,5,7 -o signatures/ --validate`
**Explanation:** Test multiple ranks and select best model based on validation.

### Visualize factorization results
**Args:** `cvanmf -i data.txt -k 5 -o results/ --plot`
**Explanation:** Generate visualization of NMF factorization and signatures.
