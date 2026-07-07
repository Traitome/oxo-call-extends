---
name: pybdei
category: utility
description: pybdei performs maximum likelihood estimation of Birth-Death Exposed-Infectious (BDEI) epidemiological model parameters from phylogenetic trees.
tags: [pybdei, utility, epidemiology, phylogenetic-trees]
author: oxo-call-community
source_url: "https://github.com/evolbioinfo/bdei"
---

## Concepts

- **Tool Overview**: pybdei estimates epidemiological parameters.
- **Core Function**: BDEI model parameter estimation.
- **Algorithm**: Uses maximum likelihood estimation.
- **Input Format**: Accepts phylogenetic trees.
- **Output**: Produces parameter estimates.
- **Use Case**: Epidemiological modeling.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex trees require memory.
- **Data Quality**: Results depend on tree quality.
- **Model Assumptions**: May affect accuracy.
- **Runtime**: Estimation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pybdei --help`
**Explanation:** Shows available options and usage instructions.

### Estimate parameters
**Args:** `pybdei estimate -i tree.nwk -o params.txt`
**Explanation:** Estimates BDEI model parameters from tree.

### With parameters
**Args:** `pybdei estimate -i tree.nwk -p params.yaml -o params.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pybdei -v estimate -i tree.nwk -o params.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pybdei -t 4 estimate -i tree.nwk -o params.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Bootstrap analysis
**Args:** `pybdei bootstrap -i tree.nwk -n 100 -o bootstrap.txt`
**Explanation:** Performs bootstrap analysis.

### Generate report
**Args:** `pybdei estimate -i tree.nwk -o params.txt --report report.html`
**Explanation:** Generates HTML report.