---
name: bmfilter
category: metagenomics
description: Filter reads using BMTagger bitmask and SRPRISM databases
tags: [bmfilter, bmtagger, metagenomics, host-removal, filtering]
author: oxo-call-community
source_url: "ftp://ftp.ncbi.nlm.nih.gov/pub/agarwala/bmtagger/"
---

## Concepts

- **Tool Overview**: bmfilter removes host/contaminant reads using bitmask and SRPRISM databases.
- **Core Function**: Filters metagenomic reads that match known contaminant sequences.
- **Input**: FASTQ files and pre-built bitmask/SRPRISM databases.
- **Output**: Filtered reads without contaminant sequences.
- **Speed**: Very fast k-mer based filtering for large datasets.
- **Installation**: Install via bioconda: `conda install -c bioconda bmtagger`

## Pitfalls

- **Paired-End Filtering**: Both reads removed if either matches; use -1/-2 for paired data.
- **Database Path**: Ensure correct path to bitmask and SRPRISM databases.
- **Output Naming**: Use -o prefix to avoid overwriting input files.
- **Thread Count**: Use -t for parallel processing of large files.

## Examples

### Filter single-end reads
**Args:** `bmfilter -b human.bitmask reads.fq > filtered.fq`
**Explanation:** Removes human reads using bitmask database.

### Filter paired-end reads
**Args:** `bmfilter -b human.bitmask -x human.srprism -1 R1.fq -2 R2.fq -o filtered`
**Explanation:** Filters paired-end reads outputting filtered_R1.fq and filtered_R2.fq.

### Multi-threaded filtering
**Args:** `bmfilter -b human.bitmask -t 8 reads.fq > filtered.fq`
**Explanation:** Uses 8 threads for faster filtering of large datasets.

### Save removed reads
**Args:** `bmfilter -b human.bitmask reads.fq -o filtered -r removed.fq`
**Explanation:** Saves both filtered and removed reads to separate files.

### Quick k-mer only filtering
**Args:** `bmfilter -b human.bitmask reads.fq -o filtered.fq`
**Explanation:** Fast filtering using only bitmask without alignment step.
