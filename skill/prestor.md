---
name: prestor
category: qc
description: prestor generates quality control plots from pRESTO output.
tags: [prestor, qc, quality-control, visualization]
author: oxo-call-community
source_url: "https://bitbucket.org/javh/prototype-prestor"
---

## Concepts

- **Tool Overview**: prestor visualizes pRESTO output.
- **Core Function**: QC plot generation.
- **Algorithm**: Uses plotting methods.
- **Input Format**: Accepts pRESTO output.
- **Output**: Produces QC plots.
- **Use Case**: Quality control, data visualization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Plot Generation**: May have rendering issues.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prestor --help`
**Explanation:** Shows available options and usage instructions.

### Generate QC plots
**Args:** `prestor -i presto_output.txt -o qc_plots`
**Explanation:** Generates quality control plots.

### With parameters
**Args:** `prestor -i presto_output.txt -p params.yaml -o qc_plots`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prestor -v -i presto_output.txt -o qc_plots`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prestor -t 4 -i presto_output.txt -o qc_plots`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prestor -i presto_output.txt -o qc_plots --pdf`
**Explanation:** Outputs in PDF format.

### Generate report
**Args:** `prestor -i presto_output.txt -o qc_plots --report report.html`
**Explanation:** Generates HTML report.