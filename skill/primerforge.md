---
name: primerforge
category: utility
description: primerforge identifies primers that can distinguish genomes.
tags: [primerforge, utility, primers, genome-detection]
author: oxo-call-community
source_url: "https://github.com/dr-joe-wirth/primerForge"
---

## Concepts

- **Tool Overview**: primerforge designs diagnostic primers.
- **Core Function**: Species-specific primer design.
- **Algorithm**: Uses comparative genomics methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces primer sequences.
- **Use Case**: Species identification, diagnostics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Primer Specificity**: May have cross-reactivity.
- **Runtime**: Design may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `primerForge --help`
**Explanation:** Shows available options and usage instructions.

### Design primers
**Args:** `primerForge -i genomes.fasta -o primers.csv`
**Explanation:** Designs species-specific primers.

### With parameters
**Args:** `primerForge -i genomes.fasta -p params.yaml -o primers.csv`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `primerForge -v -i genomes.fasta -o primers.csv`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `primerForge -t 4 -i genomes.fasta -o primers.csv`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `primerForge -i genomes.fasta -o primers.bed --bed`
**Explanation:** Outputs in BED format.

### Generate report
**Args:** `primerForge -i genomes.fasta -o primers.csv --report report.html`
**Explanation:** Generates HTML report.