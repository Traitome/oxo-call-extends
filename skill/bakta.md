---
name: bakta
category: annotation
description: Bakta - Rapid and standardized annotation of bacterial genomes, MAGs, and plasmids
tags: [bacterial-annotation, genome-annotation, prokka-alternative, standardized]
author: oxo-call-community
source_url: "https://github.com/oschwengers/bakta"
---

## Concepts

- **Tool Overview**: Bakta provides rapid and standardized annotation of bacterial genomes, metagenome-assembled genomes (MAGs), and plasmids with comprehensive feature prediction.

- **Standardized Annotations**: Uses standardized databases and nomenclature for consistent, comparable annotations across studies.

- **Comprehensive Features**: Predicts protein-coding genes, rRNAs, tRNAs, tmRNAs, CRISPR arrays, ncRNAs, regulatory RNAs, and genomic islands.

- **Database Integration**: Integrates multiple databases including UniProt, RefSeq, and specialized databases for specific feature types.

- **Speed**: Optimized for fast annotation through efficient algorithms and pre-computed databases.

## Pitfalls

- **Database Size**: Requires large database download (~30GB). Ensure sufficient disk space.

- **Memory Requirements**: Large genomes require substantial memory for annotation.

- **Novel Organisms**: Novel or highly divergent organisms may have lower annotation quality due to database limitations.

- **Update Frequency**: Database updates may change annotations. Document database version used.

## Examples

### Basic genome annotation
**Args:** `bakta --genome genome.fasta --output annotation/`
**Explanation:** Annotates bacterial genome with comprehensive feature prediction.

### Use local database
**Args:** `bakta --genome genome.fasta --db /path/to/bakta_db --output annotation/`
**Explanation:** Uses local Bakta database instead of downloading each time.

### Annotate plasmid
**Args:** `bakta --genome plasmid.fasta --compliant --output plasmid_annotation/`
**Explanation:** Annotates plasmid sequence with GenBank compliance for submission.

### Annotate MAG
**Args:** `bakta --genome mag.fasta --min-contig-length 500 --output mag_annotation/`
**Explanation:** Annotates metagenome-assembled genome, filtering short contigs.

### Specify output formats
**Args:** `bakta --genome genome.fasta --output annotation/ --output-format gff3,gbk,faa`
**Explanation:** Outputs annotation in multiple formats: GFF3, GenBank, and protein FASTA.

### Parallel processing
**Args:** `bakta --genome genome.fasta --threads 16 --output annotation/`
**Explanation:** Uses 16 threads for faster annotation of large genomes.

### Add custom database
**Args:** `bakta --genome genome.fasta --db /path/to/bakta_db --custom /path/to/custom_db --output annotation/`
**Explanation:** Supplements standard database with custom protein sequences for improved annotation.
