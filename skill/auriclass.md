---
name: auriclass
category: variant-calling
description: AuriClass - Tool for rapid clade prediction of Candida auris genomes
tags: [candida-auris, fungal-pathogen, clade-prediction, outbreak-tracking]
author: oxo-call-community
source_url: "https://github.com/RIVM-bioinformatics/auriclass"
---

## Concepts

- **Tool Overview**: AuriClass quickly predicts the clade (geographic lineage) of Candida auris genomes, a multidrug-resistant fungal pathogen of major public health concern.

- **Clade Classification**: Identifies which of the known C. auris clades (I-V) a genome belongs to, providing epidemiological context for infection control.

- **Rapid Analysis**: Designed for quick turnaround, enabling real-time surveillance and outbreak investigation.

- **Genome Input**: Accepts assembled genomes or raw reads for clade prediction.

## Pitfalls

- **Database Dependency**: Requires up-to-date clade reference database. Outdated databases may miss new clades or misclassify samples.

- **Hybrid Genomes**: Recombinant or hybrid genomes may have ambiguous clade assignments.

- **Quality Requirements**: Low-quality genomes or incomplete assemblies may give incorrect predictions.

- **Novel Clades**: Emerging clades not in database will be assigned to closest existing clade, potentially misrepresenting true lineage.

## Examples

### Basic clade prediction from assembly
**Args:** `auriclass predict --assembly genome.fasta --output results.txt`
**Explanation:** Predicts C. auris clade from assembled genome, outputs prediction with confidence score.

### Prediction from raw reads
**Args:** `auriclass predict --reads reads_R1.fastq.gz reads_R2.fastq.gz --output results.txt`
**Explanation:** Predicts clade directly from raw sequencing reads without requiring prior assembly.

### Batch processing
**Args:** `auriclass batch --input-dir genomes/ --output batch_results.tsv`
**Explanation:** Processes all genome files in directory, outputs results in tab-separated format for multiple samples.

### Update reference database
**Args:** `auriclass update-db --db-dir /path/to/database`
**Explanation:** Updates clade reference database to latest version for improved prediction accuracy.

### Detailed output
**Args:** `auriclass predict --assembly genome.fasta --output results.txt --verbose`
**Explanation:** Provides detailed output including SNP distances to reference clades and confidence metrics.
