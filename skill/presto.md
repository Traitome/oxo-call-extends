---
name: presto
category: formatting
description: presto is a toolkit for processing high-throughput lymphocyte receptor sequencing data.
tags: [presto, formatting, immunology, receptor-sequencing]
author: oxo-call-community
source_url: "https://presto.readthedocs.io"
---

## Concepts

- **Tool Overview**: presto processes immunosequencing data.
- **Core Function**: Receptor sequence processing.
- **Algorithm**: Uses bioinformatics methods.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces processed sequences.
- **Use Case**: Immunology, adaptive immunity research.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Receptor Identification**: May have false positives.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `presto --help`
**Explanation:** Shows available options and usage instructions.

### Process sequences
**Args:** `presto -i reads.fastq -o processed.txt`
**Explanation:** Processes lymphocyte receptor sequencing data.

### With parameters
**Args:** `presto -i reads.fastq -p params.yaml -o processed.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `presto -v -i reads.fastq -o processed.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `presto -t 4 -i reads.fastq -o processed.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `presto -i reads.fastq -o processed.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `presto -i reads.fastq -o processed.txt --report report.html`
**Explanation:** Generates HTML report.