---
name: mirtop
category: expression
description: Small RNA-seq annotation.
tags: [mirtop, expression, microrna]
author: oxo-call-community
source_url: "https://github.com/mirtop/mirtop"
---

## Concepts

- **Tool Overview**: mirtop v0.4.30 annotates small RNA sequencing data.
- **Core Function**: Annotates and quantifies small RNA species.
- **Small RNA Annotation**: Identifies and classifies small RNA types.
- **miRNA Analysis**: Focuses on microRNA annotation and quantification.
- **Input/Output**: Accepts aligned reads; outputs annotated results.
- **Standardized Format**: Produces standardized annotation output.

## Pitfalls

- **Small RNA Specific**: Designed for small RNA sequencing data.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal annotation.
- **Data Quality**: Results depend on input alignment quality.
- **Annotation Standards**: Requires consistent input format.

## Examples

### Annotate small RNA-seq
**Args:** `mirtop gff -i alignments.bam -o annotations.gff`
**Explanation:** Annotates small RNA alignments.

### With reference
**Args:** `mirtop gff -i alignments.bam -r reference.gff -o annotations.gff`
**Explanation:** Uses reference annotation.

### Quantify expression
**Args:** `mirtop quantify -i alignments.bam -o counts.tsv`
**Explanation:** Quantifies small RNA expression.

### Batch processing
**Args:** `mirtop gff -i bam/ -o gff/`
**Explanation:** Processes multiple BAM files.

### Generate report
**Args:** `mirtop report -i annotations.gff -o report.html`
**Explanation:** Generates annotation report.