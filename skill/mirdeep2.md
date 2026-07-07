---
name: mirdeep2
category: utility
description: A completely overhauled tool which discovers microRNA genes by analyzing sequenced RNAs
tags: [mirdeep2, utility, microrna]
author: oxo-call-community
source_url: "https://www.mdc-berlin.de/8551903/en/research/research_teams/systems_biology_of_gene_regulatory_elements/projects/miRDeep"
---

## Concepts

- **Tool Overview**: miRDeep2 v2.0.1.3 discovers miRNA genes from sequencing data.
- **Core Function**: Identifies novel and known miRNAs from small RNA-seq data.
- **miRNA Discovery**: Detects miRNA precursors and mature sequences.
- **Expression Analysis**: Quantifies miRNA expression levels.
- **Input/Output**: Accepts small RNA-seq data; outputs miRNA predictions.
- **Small RNA Research**: Supports miRNA transcriptome analysis workflows.

## Pitfalls

- **Small RNA Specific**: Designed for small RNA sequencing data.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for optimal discovery.
- **Data Quality**: Results depend on input data quality.
- **Reference Genome**: Requires appropriate reference sequences.

## Examples

### Discover miRNAs
**Args:** `miRDeep2.pl reads.fastq reference.fasta mature.fa precursor.fa -o results/`
**Explanation:** Runs complete miRNA discovery pipeline.

### With known miRNAs
**Args:** `miRDeep2.pl reads.fastq reference.fasta known_mature.fa known_precursor.fa -o results/`
**Explanation:** Uses known miRNAs for validation.

### Quantify expression
**Args:** `miRDeep2.pl reads.fastq reference.fasta mature.fa precursor.fa -o results/ -q`
**Explanation:** Quantifies miRNA expression levels.

### Batch processing
**Args:** `miRDeep2.pl fastq/ reference.fasta mature.fa precursor.fa -o results/`
**Explanation:** Processes multiple FASTQ files.

### Generate report
**Args:** `miRDeep2.pl reads.fastq reference.fasta mature.fa precursor.fa -o results/ -r`
**Explanation:** Generates HTML analysis report.