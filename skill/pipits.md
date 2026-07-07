---
name: pipits
category: hpc
description: pipits analyzes fungal ITS sequences from Illumina sequencing.
tags: [pipits, hpc, fungal, its]
author: oxo-call-community
source_url: "https://github.com/hsgweon/pipits"
---

## Concepts

- **Tool Overview**: pipits analyzes fungal ITS sequences.
- **Core Function**: Fungal ITS sequence analysis.
- **Algorithm**: Uses sequence analysis methods.
- **Input Format**: Accepts FASTA/BED files.
- **Output**: Produces ITS analysis results.
- **Use Case**: Fungal metagenomics, ITS analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **ITS Specificity**: May have specificity issues.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pipits --help`
**Explanation:** Shows available options and usage instructions.

### Analyze ITS sequences
**Args:** `pipits -i its_sequences.fasta -o its_results.txt`
**Explanation:** Analyzes fungal ITS sequences.

### With parameters
**Args:** `pipits -i its_sequences.fasta -p params.yaml -o its_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pipits -v -i its_sequences.fasta -o its_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pipits -t 4 -i its_sequences.fasta -o its_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pipits -i its_sequences.fasta -o its_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `pipits -i its_sequences.fasta -o its_results.txt --report report.html`
**Explanation:** Generates HTML report.