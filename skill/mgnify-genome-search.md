---
name: mgnify-genome-search
category: utility
description: MAGs queue script against MGnify database
tags: [mgnify-genome-search, utility, metagenomics]
author: oxo-call-community
source_url: "https://github.com/SantaMcCloud/MGnify-genome-search"
---

## Concepts

- **Tool Overview**: mgnify-genome-search v1.0.0 is a script for querying MAGs (Metagenome-Assembled Genomes) against the MGnify database.
- **Core Function**: Searches MGnify database for matching genomes.
- **Database Query**: Queries the MGnify database for genome comparisons.
- **MAG Analysis**: Analyzes metagenome-assembled genomes against reference databases.
- **Input/Output**: Accepts MAG sequences; outputs matching results from MGnify.
- **Taxonomic Comparison**: Compares MAGs against known reference genomes.

## Pitfalls

- **Network Requirements**: Requires internet access to query MGnify database.
- **Database Updates**: Database content may change over time.
- **Computational Resources**: Processing large MAG sets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal search results.
- **Data Quality**: Search accuracy depends on input MAG quality.

## Examples

### Search MGnify database
**Args:** `mgnify-genome-search -i mag.fasta -o results.txt`
**Explanation:** Searches MGnify database for matching genomes.

### With custom parameters
**Args:** `mgnify-genome-search -i mag.fasta -o results.txt -e 1e-10`
**Explanation:** Uses e-value threshold of 1e-10 for searching.

### Batch processing
**Args:** `mgnify-genome-search -i mags/ -o results/`
**Explanation:** Processes multiple MAGs in batch mode.

### Detailed output
**Args:** `mgnify-genome-search -i mag.fasta -o results.txt -v`
**Explanation:** Generates detailed search report.

### Taxonomic filtering
**Args:** `mgnify-genome-search -i mag.fasta -o results.txt -t Bacteria`
**Explanation:** Filters results by taxonomic group.