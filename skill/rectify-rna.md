---
name: rectify-rna
category: expression
description: RECTIFY is a unified RNA 3' end correction framework for transcriptomics analysis.
tags: [rectify-rna, expression, rna-correction, transcriptomics]
author: oxo-call-community
source_url: "https://github.com/k-roy/RECTIFY#readme"
---

## Concepts

- **Tool Overview**: rectify-rna corrects RNA.
- **Core Function**: RNA 3' end correction.
- **Algorithm**: Uses correction methods.
- **Input Format**: Accepts RNA-seq reads.
- **Output**: Produces corrected reads.
- **Use Case**: Transcriptomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Read Quality**: Affects correction.
- **Parameters**: Must be configured.
- **Runtime**: Correction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rectify-rna --help`
**Explanation:** Shows available options and usage instructions.

### Correct RNA ends
**Args:** `rectify-rna correct -i rna_reads.fastq -o corrected_reads.fastq`
**Explanation:** Corrects RNA 3' ends.

### With parameters
**Args:** `rectify-rna correct -i rna_reads.fastq -p params.yaml -o corrected_reads.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rectify-rna -v correct -i rna_reads.fastq -o corrected_reads.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rectify-rna -t 4 correct -i rna_reads.fastq -o corrected_reads.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `rectify-rna correct -i rna_reads.fastq -r reference.fasta -o corrected_reads.fastq`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `rectify-rna correct -i rna_reads.fastq -o corrected_reads.fastq --report report.html`
**Explanation:** Generates HTML report.