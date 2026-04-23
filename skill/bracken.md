---
name: bracken
category: metagenomics
description: Bayesian Reestimation of Abundance with KrakEN for species abundance estimation
tags: [bracken, kraken, metagenomics, abundance, taxonomic-classification]
author: oxo-call-community
source_url: "https://github.com/jenniferlu717/Bracken"
---

## Concepts

- **Tool Overview**: Bracken is a statistical method that computes species abundance from Kraken classification results.
- **Core Function**: Re-estimates species abundance by redistributing reads assigned to higher taxonomic levels.
- **Workflow**: Requires Kraken database built with bracken-build before abundance estimation.
- **Classification Levels**: Supports species (S), genus (G), family (F), order (O), class (C), phylum (P), domain (D) levels.
- **Database Requirement**: Must run bracken-build to generate kmer distribution files for the Kraken database.
- **Installation**: Install via bioconda: `conda install -c bioconda bracken`

## Pitfalls

- **Database Compatibility**: Bracken database must match the Kraken database used for classification.
- **Read Length**: Specify correct read length (-r) that matches sample read length.
- **Threshold Setting**: Default threshold of 10 reads may need adjustment for low-biomass samples.
- **Kmer Length**: Must match kmer length used in Kraken database construction.
- **Output Interpretation**: Added_reads column shows reads redistributed from higher taxonomic levels.

## Examples

### Build Bracken database
**Args:** `bracken-build -d kraken_db -k 35 -l 100 -t 8`
**Explanation:** Builds Bracken database files from Kraken database with 35-mer length and 100bp read length.

### Estimate species abundance
**Args:** `bracken -d kraken_db -i sample.kreport -o sample.bracken -l S -r 100`
**Explanation:** Estimates species-level abundance from Kraken report file.

### Estimate genus-level abundance
**Args:** `bracken -d kraken_db -i sample.kreport -o sample_genus.bracken -l G -r 100`
**Explanation:** Estimates genus-level abundance from Kraken classification results.

### Adjust read threshold
**Args:** `bracken -d kraken_db -i sample.kreport -o sample.bracken -l S -r 100 -t 5`
**Explanation:** Uses threshold of 5 reads minimum for abundance re-estimation.

### Multiple classification levels
**Args:** `bracken -d kraken_db -i sample.kreport -o sample.bracken -l S -r 150`
**Explanation:** Estimates species abundance for 150bp reads from Kraken report.

### Full workflow example
**Args:** `kraken2 --db kraken_db --report sample.kreport sample.fq > sample.kraken && bracken -d kraken_db -i sample.kreport -o sample.bracken -l S -r 100`
**Explanation:** Classifies reads with Kraken2 and estimates abundance with Bracken in one pipeline.

### Using Python script directly
**Args:** `estimate_abundance.py -i sample.kreport -k kraken_db/database100mers.kmer_distrib -o sample.bracken -l S`
**Explanation:** Direct Python script for abundance estimation with explicit kmer distribution file.
