---
name: spingo
category: metagenomics
description: SPINGO - Species level Identification of metagenomic amplicons
tags: [spingo, metagenomics, species-identification, amplicons, 16s]
author: oxo-call-community
source_url: "https://github.com/GuyAllard/SPINGO"
---

## Concepts

- **Tool Overview**: spingo (v1.3) - A species identification tool for metagenomic amplicons
- **Core Function**: Performs species-level identification from metagenomic amplicon sequences
- **Input/Output**: Accepts amplicon sequences; outputs species assignments
- **Algorithm**: Sequence alignment and database matching
- **Installation**: `conda install -c bioconda spingo`
- **Key Features**: Species identification, metagenomics, amplicon analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted amplicon sequences
- **Sequence Quality**: Sequence quality affects identification accuracy
- **Database Coverage**: Database coverage affects identification completeness
- **Memory Usage**: Large sequence sets require significant memory
- **Output Format**: Output format depends on configuration
- **Identification Accuracy**: Accuracy depends on sequence quality and database

## Examples

### Display help
**Args:** `spingo --help`
**Explanation:** Shows available options and usage information.

### Basic species identification
**Args:** `spingo -i amplicons.fasta -d database/ -o species_assignments.tsv`
**Explanation:** Identify species from amplicon sequences.

### With database
**Args:** `spingo -i amplicons.fasta -d refseq_db/ -o species_assignments.tsv`
**Explanation:** Use specific reference database.

### Multiple sequences
**Args:** `spingo -i amplicons1.fasta amplicons2.fasta -d database/ -o species_assignments.tsv`
**Explanation:** Identify species for multiple sequence files.

### With confidence threshold
**Args:** `spingo -i amplicons.fasta -d database/ -o species_assignments.tsv --confidence 0.9`
**Explanation:** Set confidence threshold for assignments.

### Output detailed results
**Args:** `spingo -i amplicons.fasta -d database/ -o species_assignments.tsv --detailed`
**Explanation:** Output detailed assignment information.

### Output alignments
**Args:** `spingo -i amplicons.fasta -d database/ -o species_assignments.tsv --alignments`
**Explanation:** Output sequence alignments.

### Output statistics
**Args:** `spingo -i amplicons.fasta -d database/ -o species_assignments.tsv --stats`
**Explanation:** Output identification statistics.

### Generate report
**Args:** `spingo -i amplicons.fasta -d database/ -o species_assignments.tsv --report`
**Explanation:** Generate identification report.

### With threads
**Args:** `spingo -i amplicons.fasta -d database/ -o species_assignments.tsv -p 8`
**Explanation:** Use multiple threads for identification.