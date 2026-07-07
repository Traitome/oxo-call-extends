---
name: dfam
category: annotation
description: Dfam - database and scanning tool for repetitive DNA elements in eukaryotic genomes.
tags: [dfam, annotation, repeat, transposable-element, hmm]
author: oxo-call-community
source_url: "https://dfam.org"
---

## Concepts

- **Tool Overview**: dfam (v3.7+) is a database and scanning tool for repetitive DNA elements (transposable elements) in eukaryotic genomes. It uses HMM-based profiles for repeat identification.
- **Core Function**: Identifies and annotates transposable elements, retrotransposons, and other repetitive sequences using a comprehensive database of HMM profiles.
- **Input/Output**: Input: Genome FASTA files. Output: Repeat annotations (GFF/FASTA), classification, consensus sequences.
- **Algorithm**: Uses hidden Markov models (HMMs) to scan sequences and identify matches to known repetitive element families.
- **Key Features**: Comprehensive repeat database, HMM-based detection, classification hierarchy, consensus generation, batch processing.
- **Installation**: `conda install -c bioconda dfam`

## Pitfalls

- **Database Update**: Requires regular database updates for new repeat families.
- **Computational Time**: Scanning large genomes can be time-consuming.
- **False Positives**: May produce false positive matches in low-complexity regions.
- **Memory Usage**: May require significant memory for large genomes.
- **Database Size**: Full Dfam database is large and requires significant storage.

## Examples

### Scan genome for repetitive elements
**Args:** `dfamscan.pl --seq genome.fa --output repeats.gff`
**Explanation:** Scans genome for repetitive elements using Dfam HMM profiles.

### With custom database
**Args:** `dfamscan.pl --seq genome.fa --output repeats.gff --hmm-db custom.hmm`
**Explanation:** Use custom HMM database for repeat scanning.

### Generate consensus sequences
**Args:** `dfamscan.pl --seq genome.fa --output repeats.gff --consensus consensus.fa`
**Explanation:** Generate consensus sequences for detected repeats.

### Parallel processing
**Args:** `dfamscan.pl --seq genome.fa --output repeats.gff --cpu 8`
**Explanation:** Use 8 CPU cores for parallel processing.

### Filter by repeat type
**Args:** `dfamscan.pl --seq genome.fa --output repeats.gff --filter-type DNA`
**Explanation:** Only report DNA transposons, filtering out other repeat types.