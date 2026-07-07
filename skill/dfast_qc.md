---
name: dfast_qc
category: qc
description: DFAST_QC - Taxonomy and completeness check for prokaryotic genomes.
tags: [dfast_qc, qc, taxonomy, completeness, prokaryote]
author: oxo-call-community
source_url: "https://github.com/nigyta/dfast_qc"
---

## Concepts

- **Tool Overview**: dfast_qc (v1.1.1+) is a quality control tool for checking taxonomy and completeness of prokaryotic genomes. It integrates multiple quality assessment methods.
- **Core Function**: Verifies taxonomic assignment using marker genes and assesses genome completeness and contamination using CheckM-based metrics.
- **Input/Output**: Input: Genome assembly (FASTA), optional metadata. Output: Taxonomy reports, completeness/contamination metrics, quality scores.
- **Algorithm**: Uses single-copy marker genes for taxonomic classification and genome quality assessment.
- **Key Features**: Taxonomic classification, completeness estimation, contamination detection, quality scoring, report generation.
- **Installation**: `conda install -c bioconda dfast_qc`

## Pitfalls

- **Input Requirements**: Requires assembled genome in FASTA format with proper sequence headers.
- **Marker Gene Database**: Depends on up-to-date marker gene databases for accurate results.
- **Genome Quality**: Low-quality assemblies may produce unreliable completeness estimates.
- **Taxonomic Range**: Optimized for prokaryotes, may not work well for eukaryotic genomes.
- **Memory Usage**: May require significant memory for large genomes.

## Examples

### Check genome quality
**Args:** `dfast_qc --genome assembly.fa --output qc_report/`
**Explanation:** Checks taxonomy and completeness of prokaryotic genome.

### With custom database
**Args:** `dfast_qc --genome assembly.fa --output qc_report/ --db custom_markers/`
**Explanation:** Use custom marker gene database for analysis.

### Generate summary report
**Args:** `dfast_qc --genome assembly.fa --output qc_report/ --report summary.txt`
**Explanation:** Generate comprehensive quality summary report.

### Skip taxonomy check
**Args:** `dfast_qc --genome assembly.fa --output qc_report/ --skip-taxonomy`
**Explanation:** Skip taxonomic classification, only check completeness.

### Batch processing
**Args:** `dfast_qc --genome-dir genomes/ --output-dir qc_reports/`
**Explanation:** Process multiple genomes in batch mode.