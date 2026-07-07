---
name: pylocuszoom
category: alignment
description: pylocuszoom creates publication-ready GWAS visualization including regional association plots and gene tracks.
tags: [pylocuszoom, alignment, gwas, visualization]
author: oxo-call-community
source_url: "https://github.com/michael-denyer/pylocuszoom"
---

## Concepts

- **Tool Overview**: pylocuszoom visualizes GWAS data.
- **Core Function**: Regional association plotting.
- **Algorithm**: Uses matplotlib/bokeh.
- **Input Format**: Accepts GWAS summary stats.
- **Output**: Produces publication-ready plots.
- **Use Case**: GWAS visualization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex plots require memory.
- **Data Quality**: Results depend on input quality.
- **Plot Customization**: May require tuning.
- **Runtime**: Plotting may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pylocuszoom --help`
**Explanation:** Shows available options and usage instructions.

### Create regional plot
**Args:** `pylocuszoom plot -i gwas_results.txt -c chr1:1-1000000 -o region_plot.png`
**Explanation:** Generates regional association plot.

### With parameters
**Args:** `pylocuszoom plot -i gwas_results.txt -p params.yaml -o region_plot.png`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pylocuszoom -v plot -i gwas_results.txt -o region_plot.png`
**Explanation:** Runs with verbose output.

### Forest plot
**Args:** `pylocuszoom forest -i odds_ratios.txt -o forest_plot.png`
**Explanation:** Creates forest plot.

### PheWAS plot
**Args:** `pylocuszoom phewas -i phewas_results.txt -o phewas_plot.png`
**Explanation:** Generates PheWAS plot.

### Generate report
**Args:** `pylocuszoom plot -i gwas_results.txt -o region_plot.png --report report.html`
**Explanation:** Generates HTML report.