---
name: reffinder
category: formatting
description: RefFinder is a fast lightweight tool for extracting nucleotides from FASTA files using streams.
tags: [reffinder, formatting, fasta, nucleotide-extraction]
author: oxo-call-community
source_url: "https://github.com/ANGSD/refFinder"
---

## Concepts

- **Tool Overview**: reffinder extracts nucleotides.
- **Core Function**: Nucleotide extraction.
- **Algorithm**: Uses streaming methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces extracted sequences.
- **Use Case**: Sequence processing.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large files require memory.
- **File Format**: Affects extraction.
- **Parameters**: Must be configured.
- **Runtime**: Extraction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `reffinder --help`
**Explanation:** Shows available options and usage instructions.

### Extract nucleotides
**Args:** `reffinder extract -i input.fasta -o output.fasta`
**Explanation:** Extracts nucleotides from FASTA.

### With parameters
**Args:** `reffinder extract -i input.fasta -p params.yaml -o output.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `reffinder -v extract -i input.fasta -o output.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `reffinder -t 4 extract -i input.fasta -o output.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### With regions
**Args:** `reffinder extract -i input.fasta -r regions.txt -o output.fasta`
**Explanation:** Extracts specific regions.

### Generate report
**Args:** `reffinder extract -i input.fasta -o output.fasta --report report.html`
**Explanation:** Generates HTML report.