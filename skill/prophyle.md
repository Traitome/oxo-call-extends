---
name: prophyle
category: metagenomics
description: prophyle is a phylogeny-based metagenomic classifier for taxonomic profiling.
tags: [prophyle, metagenomics, classification, taxonomy]
author: oxo-call-community
source_url: "https://github.com/karel-brinda/prophyle"
---

## Concepts

- **Tool Overview**: prophyle classifies metagenomic sequences.
- **Core Function**: Taxonomic classification.
- **Algorithm**: Uses phylogenetic methods.
- **Input Format**: Accepts sequencing reads.
- **Output**: Produces taxonomic profiles.
- **Use Case**: Metagenomics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large databases require memory.
- **Data Quality**: Results depend on input quality.
- **Classification Accuracy**: May have errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prophyle --help`
**Explanation:** Shows available options and usage instructions.

### Classify reads
**Args:** `prophyle classify -i reads.fastq -d database -o profile.txt`
**Explanation:** Classifies metagenomic reads.

### With parameters
**Args:** `prophyle classify -i reads.fastq -d database -p params.yaml -o profile.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prophyle -v classify -i reads.fastq -d database -o profile.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prophyle -t 4 classify -i reads.fastq -d database -o profile.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Build database
**Args:** `prophyle build -g genomes/ -o database/`
**Explanation:** Builds classification database.

### Generate report
**Args:** `prophyle classify -i reads.fastq -d database -o profile.txt --report report.html`
**Explanation:** Generates HTML report.