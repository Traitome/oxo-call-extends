---
name: bactopia-teton
category: metagenomics
description: Bactopia Teton - Taxonomic classification component for Bactopia pipeline
tags: [bactopia-teton, metagenomics, taxonomic-classification, kraken2, centrifuge]
author: oxo-call-community
source_url: "https://bactopia.github.io/"
---

## Concepts

- **Tool Overview**: Bactopia Teton is the taxonomic classification component of the Bactopia pipeline, providing comprehensive taxonomic identification of bacterial sequences. Version 1.1.3.
- **Core Function**: Performs taxonomic classification of sequencing reads or assemblies.
- **Kraken2 Integration**: Uses Kraken2 for accurate taxonomic assignment.
- **Centrifuge Support**: Also supports Centrifuge for alternative classification approach.
- **Database Integration**: Works with standard taxonomic databases (NCBI, RefSeq, etc.).
- **Output Formats**: Generates classification reports in multiple formats.
- **Input/Output**: Accepts FASTQ reads or FASTA assemblies, outputs taxonomic assignments.
- **Installation**: `conda install -c bioconda bactopia-teton`.

## Pitfalls

- **Version Compatibility**: Must match Bactopia pipeline version for proper integration.
- **Database Requirements**: Requires large taxonomic databases. Pre-download for better performance.
- **Memory Usage**: Classification requires significant memory, especially with large databases.
- **Classification Confidence**: Low-confidence assignments may require manual review.
- **Database Updates**: Taxonomic databases change frequently. Keep databases updated.

## Examples

### Classify reads
**Args:** `bactopia-teton --input reads.fastq --output classification/`
**Explanation:** Performs taxonomic classification on sequencing reads.

### Classify assembly
**Args:** `bactopia-teton --input assembly.fasta --type assembly --output classification/`
**Explanation:** Classifies assembled contigs instead of raw reads.

### Use custom database
**Args:** `bactopia-teton --input reads.fastq --database custom_db --output classification/`
**Explanation:** Uses custom taxonomic database for classification.

### Kraken2 specific
**Args:** `bactopia-teton --input reads.fastq --method kraken2 --output classification/`
**Explanation:** Uses Kraken2 for taxonomic classification.

### Centrifuge specific
**Args:** `bactopia-teton --input reads.fastq --method centrifuge --output classification/`
**Explanation:** Uses Centrifuge for taxonomic classification.

### Generate report
**Args:** `bactopia-teton --input reads.fastq --output classification/ --report report.html`
**Explanation:** Generates HTML summary report of classification results.

### Confidence threshold
**Args:** `bactopia-teton --input reads.fastq --confidence 0.8 --output classification/`
**Explanation:** Sets minimum confidence threshold for assignments.

### Display help
**Args:** `bactopia-teton --help`
**Explanation:** Shows all available command-line options and usage information.