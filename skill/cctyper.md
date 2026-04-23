---
name: cctyper
category: annotation
description: Automatic detection and subtyping of CRISPR-Cas operons
tags: [cctyper, crispr, cas, typing, annotation]
author: oxo-call-community
source_url: "https://github.com/Russel88/CRISPRCasTyper"
---

## Concepts

- **Tool Overview**: CRISPRCasTyper detects and subtypes CRISPR-Cas operons in genomic sequences.
- **Core Function**: Identifies CRISPR arrays and Cas genes, then assigns subtype.
- **Algorithm**: Combines CRISPR detection with Cas gene HMM search for subtype classification.
- **Input**: Assembled genome or metagenome in FASTA format.
- **Output**: CRISPR arrays, Cas genes, and subtype assignments.
- **Subtypes**: Detects all major CRISPR-Cas types and subtypes.
- **Installation**: Install via bioconda: `conda install -c bioconda cctyper`

## Pitfalls

- **Assembly Required**: Requires assembled genome, not raw reads.
- **Database**: Downloads HMM database on first run.
- **Fragmented Genomes**: Incomplete genomes may have split operons.
- **Novel Subtypes**: Novel or divergent subtypes may be unclassified.

## Examples

### Detect CRISPR-Cas systems
**Args:** `cctyper genome.fa output_dir/`
**Explanation:** Detects and subtypes CRISPR-Cas operons in genome.

### Set minimum array repeats
**Args:** `cctyper genome.fa output/ --min_repeats 3`
**Explanation:** Requires minimum 3 repeats for CRISPR array detection.

### Set threads
**Args:** `cctyper genome.fa output/ -t 8`
**Explanation:** Uses 8 threads for faster analysis.

### Verbose output
**Args:** `cctyper genome.fa output/ -v`
**Explanation:** Prints detailed progress information.

### Display help
**Args:** `cctyper --help`
**Explanation:** Shows all available options and usage information.
