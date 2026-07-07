---
name: pixelator
category: programming
description: pixelator processes MPX assay sequencing data.
tags: [pixelator, programming, mpx, sequencing]
author: oxo-call-community
source_url: "https://github.com/PixelgenTechnologies/pixelator"
---

## Concepts

- **Tool Overview**: pixelator analyzes MPX assay data.
- **Core Function**: Molecular Pixelation data processing.
- **Algorithm**: Uses MPX-specific analysis methods.
- **Input Format**: Accepts MPX sequencing files.
- **Output**: Produces MPX analysis results.
- **Use Case**: Spatial transcriptomics, MPX assays.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequencing Quality**: Results depend on data quality.
- **MPX Specificity**: Requires MPX-specific data.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pixelator --help`
**Explanation:** Shows available options and usage instructions.

### Process MPX data
**Args:** `pixelator process -i mpx_data.fastq -o results/`
**Explanation:** Processes Molecular Pixelation assay data.

### With parameters
**Args:** `pixelator process -i mpx_data.fastq -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pixelator process -v -i mpx_data.fastq -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pixelator process -t 4 -i mpx_data.fastq -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pixelator process -i mpx_data.fastq -o results.json --json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `pixelator process -i mpx_data.fastq -o results/ --report report.html`
**Explanation:** Generates HTML report.