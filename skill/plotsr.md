---
name: plotsr
category: utility
description: plotsr visualizes structural annotations between genomes.
tags: [plotsr, utility, visualization, structural-variation]
author: oxo-call-community
source_url: "https://github.com/schneebergerlab/plotsr"
---

## Concepts

- **Tool Overview**: plotsr visualizes genomic structures.
- **Core Function**: Structural annotation visualization.
- **Algorithm**: Uses comparative genomics methods.
- **Input Format**: Accepts GFF/GTF annotation files.
- **Output**: Produces visualization images.
- **Use Case**: Comparative genomics, genome alignment.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Data Quality**: Results depend on annotation quality.
- **Visualization Accuracy**: May have rendering issues.
- **Runtime**: Plotting may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plotsr --help`
**Explanation:** Shows available options and usage instructions.

### Plot structural annotations
**Args:** `plotsr -i annotations.gff -o visualization.png`
**Explanation:** Visualizes structural annotations between genomes.

### With parameters
**Args:** `plotsr -i annotations.gff -p params.yaml -o visualization.png`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plotsr -v -i annotations.gff -o visualization.png`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plotsr -t 4 -i annotations.gff -o visualization.png`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plotsr -i annotations.gff -o visualization.svg --svg`
**Explanation:** Outputs in SVG format.

### Generate report
**Args:** `plotsr -i annotations.gff -o visualization.png --report report.html`
**Explanation:** Generates HTML report.