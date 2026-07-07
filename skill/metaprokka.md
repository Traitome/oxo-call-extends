---
name: metaprokka
category: annotation
description: A fork of Prokka using Prodigal-GV for phage annotation and metagenome/metavirome tweaks
tags: [metaprokka, annotation, phage, metavirome]
author: oxo-call-community
source_url: "https://github.com/telatin/metaprokka"
---

## Concepts

- **Tool Overview**: MetaProkka v1.15.0 is a fork of Prokka optimized for phage annotation and metagenome/metavirome analysis.
- **Core Function**: Annotates prokaryotic genomes with a focus on phage and viral sequences.
- **Prodigal-GV Integration**: Uses Prodigal-GV for improved gene prediction in viral and metagenomic sequences.
- **Metagenome Optimization**: Includes specific tweaks for metagenome and metavirome annotation workflows.
- **Input/Output**: Accepts FASTA-formatted sequences; outputs annotated genomes with gene predictions.
- **Comprehensive Annotation**: Provides gene predictions, functional annotations, and feature tables.

## Pitfalls

- **Database Completeness**: Annotation quality depends on reference database completeness.
- **Sequence Quality**: Poor quality sequences may affect gene prediction accuracy.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Runtime**: Annotating complex metagenomes can be time-consuming.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **False Positives**: May predict false positive genes in fragmented sequences.

## Examples

### Annotate sequences
**Args:** `metaprokka --infile sequences.fasta --outdir annotation/`
**Explanation:** Annotates input sequences with gene predictions.

### Phage-specific annotation
**Args:** `metaprokka --infile phage.fasta --outdir annotation/ --phage`
**Explanation:** Optimizes annotation for phage sequences.

### Metavirome analysis
**Args:** `metaprokka --infile virome.fasta --outdir annotation/ --metavirome`
**Explanation:** Optimizes annotation for metavirome sequences.

### With custom database
**Args:** `metaprokka --infile sequences.fasta --outdir annotation/ --db custom_db/`
**Explanation:** Uses a custom annotation database.

### Batch processing
**Args:** `metaprokka --indir fasta/ --outdir annotations/`
**Explanation:** Processes multiple FASTA files in batch mode.