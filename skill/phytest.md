---
name: phytest
category: population-genomics
description: phytest provides quality control for phylogenetic pipelines using pytest.
tags: [phytest, population-genomics, quality-control, pytest]
author: oxo-call-community
source_url: "https://github.com/phytest-devs/phytest"
---

## Concepts

- **Tool Overview**: phytest performs quality control.
- **Core Function**: Quality control for phylogenetic pipelines.
- **Algorithm**: Uses pytest testing framework.
- **Input Format**: Accepts phylogenetic data files.
- **Output**: Produces quality control results.
- **Use Case**: Phylogenetics, quality assurance.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Test Coverage**: Requires proper test configuration.
- **Runtime**: Testing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phytest --help`
**Explanation:** Shows available options and usage instructions.

### Run quality control
**Args:** `phytest -i phylogenetic_data.txt -o qc_results.txt`
**Explanation:** Runs quality control on phylogenetic pipeline.

### With parameters
**Args:** `phytest -i phylogenetic_data.txt -p params.yaml -o qc_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phytest -v -i phylogenetic_data.txt -o qc_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phytest -t 4 -i phylogenetic_data.txt -o qc_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phytest -i phylogenetic_data.txt -o qc_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phytest -i phylogenetic_data.txt -o qc_results.txt --report report.html`
**Explanation:** Generates HTML report.