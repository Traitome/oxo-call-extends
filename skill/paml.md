---
name: paml
category: utility
description: PAML is a package for phylogenetic analyses using maximum likelihood.
tags: [paml, utility, phylogenetics, maximum-likelihood]
author: oxo-call-community
source_url: "https://evomics.org/resources/software/molecular-evolution-software/paml"
---

## Concepts

- **Tool Overview**: PAML performs phylogenetic analyses using maximum likelihood.
- **Core Function**: Estimates evolutionary parameters and phylogenies.
- **Algorithm**: Uses maximum likelihood estimation.
- **Input Format**: Accepts sequence alignments and tree files.
- **Output**: Produces parameter estimates and likelihood values.
- **Use Case**: Molecular evolution, phylogenetics, and selection analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Model Selection**: Requires careful model selection.
- **Convergence**: May require multiple runs for convergence.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `codeml --help`
**Explanation:** Shows available options and usage instructions.

### Run codeml
**Args:** `codeml control.ctl`
**Explanation:** Executes codeml with control file.

### With alignment
**Args:** `baseml -infile alignment.fasta -outfile results.txt`
**Explanation:** Runs baseml on alignment.

### Parameter file
**Args:** `codeml my_analysis.ctl`
**Explanation:** Uses custom control file.

### Verbose mode
**Args:** `codeml -v control.ctl`
**Explanation:** Runs with verbose output.

### Threads
**Args:** `codeml -t 8 control.ctl`
**Explanation:** Uses 8 threads for parallel processing.

### Model testing
**Args:** `codeml model_test.ctl`
**Explanation:** Tests different evolutionary models.