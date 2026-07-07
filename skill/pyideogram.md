---
name: pyideogram
category: utility
description: pyideogram plots ideograms (chromosome diagrams) using matplotlib.
tags: [pyideogram, utility, visualization, chromosomes]
author: oxo-call-community
source_url: "https://github.com/Balthasar-eu/pyideogram"
---

## Concepts

- **Tool Overview**: pyideogram plots chromosome ideograms.
- **Core Function**: Karyotype visualization.
- **Algorithm**: Uses matplotlib plotting.
- **Input Format**: Accepts chromosome data.
- **Output**: Produces ideogram plots.
- **Use Case**: Genome visualization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Complex plots require memory.
- **Data Quality**: Results depend on input quality.
- **Chromosome Names**: Must match expected format.
- **Runtime**: Plotting may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyideogram --help`
**Explanation:** Shows available options and usage instructions.

### Plot ideogram
**Args:** `pyideogram plot -i cytobands.txt -o ideogram.png`
**Explanation:** Generates chromosome ideogram.

### With parameters
**Args:** `pyideogram plot -i cytobands.txt -p params.yaml -o ideogram.png`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyideogram -v plot -i cytobands.txt -o ideogram.png`
**Explanation:** Runs with verbose output.

### Specific chromosomes
**Args:** `pyideogram plot -i cytobands.txt -c chr1,chr2,chr3 -o ideogram.png`
**Explanation:** Plots specific chromosomes.

### High resolution
**Args:** `pyideogram plot -i cytobands.txt -r 300 -o ideogram.png`
**Explanation:** Generates high-res image.

### Generate report
**Args:** `pyideogram plot -i cytobands.txt -o ideogram.png --report report.html`
**Explanation:** Generates HTML report.