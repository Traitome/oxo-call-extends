---
name: ntstat
category: population-genomics
description: ntStat performs statistical analysis of k-mer frequency and depth for population genomics.
tags: [ntstat, population-genomics, k-mer, statistics]
author: oxo-call-community
source_url: "https://github.com/BirolLab/ntStat"
---

## Concepts

- **Tool Overview**: ntStat analyzes k-mer frequency and depth statistics from sequencing data.
- **Core Function**: Computes statistical metrics for k-mer distributions.
- **Algorithm**: Uses efficient counting and statistical methods.
- **Input Format**: Accepts FASTQ/FASTA reads or k-mer counts.
- **Output**: Produces statistical summaries and visualizations.
- **Use Case**: Population genetics, sequencing quality control, and coverage analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large k-mer sets require memory.
- **k-mer Size**: Requires appropriate k-mer size selection.
- **Computational Cost**: Analysis can be computationally intensive.
- **Data Quality**: Results depend on input data quality.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `ntstat --help`
**Explanation:** Shows available options and usage instructions.

### Compute statistics
**Args:** `ntstat -i reads.fastq -o statistics.txt`
**Explanation:** Computes k-mer statistics from reads.

### With k-mer size
**Args:** `ntstat -i reads.fastq -k 21 -o statistics.txt`
**Explanation:** Sets k-mer size to 21.

### Multiple files
**Args:** `ntstat -i reads_1.fastq -i2 reads_2.fastq -o statistics.txt`
**Explanation:** Processes multiple read files.

### Output plot
**Args:** `ntstat -i reads.fastq -o statistics.txt --plot`
**Explanation:** Generates visualization plots.

### Threads
**Args:** `ntstat -i reads.fastq -t 8 -o statistics.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `ntstat -i reads.fastq -v -o statistics.txt`
**Explanation:** Runs with verbose output.