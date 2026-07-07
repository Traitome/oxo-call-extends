---
name: mi-pimento
category: variant-calling
description: A PrIMEr infereNce TOolkit to facilitate large-scale calling of metabarcoding amplicon sequence variants.
tags: [mi-pimento, variant-calling, metabarcoding]
author: oxo-call-community
source_url: "https://github.com/EBI-Metagenomics/PIMENTO"
---

## Concepts

- **Tool Overview**: MI-PIMENTO v1.0.3 performs primer inference for metabarcoding analysis.
- **Core Function**: Calls amplicon sequence variants from metabarcoding data.
- **Primer Inference**: Identifies primer sequences in sequencing reads.
- **Amplicon Analysis**: Processes amplicon sequencing data.
- **Input/Output**: Accepts sequencing reads; outputs variant calls.
- **Metabarcoding**: Supports environmental DNA analysis workflows.

## Pitfalls

- **Amplicon Specific**: Designed for amplicon sequencing data.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Calling accuracy depends on input data quality.
- **Primer Design**: Results depend on primer specificity.

## Examples

### Call amplicon variants
**Args:** `mi-pimento -i reads.fastq -o variants.vcf`
**Explanation:** Calls amplicon sequence variants from reads.

### With primer sequences
**Args:** `mi-pimento -i reads.fastq -p primers.fasta -o variants.vcf`
**Explanation:** Uses custom primer sequences.

### Detailed output
**Args:** `mi-pimento -i reads.fastq -o variants.vcf -v`
**Explanation:** Generates detailed variant report.

### Batch processing
**Args:** `mi-pimento -i fastq/ -o variants/`
**Explanation:** Processes multiple FASTQ files.

### Filter by quality
**Args:** `mi-pimento -i reads.fastq -o variants.vcf -q 30`
**Explanation:** Uses quality threshold of 30.