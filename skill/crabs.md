---
name: crabs
category: utility
description: Creating Reference databases for Amplicon-Based Sequencing - build curated reference databases for eDNA metabarcoding
tags: [crabs, edna, metabarcoding, reference-database, bioinformatics, amplicon, environmental-dna, biodiversity]
author: oxo-call-community
source_url: "https://github.com/gjeunen/reference_database_creator"
---

## Concepts

- **Tool Overview**: CRABS (Creating Reference databases for Amplicon-Based Sequencing) is a software program for generating curated reference databases from eDNA metabarcoding sequencing data.
- **Core Function**: Downloads sequences from online repositories, performs in silico PCR to extract amplicon regions, curates and filters the database, and exports in formats ready for taxonomic classification.
- **Algorithm**: Seven-module workflow including download, import, PCR extraction, barcode matching, curation, export, and visualization. Supports parallel processing and multiple file formats.
- **Input**: Primer sequences (forward/reverse), marker gene database access, sequence data from BOLD, GenBank, or other repositories.
- **Output**: Curated reference database in multiple formats (FASTA, BLAST, IDTAXA, Qiime2, DADA2) for downstream taxonomic classification.
- **Application**: eDNA metabarcoding, biodiversity monitoring, aquatic species detection, diet analysis, environmental impact assessment.
- **Installation**: `conda install -c bioconda crabs` or clone GitHub repository with manual dependency installation.

## Pitfalls

- **Dependencies**: Requires multiple external tools (VSEARCH, MAFFT, BLAST+, etc.) for full functionality
- **Primer Mismatch**: Default allows 4 mismatches in primer-binding regions; adjust based on marker gene variability
- **Database Size**: Large reference databases require significant computational resources
- **In Silico PCR**: Results depend on primer specificity; may miss true variants or include non-target sequences
- **Taxonomic Curation**: Requires manual verification of taxonomic names and synonyms

## Examples

### Download sequences from BOLD
**Args:** `crabs download -i bold -o output_dir`
**Explanation:** Downloads reference sequences from BOLD (Barcode of Life Data System) database.

### Import sequences into CRABS format
**Args:** `crabs import -i raw_sequences.fasta -o crabs_format/`
**Explanation:** Converts downloaded sequences into CRABS internal format for processing.

### In silico PCR extraction
**Args:** `crabs pcr -i crabs_format/ -o pcr_output/ --forward GTCGGTAAAACTCGTGCCAGC --reverse CATAGTGGGGTATCTAATCCCAGTTTG`
**Explanation:** Extracts amplicon regions using specified primer sequences (MiFish-E primers shown).

### Extract with bidirectional PCR
**Args:** `crabs pcr -i crabs_format/ -o pcr_output/ --forward F_primers.txt --reverse R_primers.txt --bidirectional`
**Explanation:** Performs PCR extraction in both directions simultaneously.

### Filter by taxonomic rank
**Args:** `crabs filter -i curated_db/ -o filtered_db/ --rank species --threshold 0.9`
**Explanation:** Filters database to species-level annotations with 90% confidence threshold.

### Mismatch tolerance setting
**Args:** `crabs pcr -i crabs_format/ -o pcr_output/ --mismatch 2`
**Explanation:** Sets maximum allowed mismatches in primer regions to 2 (default is 4).

### Export to BLAST format
**Args:** `crabs export -i curated_db/ -o export/ --format blast`
**Explanation:** Exports reference database in BLAST format for local megablast analysis.

### Export to DADA2 format
**Args:** `crabs export -i curated_db/ -o export/ --format dada2`
**Explanation:** Exports in DADA2/R package format for amplicon sequence variant (ASV) classification.

### Visualize database statistics
**Args:** `crabs visualize -i curated_db/ -o plots/`
**Explanation:** Generates visualizations of database composition including taxonomic distribution and sequence length histograms.

### Build database with multiple markers
**Args:** `crabs download -i bold --marker COI -o coi_db/ && crabs download -i bold --marker 12S -o 12s_db/`
**Explanation:** Downloads sequences for multiple marker genes (COI and 12S rRNA) for multi-marker metabarcoding.
