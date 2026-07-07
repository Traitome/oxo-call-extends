---
name: qimba
category: programming
description: Qimba is a toolkit for metabarcoding analyses and bioinformatics workflows.
tags: [qimba, programming, metabarcoding, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/quadram-institute-bioscience/qimba"
---

## Concepts

- **Tool Overview**: qimba analyzes metabarcoding data.
- **Core Function**: Sequence analysis.
- **Algorithm**: Uses various methods.
- **Input Format**: Accepts sequence files.
- **Output**: Produces analysis results.
- **Use Case**: Metabarcoding.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Parameters**: Must be configured.
- **Dependencies**: Must be installed.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qimba --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `qimba analyze -i sequences.fasta -o results/`
**Explanation:** Runs metabarcoding analysis.

### With parameters
**Args:** `qimba analyze -i sequences.fasta -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qimba -v analyze -i sequences.fasta -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qimba -t 4 analyze -i sequences.fasta -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Quality filtering
**Args:** `qimba filter -i sequences.fasta -q 20 -o filtered.fasta`
**Explanation:** Filters by quality.

### Generate report
**Args:** `qimba analyze -i sequences.fasta -o results/ --report report.html`
**Explanation:** Generates HTML report.