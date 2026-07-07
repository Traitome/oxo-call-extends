---
name: msi
category: utility
description: Metabarcoding sequences identification from nanopore reads to taxa tables.
tags: [msi, utility, metagenomics]
author: oxo-call-community
source_url: "https://github.com/nunofoneca/msi"
---

## Concepts

- **Tool Overview**: MSI v0.3.8 identifies metabarcoding sequences from nanopore data.
- **Core Function**: Processes nanopore reads for taxonomic classification.
- **Metabarcoding**: Specialized for DNA metabarcoding analysis.
- **Nanopore Support**: Optimized for Oxford Nanopore sequencing data.
- **Taxonomic Assignment**: Assigns taxonomy to sequencing reads.
- **Input/Output**: Accepts FASTQ reads; outputs taxa tables.

## Pitfalls

- **Nanopore Specific**: Designed for nanopore sequencing data.
- **Barcode Quality**: Results depend on barcode quality.
- **Memory Requirements**: Memory usage depends on dataset size.
- **Parameter Tuning**: May require parameter adjustment for classification.
- **Database Dependence**: Requires reference database for classification.
- **Computational Resources**: Large datasets may require significant resources.

## Examples

### Identify sequences
**Args:** `msi -i reads.fastq -o taxa_table.txt`
**Explanation:** Identifies taxonomic composition from reads.

### With custom database
**Args:** `msi -i reads.fastq -d custom_db -o taxa_table.txt`
**Explanation:** Uses custom reference database.

### Generate taxa table
**Args:** `msi -i reads.fastq -t -o taxa_table.csv`
**Explanation:** Outputs formatted taxa table.

### Batch processing
**Args:** `msi -i fastq/ -o results/`
**Explanation:** Processes multiple sample files.

### Generate report
**Args:** `msi -i reads.fastq -r report.html -o taxa_table.txt`
**Explanation:** Generates analysis report.