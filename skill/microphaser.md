---
name: microphaser
category: utility
description: Phasing small tumor DNA sequences for mutated neopeptide generation from NGS data.
tags: [microphaser, utility, cancer]
author: oxo-call-community
source_url: "https://github.com/koesterlab/microphaser"
---

## Concepts

- **Tool Overview**: MicroPhaser v0.8.0 phases tumor DNA sequences for mutated neopeptide generation.
- **Core Function**: Phases small tumor DNA sequences to generate mutated neopeptides.
- **Haplotype Phasing**: Determines haplotype phase of tumor mutations.
- **Neopeptide Generation**: Identifies potential neoantigens from tumor sequences.
- **Input/Output**: Accepts tumor sequencing data; outputs phased haplotypes.
- **Cancer Immunology**: Supports cancer immunotherapy research.

## Pitfalls

- **Cancer Specific**: Designed for tumor sequence analysis.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal phasing.
- **Data Quality**: Phasing accuracy depends on input data quality.
- **Variant Calling**: Requires prior variant calling.

## Examples

### Phase tumor sequences
**Args:** `microphaser -i tumor.bam -o phased.txt`
**Explanation:** Phases tumor DNA sequences for neopeptide generation.

### With variant file
**Args:** `microphaser -i tumor.bam -v variants.vcf -o phased.txt`
**Explanation:** Uses pre-called variants for phasing.

### Generate neopeptides
**Args:** `microphaser -i tumor.bam -o phased.txt -n neopeptides.txt`
**Explanation:** Generates mutated neopeptides from phased sequences.

### Batch processing
**Args:** `microphaser -i bam/ -o results/`
**Explanation:** Processes multiple tumor samples in batch mode.

### Detailed output
**Args:** `microphaser -i tumor.bam -o phased.txt -v`
**Explanation:** Generates detailed phasing report.