---
name: quaqc
category: qc
description: QuaQC provides quick quality control for ATAC-seq data analysis.
tags: [quaqc, qc, atac-seq, quality-control]
author: oxo-call-community
source_url: "https://github.com/bjmt/quaqc/blob/v1.5/README.md"
---

## Concepts

- **Tool Overview**: quaqc performs ATAC-seq QC.
- **Core Function**: Quality control.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts BAM/FASTQ files.
- **Output**: Produces QC metrics.
- **Use Case**: ATAC-seq analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Input Type**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: QC may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quaqc --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `quaqc run -i aligned.bam -o qc_report/`
**Explanation:** Runs ATAC-seq quality control.

### With parameters
**Args:** `quaqc run -i aligned.bam -p params.yaml -o qc_report/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quaqc -v run -i aligned.bam -o qc_report/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quaqc -t 4 run -i aligned.bam -o qc_report/`
**Explanation:** Uses 4 threads for parallel processing.

### From FASTQ
**Args:** `quaqc run -i reads.fastq -g genome.fasta -o qc_report/`
**Explanation:** Runs QC from raw reads.

### Generate report
**Args:** `quaqc run -i aligned.bam -o qc_report/ --report report.html`
**Explanation:** Generates HTML report.