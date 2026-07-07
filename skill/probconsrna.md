---
name: probconsrna
category: utility
description: probconsrna is an experimental version of PROBCONS for nucleotide sequences.
tags: [probconsrna, utility, rna-alignment, msa]
author: oxo-call-community
source_url: "http://probcons.stanford.edu/"
---

## Concepts

- **Tool Overview**: probconsrna aligns RNA sequences.
- **Core Function**: Nucleotide sequence alignment.
- **Algorithm**: Uses probabilistic methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces alignments.
- **Use Case**: RNA sequence analysis, structural biology.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Alignment Accuracy**: May have errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `probconsRNA --help`
**Explanation:** Shows available options and usage instructions.

### Align RNA sequences
**Args:** `probconsRNA input.fasta output.fasta`
**Explanation:** Performs multiple RNA sequence alignment.

### With parameters
**Args:** `probconsRNA -p params.txt input.fasta output.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `probconsRNA -v input.fasta output.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `probconsRNA -t 4 input.fasta output.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `probconsRNA input.fasta output.clustal --clustal`
**Explanation:** Outputs in Clustal format.

### Generate report
**Args:** `probconsRNA input.fasta output.fasta --report report.html`
**Explanation:** Generates HTML report.