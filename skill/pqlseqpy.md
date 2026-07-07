---
name: pqlseqpy
category: programming
description: pqlseqpy is a fast implementation of PQLseq in Python.
tags: [pqlseqpy, programming, qtl, sequencing]
author: oxo-call-community
source_url: "https://github.com/mokar2001/PQLseqPy"
---

## Concepts

- **Tool Overview**: pqlseqpy analyzes QTL-seq data.
- **Core Function**: QTL mapping.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts sequencing data.
- **Output**: Produces QTL results.
- **Use Case**: Quantitative trait analysis, genetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on sequencing quality.
- **Statistical Power**: May have false positives.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `pqlseqpy --help`
**Explanation:** Shows available options and usage instructions.

### Run QTL analysis
**Args:** `pqlseqpy -i reads.fastq -r reference.fasta -o qtl.txt`
**Explanation:** Performs QTL-seq analysis.

### With parameters
**Args:** `pqlseqpy -i reads.fastq -r reference.fasta -p params.yaml -o qtl.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `pqlseqpy -v -i reads.fastq -r reference.fasta -o qtl.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `pqlseqpy -t 4 -i reads.fastq -r reference.fasta -o qtl.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `pqlseqpy -i reads.fastq -r reference.fasta -o qtl.csv --csv`
**Explanation:** Outputs in CSV format.

### Generate report
**Args:** `pqlseqpy -i reads.fastq -r reference.fasta -o qtl.txt --report report.html`
**Explanation:** Generates HTML report.