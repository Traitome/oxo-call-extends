---
name: mkdesigner
category: variant-calling
description: Genome-wide design of markers for PCR-based genotyping from NGS data.
tags: [mkdesigner, variant-calling, genotyping]
author: oxo-call-community
source_url: "https://github.com/KChigira/mkdesigner"
---

## Concepts

- **Tool Overview**: mkdesigner v0.5.3 designs PCR-based genotyping markers from NGS data.
- **Core Function**: Designs genome-wide markers for PCR genotyping.
- **Marker Design**: Identifies optimal PCR primer pairs.
- **NGS Integration**: Uses next-generation sequencing data.
- **Input/Output**: Accepts variant data; outputs marker designs.
- **Genotyping Support**: Supports PCR-based genotyping workflows.

## Pitfalls

- **PCR Specific**: Designed for PCR-based markers.
- **Computational Resources**: Processing large genomes may require significant resources.
- **Memory Requirements**: Memory usage depends on genome size.
- **Parameter Tuning**: May require parameter adjustment for optimal design.
- **Data Quality**: Results depend on input variant data quality.
- **Primer Specificity**: Requires careful primer design validation.

## Examples

### Design genotyping markers
**Args:** `mkdesigner -v variants.vcf -g genome.fasta -o markers.txt`
**Explanation:** Designs PCR markers from variants.

### With custom parameters
**Args:** `mkdesigner -v variants.vcf -g genome.fasta -o markers.txt -p params.yaml`
**Explanation:** Uses custom design parameters.

### Primer validation
**Args:** `mkdesigner -v variants.vcf -g genome.fasta -o markers.txt -c`
**Explanation:** Validates primer specificity.

### Batch processing
**Args:** `mkdesigner -v vcf/ -g genome.fasta -o markers/`
**Explanation:** Processes multiple VCF files.

### Generate report
**Args:** `mkdesigner -v variants.vcf -g genome.fasta -o markers.txt -r report.html`
**Explanation:** Generates marker design report.