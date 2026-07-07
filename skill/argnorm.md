---
name: argnorm
category: metagenomics
description: Normalize antibiotic resistance gene abundance using ARO ontology from CARD
tags: [argnorm, metagenomics, antibiotic-resistance, ARGs, CARD]
author: oxo-call-community
source_url: "https://argnorm.readthedocs.io/en/latest/"
---

## Concepts

- **Tool Overview**: ARGNorm normalizes antibiotic resistance gene (ARG) abundance tables from metagenomic analyses using the ARO (Antibiotic Resistance Ontology) from CARD (Comprehensive Antibiotic Resistance Database). Version 1.1.0.
- **Core Function**: Provides standardized normalization of ARG abundance data by mapping genes to ARO terms, enabling consistent comparison across studies.
- **CARD Integration**: Uses the curated CARD ontology for accurate ARG classification and normalization.
- **Abundance Normalization**: Converts raw read counts to normalized abundance values accounting for gene length and sequencing depth.
- **Metagenomics Support**: Designed for processing outputs from metagenomic profiling tools like MetaPhlAn, Kraken, and custom annotations.
- **Output Formats**: Supports TSV, CSV, and JSON output formats for downstream analysis.
- **Installation**: `conda install -c bioconda argnorm` or `pip install argnorm`.

## Pitfalls

- **Input Format**: Requires properly formatted abundance tables with gene identifiers. Check documentation for required format.
- **CARD Database**: Requires access to CARD database for ontology mapping. Updates may change normalization results.
- **Gene ID Matching**: IDs must match CARD database entries. Custom gene naming may require mapping files.
- **Version Compatibility**: Different CARD versions may have different ARO term mappings.
- **Large Tables**: Very large abundance tables may require significant memory for processing.

## Examples

### Normalize ARG abundance table
**Args:** `argnorm normalize --input abundance.tsv --output normalized_abundance.tsv`
**Explanation:** Normalizes raw ARG abundance values using ARO ontology and CARD database.

### Use custom ARO mapping
**Args:** `argnorm normalize --input abundance.csv --aro_mapping custom_aro.txt --output normalized.csv`
**Explanation:** Uses custom ARO mapping file instead of default CARD database.

### Filter by ARG category
**Args:** `argnorm filter --input normalized.tsv --category "beta-lactam" --output filtered.tsv`
**Explanation:** Filters normalized results to only include beta-lactam resistance genes.

### Generate summary report
**Args:** `argnorm report --input normalized.tsv --output report.html --format html`
**Explanation:** Creates HTML summary report with visualizations of ARG abundance profiles.

### Batch processing
**Args:** `argnorm batch --input_dir abundance_tables/ --output_dir normalized_results/`
**Explanation:** Processes multiple abundance table files in batch mode.

### Export for statistical analysis
**Args:** `argnorm export --input normalized.tsv --format json --output data.json`
**Explanation:** Exports normalized data in JSON format for integration with R or Python analysis pipelines.