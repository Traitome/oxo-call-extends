---
name: phantasm-xenogi
category: utility
description: phantasm-xenogi provides xenoGI functionality for PHANTASM.
tags: [phantasm-xenogi, utility, xenogi, phylogenomics]
author: oxo-call-community
source_url: "https://github.com/dr-joe-wirth/xenoGI"
---

## Concepts

- **Tool Overview**: phantasm-xenogi provides phylogenomic utilities.
- **Core Function**: Extends PHANTASM with xenoGI tools.
- **Algorithm**: Uses genomic island detection.
- **Input Format**: Accepts genome data files.
- **Output**: Produces phylogenomic analysis results.
- **Use Case**: Phylogenomics, genomic island analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Genome Quality**: Results depend on genome quality.
- **Island Detection**: May miss complex islands.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phantasm-xenogi --help`
**Explanation:** Shows available options and usage instructions.

### Analyze genomes
**Args:** `phantasm-xenogi -i genomes/ -o xenogi_results/`
**Explanation:** Performs xenoGI analysis.

### With parameters
**Args:** `phantasm-xenogi -i genomes/ -p params.yaml -o xenogi_results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phantasm-xenogi -v -i genomes/ -o xenogi_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phantasm-xenogi -t 4 -i genomes/ -o xenogi_results/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phantasm-xenogi -i genomes/ -o xenogi_results/ --format json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `phantasm-xenogi -i genomes/ -o xenogi_results/ --report report.html`
**Explanation:** Generates HTML report.