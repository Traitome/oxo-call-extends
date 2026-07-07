---
name: dbcan
category: annotation
description: Standalone version of dbCAN annotation tool for automated CAZyme annotation.
tags: [dbcan, annotation, CAZyme, carbohydrate, enzyme]
author: oxo-call-community
source_url: "https://run-dbcan.readthedocs.io/en/latest"
---

## Concepts

- **Tool Overview**: dbcan (v5.2.8+) is a standalone tool for automated Carbohydrate-Active Enzyme (CAZyme) annotation. It integrates HMMER, DIAMOND, and eCAMI methods to identify CAZyme domains in protein sequences.
- **Core Function**: Annotates carbohydrate-active enzymes in genomic or protein sequences by searching against the dbCAN database (CAZy database) using multiple complementary approaches.
- **Input/Output**: Input: Protein FASTA or nucleotide FASTA (genomic contigs). Output: CAZyme annotations in GFF3 format, summary tables, and domain architecture.
- **Algorithm**: Uses three approaches: HMMER (HMM profiles from dbCAN), DIAMOND (sequence similarity), and eCAMI (deep learning). Combines results for high-confidence predictions.
- **Key Features**: Multi-method consensus, supports metagenomic data, provides substrate specificity predictions, and outputs comprehensive annotation reports.
- **Installation**: `conda install -c bioconda dbcan`

## Pitfalls

- **Database Version**: Results depend on dbCAN database version.
- **Input Type**: Requires protein sequences or correctly formatted nucleotide sequences.
- **E-value Threshold**: Default thresholds may need adjustment for specific datasets.
- **Computational Resources**: HMMER searches can be computationally intensive.
- **False Positives**: Some domains may be misannotated; manual curation recommended.

## Examples

### Annotate protein sequences
**Args:** `run_dbcan protein.fasta protein -o output_dir`
**Explanation:** Annotate CAZymes in protein FASTA file using all three methods.

### Annotate genomic contigs
**Args:** `run_dbcan contigs.fasta genome -o output_dir`
**Explanation:** Predict proteins from genomic contigs and annotate CAZymes.

### Use specific method
**Args:** `run_dbcan protein.fasta protein --dbcan_file dbCAN-HMMdb.txt --out_dir output`
**Explanation:** Run annotation using HMMER method only.