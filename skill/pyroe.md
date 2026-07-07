---
name: pyroe
category: expression
description: Pyroe is a Python toolkit for scRNA-seq analysis workflows using alevin-fry.
tags: [pyroe, expression, scrna-seq, alevin-fry]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/pyroe"
---

## Concepts

- **Tool Overview**: pyroe aids scRNA-seq analysis.
- **Core Function**: Expression analysis.
- **Algorithm**: Uses alevin-fry.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces expression matrices.
- **Use Case**: Single-cell RNA-seq.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Normalization**: Must be applied.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pyroe --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `pyroe analyze -i reads.fastq -o results/`
**Explanation:** Performs scRNA-seq analysis.

### With parameters
**Args:** `pyroe analyze -i reads.fastq -p params.yaml -o results/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pyroe -v analyze -i reads.fastq -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pyroe -t 4 analyze -i reads.fastq -o results/`
**Explanation:** Uses 4 threads for parallel processing.

### Build index
**Args:** `pyroe index -i reference.fasta -o index/`
**Explanation:** Builds index for alignment.

### Generate report
**Args:** `pyroe analyze -i reads.fastq -o results/ --report report.html`
**Explanation:** Generates HTML report.