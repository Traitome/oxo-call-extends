---
name: kaiju
category: metagenomics
description: Fast and sensitive taxonomic classification for metagenomics using k-mers.
tags: [kaiju, metagenomics, classification, k-mer, taxonomy]
author: oxo-call-community
source_url: "https://github.com/bioinformatics-centre/kaiju/blob/v1.10.1/README.md"
---

## Concepts

- **Tool Overview**: kaiju (v1.10.1) - A fast and sensitive taxonomic classification tool for metagenomics.
- **k-mer Matching**: Uses k-mer based approach for classification.
- **Database**: Requires pre-built reference database for classification.
- **Speed**: Designed for fast classification of large metagenomic datasets.
- **Sensitivity**: High sensitivity for detecting low-abundance taxa.
- **Output**: Generates classification results with taxonomic assignments.

## Pitfalls

- **Database Size**: Reference databases can be large and require significant storage.
- **Memory Usage**: Classification requires memory for k-mer index.
- **False Positives**: Can produce false positive classifications.
- **Low Coverage**: Low-coverage reads may not be classified.
- **Database Updates**: Requires regular database updates.
- **Taxonomic Resolution**: Limited by database completeness.

## Examples

### Build database
**Args:** `kaiju-makedb -o kaiju_db -p`
**Explanation:** Builds Kaiju reference database with proteins.

### Classify reads
**Args:** `kaiju -t nodes.dmp -f kaiju_db.fmi -i reads.fastq -o kaiju.out`
**Explanation:** Classifies reads using built database.

### Generate summary report
**Args:** `kaiju2table -t nodes.dmp -n names.dmp -i kaiju.out -o kaiju_summary.tsv`
**Explanation:** Generates human-readable summary table.

### Filter by confidence
**Args:** `kaiju -t nodes.dmp -f kaiju_db.fmi -i reads.fastq -o kaiju.out -c 0.9`
**Explanation:** Filters results by confidence threshold 0.9.

### Pair-end mode
**Args:** `kaiju -t nodes.dmp -f kaiju_db.fmi -i reads_1.fastq -j reads_2.fastq -o kaiju.out`
**Explanation:** Processes paired-end reads.

### Output in SAM format
**Args:** `kaiju -t nodes.dmp -f kaiju_db.fmi -i reads.fastq -o kaiju.sam -s`
**Explanation:** Outputs classification results in SAM format.