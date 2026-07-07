---
name: phantasm
category: population-genomics
description: phantasm performs phylogenomic analyses for microbial taxonomy.
tags: [phantasm, population-genomics, phylogenomics, taxonomy]
author: oxo-call-community
source_url: "https://github.com/dr-joe-wirth/phantasm"
---

## Concepts

- **Tool Overview**: phantasm analyzes microbial phylogenomics.
- **Core Function**: Performs taxonomy and systematics analysis.
- **Algorithm**: Uses phylogenomic analysis methods.
- **Input Format**: Accepts microbial genome files.
- **Output**: Produces phylogenomic analysis results.
- **Use Case**: Microbial taxonomy, phylogenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genome sets require memory.
- **Genome Quality**: Results depend on genome quality.
- **Taxonomy Database**: Requires proper taxonomy database.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phantasm --help`
**Explanation:** Shows available options and usage instructions.

### Analyze genomes
**Args:** `phantasm -i genomes/ -o phylogenomics_results/`
**Explanation:** Performs phylogenomic analysis.

### With parameters
**Args:** `phantasm -i genomes/ -p params.yaml -o phylogenomics_results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phantasm -v -i genomes/ -o phylogenomics_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phantasm -t 8 -i genomes/ -o phylogenomics_results/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `phantasm -i genomes/ -o phylogenomics_results/ --format json`
**Explanation:** Outputs in JSON format.

### Generate report
**Args:** `phantasm -i genomes/ -o phylogenomics_results/ --report report.html`
**Explanation:** Generates HTML report.