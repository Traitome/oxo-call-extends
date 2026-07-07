---
name: qualimap
category: alignment
description: QualiMap provides quality control of alignment sequencing data and its derivatives like feature counts.
tags: [qualimap, alignment, quality-control, bioinformatics]
author: oxo-call-community
source_url: "http://qualimap.bioinfo.cipf.es/"
---

## Concepts

- **Tool Overview**: qualimap analyzes alignment quality.
- **Core Function**: Alignment QC.
- **Algorithm**: Uses statistical methods.
- **Input Format**: Accepts BAM files.
- **Output**: Produces QC metrics.
- **Use Case**: Alignment analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Annotation**: Must be correct.
- **Parameters**: Must be configured.
- **Runtime**: Analysis may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `qualimap --help`
**Explanation:** Shows available options and usage instructions.

### Run QC
**Args:** `qualimap run -i aligned.bam -o qc_report/`
**Explanation:** Runs alignment quality control.

### With parameters
**Args:** `qualimap run -i aligned.bam -p params.yaml -o qc_report/`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `qualimap -v run -i aligned.bam -o qc_report/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `qualimap -t 4 run -i aligned.bam -o qc_report/`
**Explanation:** Uses 4 threads for parallel processing.

### RNA-Seq mode
**Args:** `qualimap rnaseq -i aligned.bam -o qc_report/`
**Explanation:** Runs RNA-Seq specific QC.

### Generate report
**Args:** `qualimap run -i aligned.bam -o qc_report/ --report report.html`
**Explanation:** Generates HTML report.