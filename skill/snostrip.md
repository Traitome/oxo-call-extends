---
name: snostrip
category: annotation
description: snoStrip - Automatic snoRNA annotation pipeline
tags: [snostrip, annotation, snorna, non-coding-rna, pipeline]
author: oxo-call-community
source_url: "http://snostrip.bioinf.uni-leipzig.de/help.py"
---

## Concepts

- **Tool Overview**: snostrip (v2.0.2) - An automated pipeline for snoRNA annotation
- **Core Function**: Identifies and annotates snoRNA genes in genomic sequences
- **Input/Output**: Accepts genomic sequences; outputs annotated snoRNA predictions
- **Algorithm**: Integrates multiple detection methods for comprehensive annotation
- **Installation**: `conda install -c bioconda snostrip`
- **Key Features**: Automated annotation, multiple snoRNA types, comprehensive pipeline

## Pitfalls

- **Input Requirements**: Requires properly formatted genomic sequences
- **Database Dependencies**: Requires snoRNA databases for homology search
- **Computation Time**: Large genomes can be slow to process
- **Annotation Quality**: Quality depends on input sequence quality
- **False Positives**: May produce false positives in repetitive regions
- **Configuration**: Requires proper configuration for optimal results

## Examples

### Display help
**Args:** `snostrip --help`
**Explanation:** Shows available options and usage information.

### Basic annotation
**Args:** `snostrip -i genome.fasta -o annotations.gff`
**Explanation:** Run snoRNA annotation pipeline.

### With custom database
**Args:** `snostrip -i genome.fasta -d snorna_db.fasta -o annotations.gff`
**Explanation:** Use custom snoRNA database.

### Full pipeline
**Args:** `snostrip -i genome.fasta -o annotations.gff --full`
**Explanation:** Run complete annotation pipeline.

### C/D box only
**Args:** `snostrip -i genome.fasta -o annotations.gff --cd-box`
**Explanation:** Search only for C/D box snoRNAs.

### H/ACA box only
**Args:** `snostrip -i genome.fasta -o annotations.gff --haca-box`
**Explanation:** Search only for H/ACA box snoRNAs.

### With validation
**Args:** `snostrip -i genome.fasta -o annotations.gff --validate`
**Explanation:** Validate predictions against known snoRNAs.

### Generate report
**Args:** `snostrip -i genome.fasta -o annotations.gff --report report.html`
**Explanation:** Generate annotation report.