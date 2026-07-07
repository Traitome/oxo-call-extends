---
name: onyx
category: alignment
description: Onyx performs alignment-free biological sex inference from sequencing data.
tags: [onyx, alignment, sex-inference, genomics]
author: oxo-call-community
source_url: "https://github.com/omics-tools/onyx"
---

## Concepts

- **Tool Overview**: Onyx infers biological sex from sequencing data.
- **Core Function**: Determines sex using alignment-free methods.
- **Algorithm**: Uses k-mer analysis and statistical modeling.
- **Input Format**: Accepts FASTQ/FASTA sequencing reads.
- **Output**: Produces sex prediction with confidence score.
- **Use Case**: Sample QC, population genetics, and sex-specific analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Input Quality**: Results depend on sequencing depth.
- **Contamination**: May affect accuracy.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Validation**: Results should be validated with known samples.

## Examples

### Display help
**Args:** `onyx --help`
**Explanation:** Shows available options and usage instructions.

### Infer sex
**Args:** `onyx -i reads.fastq -o sex_prediction.txt`
**Explanation:** Predicts biological sex from reads.

### With reference
**Args:** `onyx -i reads.fastq -r reference.fasta -o prediction.txt`
**Explanation:** Uses reference genome for analysis.

### Output format
**Args:** `onyx -i reads.fastq -o prediction.json --json`
**Explanation:** Outputs in JSON format.

### Verbose mode
**Args:** `onyx -i reads.fastq -v -o prediction.txt`
**Explanation:** Runs with verbose output.

### Confidence threshold
**Args:** `onyx -i reads.fastq -t 0.9 -o prediction.txt`
**Explanation:** Sets confidence threshold to 0.9.

### Batch processing
**Args:** `onyx batch -d fastqs/ -o predictions/`
**Explanation:** Processes multiple FASTQ files.