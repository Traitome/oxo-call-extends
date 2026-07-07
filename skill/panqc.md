---
name: panqc
category: qc
description: PanQC provides quality control and redundancy correction for pangenome analyses.
tags: [panqc, qc, pangenome, quality-control]
author: oxo-call-community
source_url: "https://github.com/maxgmarin/panqc"
---

## Concepts

- **Tool Overview**: PanQC evaluates and corrects nucleotide redundancy in pangenomes.
- **Core Function**: Performs quality control for pangenome analysis.
- **Algorithm**: Uses k-mer based similarity metrics for redundancy detection.
- **Input Format**: Accepts pangenome annotations and sequence files.
- **Output**: Produces corrected pangenome data and statistics.
- **Use Case**: Pangenome quality control, redundancy correction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Parameter Sensitivity**: Results depend on parameters.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `panqc --help`
**Explanation:** Shows available options and usage instructions.

### Run quality control
**Args:** `panqc -i pangenome/ -o qc_results/`
**Explanation:** Performs pangenome quality control.

### Redundancy correction
**Args:** `panqc nrc -i pangenome/ -o corrected/`
**Explanation:** Runs Nucleotide Redundancy Correction.

### Verbose mode
**Args:** `panqc -v -i pangenome/ -o qc_results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `panqc -t 16 -i pangenome/ -o qc_results/`
**Explanation:** Uses 16 threads for parallel processing.

### Output format
**Args:** `panqc -i pangenome/ -o qc_results.json --json`
**Explanation:** Outputs in JSON format.

### Statistics
**Args:** `panqc stats -i pangenome/ -o stats.txt`
**Explanation:** Generates quality control statistics.