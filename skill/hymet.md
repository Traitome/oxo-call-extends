---
name: hymet
category: metagenomics
description: HYMET - Hybrid Mash+minimap2 metagenomic classification
tags: [hymet, metagenomics, classification, Mash, minimap2]
author: oxo-call-community
source_url: "https://github.com/ieeta-pt/HYMET"
---

## Concepts

- **Tool Overview**: HYMET provides hybrid Mash+minimap2 metagenomic classification with benchmark and case-study tooling.
- **Hybrid Classification**: Couples Mash candidate filtering with minimap2 alignment for accurate classification.
- **Weighted LCA Resolver**: Uses weighted lowest common ancestor algorithm for taxonomic assignments.
- **Dual Pipeline**: Supports both contig-level and read-level classification.
- **Benchmark Harnesses**: Includes CAMI benchmark harnesses for reproducible evaluation.
- **Installation**: `conda install -c bioconda hymet`

## Pitfalls

- **Mash Distance**: Appropriate Mash distance threshold selection affects candidate identification.
- **Alignment Parameters**: Minimap2 parameters may need adjustment based on read type.
- **Database Format**: Requires properly formatted reference database with taxonomic information.
- **Memory Requirements**: Large reference databases require sufficient memory.
- **Taxonomic Resolution**: Limited by the taxonomic depth of the reference database.
- **Perl Dependencies**: Legacy Perl pipeline may require additional dependencies.

## Examples

### Classify contigs
**Args:** `hymet classify -i contigs.fasta -db reference_db/ -o taxonomy.tsv`
**Explanation:** Classifies assembled contigs using hybrid Mash+minimap2 approach.

### Classify reads directly
**Args:** `hymet classify-reads -i reads.fastq -db reference_db/ -o read_taxonomy.tsv`
**Explanation:** Performs direct read-level taxonomic classification.

### Build reference database
**Args:** `hymet build-db -i genomes/ -o reference_db/`
**Explanation:** Builds a reference database from a directory of genome sequences.

### Run CAMI benchmark
**Args:** `hymet benchmark -i cami_data/ -o benchmark_results/`
**Explanation:** Runs CAMI benchmark evaluation with standardized metrics.

### Generate visualization
**Args:** `hymet visualize -i taxonomy.tsv -o plot.pdf`
**Explanation:** Generates visualization of taxonomic profiles.