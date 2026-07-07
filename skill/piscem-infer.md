---
name: piscem-infer
category: expression
description: piscem-infer performs target quantification from bulk-sequencing data.
tags: [piscem-infer, expression, quantification, bulk-seq]
author: oxo-call-community
source_url: "https://github.com/COMBINE-lab/piscem-infer"
---

## Concepts

- **Tool Overview**: piscem-infer quantifies sequencing targets.
- **Core Function**: Target quantification.
- **Algorithm**: Uses quantification methods.
- **Input Format**: Accepts bulk-sequencing data files.
- **Output**: Produces quantification results.
- **Use Case**: Gene expression, transcript quantification.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequencing Quality**: Results depend on data quality.
- **Quantification Accuracy**: May have quantification errors.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `piscem-infer --help`
**Explanation:** Shows available options and usage instructions.

### Quantify targets
**Args:** `piscem-infer -i bulk_seq_data.fastq -o quantification_results.txt`
**Explanation:** Performs target quantification.

### With parameters
**Args:** `piscem-infer -i bulk_seq_data.fastq -p params.yaml -o quantification_results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `piscem-infer -v -i bulk_seq_data.fastq -o quantification_results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `piscem-infer -t 4 -i bulk_seq_data.fastq -o quantification_results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `piscem-infer -i bulk_seq_data.fastq -o quantification_results.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `piscem-infer -i bulk_seq_data.fastq -o quantification_results.txt --report report.html`
**Explanation:** Generates HTML report.