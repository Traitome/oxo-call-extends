---
name: polystest
category: utility
description: polystest provides statistical testing and visualization for omics data.
tags: [polystest, utility, statistics, visualization]
author: oxo-call-community
source_url: "https://bitbucket.org/veitveit/polystest/src/master/"
---

## Concepts

- **Tool Overview**: polystest analyzes quantitative omics data.
- **Core Function**: Statistical testing and visualization.
- **Algorithm**: Uses multiple statistical methods.
- **Input Format**: Accepts omics data files.
- **Output**: Produces statistical results and plots.
- **Use Case**: Omics data analysis, data visualization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Statistical Power**: May have false positives/negatives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `polystest --help`
**Explanation:** Shows available options and usage instructions.

### Analyze data
**Args:** `polystest -i omics_data.csv -o results/`
**Explanation:** Performs statistical testing on omics data.

### With parameters
**Args:** `polystest -i omics_data.csv -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `polystest -v -i omics_data.csv -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `polystest -t 4 -i omics_data.csv -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `polystest -i omics_data.csv -o results.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `polystest -i omics_data.csv -o results/ --report report.html`
**Explanation:** Generates HTML report.