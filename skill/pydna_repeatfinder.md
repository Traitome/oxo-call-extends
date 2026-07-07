---
name: pydna_repeatfinder
category: utility
description: pydna_repeatfinder searches for direct and inverted repeats in DNA sequences.
tags: [pydna_repeatfinder, utility, repeats, dna-analysis]
author: oxo-call-community
source_url: "https://github.com/linsalrob/repeatfinder"
---

## Concepts

- **Tool Overview**: pydna_repeatfinder finds repeats.
- **Core Function**: Repeat sequence detection.
- **Algorithm**: Uses pattern matching.
- **Input Format**: Accepts FASTA sequences.
- **Output**: Produces repeat locations.
- **Use Case**: Genome analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequences require memory.
- **Data Quality**: Results depend on input quality.
- **Repeat Complexity**: May affect detection.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pydna_repeatfinder --help`
**Explanation:** Shows available options and usage instructions.

### Find repeats
**Args:** `pydna_repeatfinder -i genome.fasta -o repeats.txt`
**Explanation:** Finds repeats in DNA sequence.

### With parameters
**Args:** `pydna_repeatfinder -i genome.fasta -p params.yaml -o repeats.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pydna_repeatfinder -v -i genome.fasta -o repeats.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pydna_repeatfinder -t 4 -i genome.fasta -o repeats.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Inverted repeats
**Args:** `pydna_repeatfinder --inverted -i genome.fasta -o inverted.txt`
**Explanation:** Finds inverted repeats.

### Generate report
**Args:** `pydna_repeatfinder -i genome.fasta -o repeats.txt --report report.html`
**Explanation:** Generates HTML report.