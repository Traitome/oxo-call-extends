---
name: viguno
category: bioinformatics
description: Viguno - Variant quality control.
tags: [viguno, variant-quality, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/viguno/"
---

## Concepts

- **Tool Overview**: Viguno - Variant quality assessment tool.
- **Core Function**: Evaluates variant calling quality.
- **Input**: VCF file.
- **Output**: Quality metrics.
- **Installation**: Install via pip or conda
- **Use Case**: Variant QC, bioinformatics.

## Pitfalls

- **Memory**: May require significant memory for large VCF files.
- **Reference**: Requires reference genome.

## Examples

### Assess quality
**Args:** `viguno -i input.vcf -o qc_report.txt`
**Explanation:** Assess variant quality.

### With options
**Args:** `viguno -i input.vcf -o qc_report.txt -r ref.fasta`
**Explanation:** Use reference for assessment.
