---
name: mity
category: variant-calling
description: Mity is a bioinformatic analysis pipeline designed to call mitochondrial SNV and INDEL variants from Whole Genome Sequencing (WGS) data.
tags: [mity, variant-calling, mitochondrial]
author: oxo-call-community
source_url: "https://github.com/KCCG/mity"
---

## Concepts

- **Tool Overview**: Mity v2.0.1 calls mitochondrial SNV and INDEL variants from WGS data.
- **Core Function**: Identifies low-heteroplasmy mitochondrial variants.
- **Low Heteroplasmy**: Detects variants with <1% heteroplasmy.
- **Variant Calling**: Calls SNVs and INDELs in mtDNA.
- **Input/Output**: Accepts WGS data; outputs variant calls.
- **Clinical Reporting**: Generates annotated reports for clinicians.

## Pitfalls

- **Mitochondrial Specific**: Designed for mtDNA variant calling.
- **Computational Resources**: Processing may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal calling.
- **Data Quality**: Results depend on input data quality.
- **High Depth**: Requires sufficient read depth for low-heteroplasmy detection.

## Examples

### Call mitochondrial variants
**Args:** `mity call --bam alignments.bam --output variants.vcf`
**Explanation:** Calls mtDNA variants from aligned reads.

### With filtering
**Args:** `mity call --bam alignments.bam --output variants.vcf --min-af 0.01`
**Explanation:** Uses minimum allele frequency of 1%.

### Merge with nuclear variants
**Args:** `mity merge --mity variants.vcf --nuclear nuclear.vcf --output merged.vcf`
**Explanation:** Merges mtDNA and nuclear variants.

### Generate report
**Args:** `mity report --vcf variants.vcf --output report.html`
**Explanation:** Generates annotated clinical report.

### Batch processing
**Args:** `mity call --bam bam/ --output variants/`
**Explanation:** Processes multiple BAM files.