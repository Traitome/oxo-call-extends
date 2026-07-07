---
name: mydbfinder
category: annotation
description: MyDbFinder - Identifies genes from custom databases in bacterial isolates
tags: [mydbfinder, annotation, gene-detection, database, bacteria, bacterial, isolate]
author: oxo-call-community
source_url: "https://bitbucket.org/genomicepidemiology/mydbfinder"
---

## Concepts

- **Tool Overview**: MyDbFinder v1.0.5 is a tool for identifying genes from user-provided databases in bacterial genome sequences. It screens bacterial genome assemblies against custom gene databases to detect specific genes of interest.
- **Core Function**: Takes a bacterial genome assembly (FASTA) and a custom gene database (sequences to search for), then identifies which genes from the database are present in the target genome with sequence similarity above specified thresholds.
- **Algorithm**: Uses sequence similarity search (BLAST-like) to find gene matches between the query database and the target genome. Reports matching genes with identity, coverage, and e-value statistics.
- **Input Format**: Requires a genome assembly in FASTA format and a gene database file containing the target gene sequences. Database can be in FASTA or similar format with one gene per entry.
- **Output**: Produces a table of identified genes with match statistics (identity, coverage, e-value), genomic locations, and sequence alignment details. Includes summary of database coverage in the target genome.
- **Use Case**: Bacterial pathogen characterization, virulence gene detection, antibiotic resistance gene screening, and custom gene screening in bacterial isolates.

## Pitfalls

- **Database Quality**: The quality and comprehensiveness of the input database directly affects detection results. Ensure the gene database is well-curated and representative.
- **Identity Threshold**: Setting appropriate sequence identity thresholds is critical. Too low may give false positives; too high may miss divergent gene variants.
- **Fragment Detection**: Short fragments of genes may be detected but not reported if below coverage thresholds. Adjust parameters for detecting partial gene matches.
- **Genome Assembly Quality**: Poor quality assemblies with many contigs may give fragmented or missed gene predictions. Use high-quality assemblies when possible.
- **Self-BLAST**: If database genes come from the same species as the query genome, expect high-identity matches that may represent endogenous genes rather than acquired genes.
- **Database Redundancy**: Redundant entries in the database may produce duplicate hits. Consider deduplicating the database before searching.

## Examples

### Basic gene detection
**Args:** `-i genome.fasta -d gene_database.fasta -o results.tsv`
**Explanation:** Standard MyDbFinder workflow. Screens genome against custom database and outputs matches.

### Specify sequence identity threshold
**Args:** `-i bacterial_isolate.fa -d virulence_genes.fa -o results.tsv -id 90`
**Explanation:** Sets minimum 90% sequence identity for gene detection, filtering out lower similarity matches.

### Adjust minimum coverage
**Args:** `-i genome.fasta -d custom_db.fasta -o results.tsv -cov 80`
**Explanation:** Requires at least 80% coverage of the database gene for a positive hit.

### Paired-end read input
**Args:** `-i genome.fasta -d ar_genes.fasta -o results.tsv -pe`
**Explanation:** Uses paired-end read information for improved gene detection and assembly validation.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and parameters for MyDbFinder.
