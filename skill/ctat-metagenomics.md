---
name: ctat-metagenomics
category: metagenomics
description: ctat-metagenomics uses centrifuge for metagenomic taxonomic classification
tags: [ctat-metagenomics, metagenomics, centrifuge, taxonomy, classification]
author: oxo-call-community
source_url: "https://github.com/NCIP/ctat-metagenomics"
---

## Concepts

- **Tool Overview**: ctat-metagenomics (v1.0.1+) is a metagenomic analysis pipeline that uses Centrifuge for rapid taxonomic classification.
- **Core Function**: Identifies and quantifies microbial species in metagenomic sequencing data using a reference database.
- **Input/Output**: Input: FASTQ reads, reference database index. Output: Taxonomic classification reports, abundance profiles.
- **Algorithm**: Uses Centrifuge's k-mer based classification algorithm for fast and accurate species identification.
- **Key Features**: Supports both short-read and long-read data, provides abundance estimates, generates interactive visualization reports.
- **Installation**: `conda install -c bioconda ctat-metagenomics`

## Pitfalls

- **Database Download**: Requires large reference databases; use `ctat-metagenomics download` to fetch.
- **Index Building**: First run requires index building; time-consuming for large databases.
- **Memory Requirements**: Classification of large datasets may require significant memory.
- **Taxonomic Resolution**: Depends on reference database completeness; rare species may be missed.
- **Output Files**: Multiple output files generated; ensure output directory exists.

## Examples

### Download reference database
**Args:** `ctat-metagenomics download --db refseq`
**Explanation:** Download the RefSeq reference database for taxonomic classification.

### Classify metagenomic reads
**Args:** `ctat-metagenomics classify -1 reads_R1.fastq -2 reads_R2.fastq -o results/`
**Explanation:** Classify paired-end metagenomic reads and generate taxonomic reports.

### Generate abundance profile
**Args:** `ctat-metagenomics profile -i classification.txt -o abundance.tsv --level species`
**Explanation:** Generate species-level abundance profile from classification results.
