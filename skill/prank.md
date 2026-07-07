---
name: prank
category: alignment
description: prank performs probabilistic multiple sequence alignment.
tags: [prank, alignment, msa, probabilistic]
author: oxo-call-community
source_url: "https://ariloytynoja.github.io/prank-msa"
---

## Concepts

- **Tool Overview**: prank aligns sequences.
- **Core Function**: Probabilistic multiple alignment.
- **Algorithm**: Uses evolutionary model methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces alignments.
- **Use Case**: Phylogenetics, sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Alignment Accuracy**: May have errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `prank --help`
**Explanation:** Shows available options and usage instructions.

### Align sequences
**Args:** `prank -d sequences.fasta -o alignment.fasta`
**Explanation:** Performs multiple sequence alignment.

### With parameters
**Args:** `prank -d sequences.fasta -p params.yaml -o alignment.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `prank -v -d sequences.fasta -o alignment.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `prank -threads 4 -d sequences.fasta -o alignment.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `prank -d sequences.fasta -o alignment.phylip -f phylip`
**Explanation:** Outputs in PHYLIP format.

### Generate report
**Args:** `prank -d sequences.fasta -o alignment.fasta --report report.html`
**Explanation:** Generates HTML report.