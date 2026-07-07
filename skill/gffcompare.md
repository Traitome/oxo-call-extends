---
name: gffcompare
category: annotation
description: gffcompare - Compare and evaluate the accuracy of gene annotations.
tags: [gffcompare, annotation, GFF, comparison, evaluation]
author: oxo-call-community
source_url: "https://github.com/gpertea/gffcompare/blob/v0.12.10/README.md"
---

## Concepts
- **Annotation Comparison**: Compares gene annotations.
- **Accuracy Evaluation**: Evaluates annotation accuracy.
- **Reference Mapping**: Maps annotations to reference.
- **Transcript Analysis**: Analyzes transcript predictions.
- **Quality Assessment**: Assesses annotation quality.

## Pitfalls
- **Reference Quality**: Requires high-quality reference.
- **Format Compatibility**: Requires correct GFF format.
- **Parameter Sensitivity**: Results sensitive to parameters.
- **Memory Usage**: Large datasets require memory.
- **Result Interpretation**: Requires careful interpretation.

## Examples
### Compare annotations
**Args:** `gffcompare -r reference.gff3 -o comparison query.gtf`
**Explanation:** Compares query annotation to reference.

### With options
**Args:** `gffcompare -r reference.gff3 -i -o comparison query.gtf`
**Explanation:** Ignores lower-case mismatches.

### Batch processing
**Args:** `gffcompare -r reference.gff3 -l queries.txt -o ./results/`
**Explanation:** Processes multiple query files.

### Generate stats
**Args:** `gffcompare -r reference.gff3 -o stats query.gtf`
**Explanation:** Generates comparison statistics.

### Generate report
**Args:** `gffcompare -r reference.gff3 -o comparison query.gtf -r -e errors.gtf`
**Explanation:** Generates detailed report.