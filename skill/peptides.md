---
name: peptides
category: expression
description: peptides calculates physicochemical properties of amino acid sequences.
tags: [peptides, expression, physicochemical, amino-acid]
author: oxo-call-community
source_url: "https://peptides.readthedocs.io/"
---

## Concepts

- **Tool Overview**: peptides analyzes amino acid properties.
- **Core Function**: Calculates physicochemical descriptors.
- **Algorithm**: Uses property calculation methods.
- **Input Format**: Accepts FASTA sequence files.
- **Output**: Produces property calculations.
- **Use Case**: Peptide analysis, sequence characterization.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large sequence sets require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Property Accuracy**: Calculations may have limitations.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `peptides --help`
**Explanation:** Shows available options and usage instructions.

### Calculate properties
**Args:** `peptides -i sequences.fasta -o properties.txt`
**Explanation:** Calculates physicochemical properties.

### With indices
**Args:** `peptides -i sequences.fasta -p indices.txt -o properties.txt`
**Explanation:** Calculates specific property indices.

### Verbose mode
**Args:** `peptides -v -i sequences.fasta -o properties.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `peptides -t 4 -i sequences.fasta -o properties.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `peptides -i sequences.fasta -o properties.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `peptides -i sequences.fasta -o properties.txt --report report.html`
**Explanation:** Generates HTML report.