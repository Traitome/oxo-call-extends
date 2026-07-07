---
name: probcons
category: alignment
description: probcons performs probabilistic consistency-based multiple sequence alignment.
tags: [probcons, alignment, msa, probabilistic]
author: oxo-call-community
source_url: "http://probcons.stanford.edu/"
---

## Concepts

- **Tool Overview**: probcons aligns protein sequences.
- **Core Function**: Probabilistic multiple alignment.
- **Algorithm**: Uses consistency-based methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces alignments.
- **Use Case**: Protein sequence analysis, phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Alignment Accuracy**: May have errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `probcons --help`
**Explanation:** Shows available options and usage instructions.

### Align sequences
**Args:** `probcons input.fasta output.fasta`
**Explanation:** Performs probabilistic multiple sequence alignment.

### With parameters
**Args:** `probcons -p params.txt input.fasta output.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `probcons -v input.fasta output.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `probcons -t 4 input.fasta output.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `probcons input.fasta output.clustal --clustal`
**Explanation:** Outputs in Clustal format.

### Generate report
**Args:** `probcons input.fasta output.fasta --report report.html`
**Explanation:** Generates HTML report.