---
name: poppunk
category: population-genomics
description: poppunk partitions populations using nucleotide k-mers.
tags: [poppunk, population-genomics, k-mers, clustering]
author: oxo-call-community
source_url: "https://poppunk.bacpop.org"
---

## Concepts

- **Tool Overview**: poppunk clusters bacterial genomes.
- **Core Function**: Population partitioning.
- **Algorithm**: Uses k-mer based methods.
- **Input Format**: Accepts FASTA/FASTQ files.
- **Output**: Produces population clusters.
- **Use Case**: Bacterial genomics, population structure.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequence quality.
- **Clustering Accuracy**: May have misclassification.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `poppunk --help`
**Explanation:** Shows available options and usage instructions.

### Run clustering
**Args:** `poppunk --input genomes/ --output clusters/`
**Explanation:** Partitions populations using k-mers.

### With parameters
**Args:** `poppunk --input genomes/ --output clusters/ --params params.yaml`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `poppunk -v --input genomes/ --output clusters/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `poppunk -t 4 --input genomes/ --output clusters/`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `poppunk --input genomes/ --output clusters.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `poppunk --input genomes/ --output clusters/ --report report.html`
**Explanation:** Generates HTML report.