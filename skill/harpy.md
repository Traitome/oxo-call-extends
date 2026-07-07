---
name: harpy
category: bioinformatics
description: Harpy processes raw haplotagging data from raw sequences to phased haplotypes.
tags: [harpy, haplotagging, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://pdimens.github.io/harpy"
---

## Concepts

- **Haplotagging Processing**: Harpy processes haplotagging data.

- **Raw Sequences**: Handles raw sequencing data.

- **Phased Haplotypes**: Generates phased haplotypes.

- **Long Read Data**: Optimized for long read sequencing data.

- **Read Alignment**: Performs read alignment.

- **Variant Calling**: Supports variant calling.

## Pitfalls

- **Read Quality**: Low-quality reads may affect results.

- **Phasing Quality**: Results depend on phasing quality.

- **Computational Resources**: May require significant resources.

- **Memory Usage**: Large datasets may require significant memory.

- **Data Format**: Ensure correct input format.

## Examples

### Process haplotagging data
**Args:** `harpy process --reads reads.fastq --output haplotypes.fasta`
**Explanation:** Processes raw haplotagging data.

### With alignment
**Args:** `harpy align --reads reads.fastq --reference reference.fasta --output aligned.bam`
**Explanation:** Aligns reads to reference genome.

### Variant calling
**Args:** `harpy call --bam aligned.bam --output variants.vcf`
**Explanation:** Calls variants from aligned reads.

### Batch processing
**Args:** `for f in *.fastq; do harpy process --reads $f --output ${f%.fastq}_haplotypes.fasta; done`
**Explanation:** Processes multiple sequencing files.

### Quality filtering
**Args:** `harpy process --reads reads.fastq --min-quality 20 --output haplotypes.fasta`
**Explanation:** Filters reads by quality score.

### Generate report
**Args:** `harpy process --reads reads.fastq --report --output report.html`
**Explanation:** Generates processing report.

### Help command
**Args:** `harpy --help`
**Explanation:** Shows available options and usage information.