---
name: pilea
category: metagenomics
description: pilea profiles bacterial growth dynamics from metagenomes.
tags: [pilea, metagenomics, bacterial, growth]
author: oxo-call-community
source_url: "https://github.com/xinehc/pilea"
---

## Concepts

- **Tool Overview**: pilea profiles bacterial growth.
- **Core Function**: Metagenome-based growth profiling.
- **Algorithm**: Uses sketching methods.
- **Input Format**: Accepts metagenome files.
- **Output**: Produces growth dynamics results.
- **Use Case**: Metagenomics, growth analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on data quality.
- **Growth Profiling**: May have profiling errors.
- **Runtime**: Profiling may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pilea --help`
**Explanation:** Shows available options and usage instructions.

### Profile growth dynamics
**Args:** `pilea -i metagenome_data.txt -o growth_results.txt`
**Explanation:** Profiles bacterial growth dynamics.

### With parameters
**Args:** `pilea -i metagenome_data.txt -p params.yaml -o growth_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pilea -v -i metagenome_data.txt -o growth_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pilea -t 4 -i metagenome_data.txt -o growth_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pilea -i metagenome_data.txt -o growth_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pilea -i metagenome_data.txt -o growth_results.txt --report report.html`
**Explanation:** Generates HTML report.