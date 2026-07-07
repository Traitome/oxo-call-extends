---
name: probabilistic2020
category: variant-calling
description: probabilistic2020 simulates somatic mutations and identifies significant oncogenes and tumor suppressor genes.
tags: [probabilistic2020, variant-calling, cancer-genomics, statistics]
author: oxo-call-community
source_url: "https://github.com/KarchinLab/probabilistic2020"
---

## Concepts

- **Tool Overview**: probabilistic2020 analyzes cancer mutations.
- **Core Function**: Somatic mutation analysis.
- **Algorithm**: Uses randomization-based testing.
- **Input Format**: Accepts mutation data files.
- **Output**: Produces oncogene predictions.
- **Use Case**: Cancer genomics, driver gene identification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Statistical Power**: May have false positives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `probabilistic2020 --help`
**Explanation:** Shows available options and usage instructions.

### Analyze mutations
**Args:** `probabilistic2020 -i mutations.vcf -o results.txt`
**Explanation:** Identifies significant oncogenes and tumor suppressor genes.

### With parameters
**Args:** `probabilistic2020 -i mutations.vcf -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `probabilistic2020 -v -i mutations.vcf -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `probabilistic2020 -t 4 -i mutations.vcf -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `probabilistic2020 -i mutations.vcf -o results.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `probabilistic2020 -i mutations.vcf -o results.txt --report report.html`
**Explanation:** Generates HTML report.