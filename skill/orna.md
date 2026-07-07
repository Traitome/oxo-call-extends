---
name: orna
category: utility
description: ORNA performs in silico read normalization for sequencing data.
tags: [orna, utility, read-normalization, sequencing]
author: oxo-call-community
source_url: "https://github.com/SchulzLab/ORNA"
---

## Concepts

- **Tool Overview**: ORNA normalizes sequencing read coverage.
- **Core Function**: Reduces read depth to uniform coverage.
- **Algorithm**: Uses k-mer based normalization.
- **Input Format**: Accepts FASTQ sequence files.
- **Output**: Produces normalized FASTQ files.
- **Use Case**: Sequencing data preprocessing, normalization, and coverage control.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **k-mer Size**: Requires appropriate k-mer size selection.
- **Coverage Bias**: May introduce coverage bias.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `orna --help`
**Explanation:** Shows available options and usage instructions.

### Normalize reads
**Args:** `orna -i reads.fastq -o normalized.fastq -c 100`
**Explanation:** Normalizes reads to 100x coverage.

### With k-mer size
**Args:** `orna -i reads.fastq -o normalized.fastq -k 21 -c 100`
**Explanation:** Uses k-mer size of 21.

### Output format
**Args:** `orna -i reads.fastq -o normalized.fasta --fasta`
**Explanation:** Outputs in FASTA format.

### Verbose mode
**Args:** `orna -i reads.fastq -v -o normalized.fastq`
**Explanation:** Runs with verbose output.

### Batch processing
**Args:** `orna batch -d fastqs/ -o normalized/ -c 100`
**Explanation:** Processes multiple FASTQ files.

### Quality filtering
**Args:** `orna -i reads.fastq -q 20 -o normalized.fastq -c 100`
**Explanation:** Filters reads by quality before normalization.