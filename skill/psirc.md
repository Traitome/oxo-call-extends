---
name: psirc
category: expression
description: psirc reconstructs and quantifies full-length linear and circular transcript isoforms from RNA-seq data.
tags: [psirc, expression, transcriptomics, circular-RNA]
author: oxo-call-community
source_url: "https://github.com/nictru/psirc/blob/master/README.md"
---

## Concepts

- **Tool Overview**: psirc reconstructs transcript isoforms.
- **Core Function**: Isoform reconstruction.
- **Algorithm**: Uses splice graph methods.
- **Input Format**: Accepts RNA-seq reads.
- **Output**: Produces isoform sequences.
- **Use Case**: Transcriptomics analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Data Quality**: Results depend on input quality.
- **Circular Detection**: May have false positives.
- **Runtime**: Processing may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `psirc --help`
**Explanation:** Shows available options and usage instructions.

### Reconstruct isoforms
**Args:** `psirc -i reads.fastq -o isoforms.fasta`
**Explanation:** Reconstructs linear and circular isoforms.

### With parameters
**Args:** `psirc -i reads.fastq -p params.yaml -o isoforms.fasta`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `psirc -v -i reads.fastq -o isoforms.fasta`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `psirc -t 4 -i reads.fastq -o isoforms.fasta`
**Explanation:** Uses 4 threads for parallel processing.

### Quantification
**Args:** `psirc -i reads.fastq -q -o quant_results.txt`
**Explanation:** Performs isoform quantification.

### Generate report
**Args:** `psirc -i reads.fastq -o isoforms.fasta --report report.html`
**Explanation:** Generates HTML report.