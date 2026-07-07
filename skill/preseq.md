---
name: preseq
category: programming
description: preseq predicts library complexity and genome coverage in sequencing.
tags: [preseq, programming, coverage, complexity]
author: oxo-call-community
source_url: "https://preseq.readthedocs.io/"
---

## Concepts

- **Tool Overview**: preseq analyzes sequencing library complexity.
- **Core Function**: Coverage prediction.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts BAM/FASTQ files.
- **Output**: Produces coverage estimates.
- **Use Case**: Sequencing experiment design.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Estimation Accuracy**: May have prediction errors.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `preseq --help`
**Explanation:** Shows available options and usage instructions.

### Predict complexity
**Args:** `preseq c_curve -i reads.fastq -o coverage.txt`
**Explanation:** Predicts library complexity and coverage.

### With parameters
**Args:** `preseq c_curve -i reads.fastq -p params.yaml -o coverage.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `preseq -v c_curve -i reads.fastq -o coverage.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `preseq -t 4 c_curve -i reads.fastq -o coverage.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `preseq c_curve -i reads.fastq -o coverage.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `preseq c_curve -i reads.fastq -o coverage.txt --report report.html`
**Explanation:** Generates HTML report.