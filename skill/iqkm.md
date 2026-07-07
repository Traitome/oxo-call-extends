---
name: iqkm
category: functional-annotation
description: iqKM - Identification and quantification of KEGG Modules in metagenomes/genomes.
tags: [iqkm, KEGG, metagenomics, functional-annotation, pathway-analysis]
author: oxo-call-community
source_url: "https://github.com/lijingdi/iqKM"
---

## Concepts

- **Tool Overview**: iqKM (v1.0) - A pipeline for assigning and quantifying KEGG Orthology (KO) and KEGG Modules (KMs) in metagenomic and genomic data.
- **Core Function**: Uses Kofam HMM profiles for KO assignment and module completeness assessment.
- **KO Assignment**: Identifies KEGG Orthology groups using HMMER-based Kofam scanning.
- **Module Quantification**: Determines KEGG module completeness and abundance.
- **Dual Mode**: Supports both genome and metagenome analysis modes.
- **Integration**: Integrates with HMMER, Prodigal, BWA, and Samtools for comprehensive analysis.

## Pitfalls

- **Database Requirements**: Requires downloading and configuring Kofam HMM database (~50GB).
- **Computational Resources**: Large datasets may require significant computational resources.
- **Gene Prediction**: Depends on accurate gene prediction from input sequences.
- **Module Completeness**: Module prediction depends on KO coverage thresholds.
- **Reference Bias**: Results may be biased towards well-annotated organisms in KEGG.
- **Memory Usage**: Memory-intensive operations may require careful resource allocation.

## Examples

### Basic genome analysis
**Args:** `iqKM -i genome.fna -o results/ --help_dir /path/to/help_dir`
**Explanation:** Performs KO and KEGG module analysis on a single genome.

### Metagenome analysis
**Args:** `iqKM -i metagenome.fna -o results/ --help_dir /path/to/help_dir --meta`
**Explanation:** Analyzes a metagenome for KEGG module content.

### With quantification
**Args:** `iqKM -i genome.fna -o results/ --help_dir /path/to/help_dir --fq reads.fastq.gz --quantify`
**Explanation:** Performs KO assignment and quantification using raw reads.

### Paired-end reads quantification
**Args:** `iqKM -i metagenome.fna -o results/ --help_dir /path/to/help_dir --fq R1.fastq.gz --rq R2.fastq.gz --meta --quantify`
**Explanation:** Analyzes metagenome with paired-end reads for module quantification.

### Custom Kofam database
**Args:** `iqKM -i genome.fna -o results/ --kofam_db /custom/kofam/db/`
**Explanation:** Uses a custom Kofam HMM database for KO assignment.

### Detailed output
**Args:** `iqKM -i genome.fna -o results/ --help_dir /path/to/help_dir --verbose`
**Explanation:** Generates detailed output including intermediate files and logs.