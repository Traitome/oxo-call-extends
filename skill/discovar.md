---
name: discovar
category: assembly
description: DISCOVAR - Genome assembly and variant discovery tool.
tags: [discovar, assembly, variant-calling, genome, broad-institute]
author: oxo-call-community
source_url: "https://www.broadinstitute.org/software/discovar/"
---

## Concepts

- **Tool Overview**: DISCOVAR is a genome assembly and variant discovery tool from Broad Institute.
- **Core Function**: Assembles genomes and discovers variants from high-coverage PCR-free data.
- **Input/Output**: Input: Paired-end reads (FASTQ). Output: Genome assemblies, variant calls (VCF), assembly statistics.
- **Algorithm**: Combines de novo assembly with variant calling in integrated pipeline.
- **Key Features**: Integrated assembly and variant calling, high accuracy, supports large genomes, phasing support, quality assessment.
- **Installation**: `conda install -c bioconda discovar`

## Pitfalls

- **Input Requirements**: Requires high-coverage PCR-free paired-end data.
- **Computational Resources**: Requires significant computational resources.
- **Memory Usage**: High memory requirements for large datasets.
- **Read Quality**: Poor quality reads affect both assembly and variant calling.
- **Time Consumption**: May take long for large genomes.

## Examples

### Assemble and call variants
**Args:** `discovar --reads R1.fq R2.fq --output assembly/`
**Explanation:** Assembles genome and discovers variants.

### Variant calling only
**Args:** `discovar --reads R1.fq R2.fq --output variants.vcf --call-only`
**Explanation:** Perform variant calling without full assembly.

### With reference genome
**Args:** `discovar --reads R1.fq R2.fq --reference ref.fa --output variants.vcf`
**Explanation:** Call variants against reference genome.

### Generate phased variants
**Args:** `discovar --reads R1.fq R2.fq --output assembly/ --phase`
**Explanation:** Generate phased variant calls.

### Quality filtering
**Args:** `discovar --reads R1.fq R2.fq --output assembly/ --min-quality 30`
**Explanation:** Apply minimum quality filter for variants.