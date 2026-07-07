---
name: pipelign
category: metagenomics
description: pipelign automates multiple sequence alignment for viral sequences.
tags: [pipelign, metagenomics, alignment, viral]
author: oxo-call-community
source_url: "https://github.com/asmmhossain/pipelign/"
---

## Concepts

- **Tool Overview**: pipelign aligns viral sequences.
- **Core Function**: Automated multiple sequence alignment.
- **Algorithm**: Uses alignment algorithms.
- **Input Format**: Accepts FASTA/BAM/SAM files.
- **Output**: Produces alignment results.
- **Use Case**: Viral genomics, sequence analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on sequence quality.
- **Alignment Accuracy**: May have alignment errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pipelign --help`
**Explanation:** Shows available options and usage instructions.

### Align sequences
**Args:** `pipelign -i sequences.fasta -o alignment.fasta`
**Explanation:** Performs multiple sequence alignment.

### With parameters
**Args:** `pipelign -i sequences.fasta -p params.yaml -o alignment.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pipelign -v -i sequences.fasta -o alignment.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pipelign -t 4 -i sequences.fasta -o alignment.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pipelign -i sequences.fasta -o alignment.stockholm --stockholm`
**Explanation:** Outputs in Stockholm format.

### Generate report
**Args:** `pipelign -i sequences.fasta -o alignment.fasta --report report.html`
**Explanation:** Generates HTML report.