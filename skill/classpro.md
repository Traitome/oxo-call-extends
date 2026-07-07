---
name: classpro
category: metagenomics
description: K-mer classifier for HiFi reads
tags: [classpro, metagenomics, hifi, k-mer, classification]
author: oxo-call-community
source_url: "https://github.com/yoshihikosuzuki/ClassPro/"
---

## Concepts

- **Tool Overview**: ClassPro is a K-mer based sequence classifier specifically designed for PacBio HiFi reads, providing accurate taxonomic classification.
- **Core Function**: Classifies HiFi sequencing reads to their most likely source organism using k-mer matching.
- **Algorithm**: Uses discriminative k-mers for fast and accurate classification of high-quality long reads.
- **Input**: PacBio HiFi reads (FASTQ/FASTA) and reference database.
- **Output**: Taxonomic classification results with confidence scores.
- **Application**: Metagenomic analysis, taxonomic profiling, and microbiome research using HiFi data.
- **Installation**: Install via bioconda: `conda install -c bioconda classpro`

## Pitfalls

- **HiFi Data**: Optimized for HiFi reads; may not work optimally with other data types.
- **Database Requirement**: Requires reference database for classification.
- **Memory Usage**: May require significant memory for large databases.
- **K-mer Selection**: Appropriate k-mer size must be chosen.
- **Computational Resources**: May require significant compute resources.

## Examples

### Classify HiFi reads
**Args:** `classpro -i hifi_reads.fastq -d database -o results.txt`
**Explanation:** Classifies PacBio HiFi reads against reference database.

### Build reference database
**Args:** `classpro_build -g genomes/*.fasta -o database`
**Explanation:** Builds reference database from genome FASTA files.

### With confidence threshold
**Args:** `classpro -i hifi_reads.fastq -d database -c 0.8 -o results.txt`
**Explanation:** Filters results to include only confident classifications.

### Display help
**Args:** `classpro --help`
**Explanation:** Shows all available options and usage information.