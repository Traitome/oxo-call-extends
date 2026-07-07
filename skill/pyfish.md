---
name: pyfish
category: population-genomics
description: pyfish creates Fish (Muller) plots for visualizing evolutionary population dynamics.
tags: [pyfish, population-genomics, visualization, muller-plot]
author: oxo-call-community
source_url: "https://bitbucket.org/schwarzlab/pyfish"
---

## Concepts

- **Tool Overview**: pyfish generates Muller plots.
- **Core Function**: Population dynamics visualization.
- **Algorithm**: Uses area plotting.
- **Input Format**: Accepts population data.
- **Output**: Produces plots.
- **Use Case**: Evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Visualization Limits**: Complex data may be unclear.
- **Runtime**: Plotting may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyfish --help`
**Explanation:** Shows available options and usage instructions.

### Create Muller plot
**Args:** `pyfish plot -i populations.txt -o muller.png`
**Explanation:** Generates Muller plot from population data.

### With parameters
**Args:** `pyfish plot -i populations.txt -p params.yaml -o muller.png`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyfish -v plot -i populations.txt -o muller.png`
**Explanation:** Runs with verbose output.

### Custom colors
**Args:** `pyfish plot -i populations.txt -c colors.txt -o muller.png`
**Explanation:** Uses custom color scheme.

### High resolution
**Args:** `pyfish plot -i populations.txt -r 300 -o muller.png`
**Explanation:** Generates high-res plot.

### Generate report
**Args:** `pyfish plot -i populations.txt -o muller.png --report report.html`
**Explanation:** Generates HTML report.