---
name: quast
category: qc
description: QUAST is a Quality Assessment Tool for Genome Assemblies, providing comprehensive metrics for evaluating assembly quality.
tags: [quast, qc, genome-assembly, quality-assessment]
author: oxo-call-community
source_url: "https://quast.sourceforge.net/docs/manual.html"
---

## Concepts

- **Tool Overview**: quast assesses assembly quality.
- **Core Function**: Assembly QC.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts FASTA files.
- **Output**: Produces QC metrics.
- **Use Case**: Assembly validation.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large assemblies require memory.
- **Reference Genome**: Must be provided for full analysis.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `quast --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `quast -i assembly.fasta -o qc_report/`
**Explanation:** Assesses assembly quality.

### With parameters
**Args:** `quast -i assembly.fasta -p params.yaml -o qc_report/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `quast -v -i assembly.fasta -o qc_report/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `quast -t 4 -i assembly.fasta -o qc_report/`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `quast -i assembly.fasta -r reference.fasta -o qc_report/`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `quast -i assembly.fasta -o qc_report/ --html-report`
**Explanation:** Generates HTML report.