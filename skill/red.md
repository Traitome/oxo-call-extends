---
name: red
category: programming
description: RED (RepeatsDetector) is an intelligent, rapid, accurate tool for detecting repeats de novo on the genomic scale.
tags: [red, programming, repeat-detection, genomic-repeats]
author: oxo-call-community
source_url: "http://toolsmith.ens.utulsa.edu"
---

## Concepts

- **Tool Overview**: red detects repeats.
- **Core Function**: Repeat detection.
- **Algorithm**: Uses detection methods.
- **Input Format**: Accepts genomic sequences.
- **Output**: Produces repeat annotations.
- **Use Case**: Genomic analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large genomes require memory.
- **Sequence Quality**: Affects detection.
- **Parameters**: Must be configured.
- **Runtime**: Detection may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `red --help`
**Explanation:** Shows available options and usage instructions.

### Detect repeats
**Args:** `red detect -i genome.fasta -o repeats.txt`
**Explanation:** Detects genomic repeats.

### With parameters
**Args:** `red detect -i genome.fasta -p params.yaml -o repeats.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `red -v detect -i genome.fasta -o repeats.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `red -t 4 detect -i genome.fasta -o repeats.txt`
**Explanation:** Uses 4 threads for parallel processing.

### With minimum length
**Args:** `red detect -i genome.fasta -l 100 -o repeats.txt`
**Explanation:** Uses minimum length threshold.

### Generate report
**Args:** `red detect -i genome.fasta -o repeats.txt --report report.html`
**Explanation:** Generates HTML report.