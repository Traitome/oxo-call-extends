---
name: pymummer
category: utility
description: pyMUMmer is a Python wrapper for the MUMmer sequence alignment tool suite.
tags: [pymummer, utility, alignment, mummer]
author: oxo-call-community
source_url: "https://github.com/sanger-pathogens/pymummer"
---

## Concepts

- **Tool Overview**: pymummer wraps MUMmer tools.
- **Core Function**: Sequence alignment.
- **Algorithm**: Uses MUMmer algorithms.
- **Input Format**: Accepts FASTA sequences.
- **Output**: Produces alignments.
- **Use Case**: Genome comparison.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **MUMmer Install**: Must have MUMmer installed.
- **Sequence Length**: May affect performance.
- **Runtime**: Alignment may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pymummer --help`
**Explanation:** Shows available options and usage instructions.

### Run nucmer
**Args:** `pymummer nucmer -r ref.fasta -q query.fasta -o output.delta`
**Explanation:** Runs nucmer alignment.

### With parameters
**Args:** `pymummer nucmer -r ref.fasta -p params.yaml -o output.delta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pymummer -v nucmer -r ref.fasta -q query.fasta -o output.delta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pymummer -t 4 nucmer -r ref.fasta -q query.fasta -o output.delta`
**Explanation:** Uses 4 threads for parallel processing.

### Show alignment
**Args:** `pymummer show-aligns -d output.delta -r ref.fasta -q query.fasta -o alignment.txt`
**Explanation:** Shows alignment details.

### Generate report
**Args:** `pymummer nucmer -r ref.fasta -q query.fasta -o output.delta --report report.html`
**Explanation:** Generates HTML report.