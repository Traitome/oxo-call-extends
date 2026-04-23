---
name: bmtagger
category: metagenomics
description: Best Match Tagger for removing host reads from metagenomics datasets
tags: [bmtagger, metagenomics, host-removal, decontamination]
author: oxo-call-community
source_url: "ftp://ftp.ncbi.nlm.nih.gov/pub/agarwala/bmtagger/"
---

## Concepts

- **Tool Overview**: BMTagger (Best Match Tagger) removes contaminating reads from metagenomics datasets, commonly used for human read removal.
- **Core Function**: Identifies and filters host reads using k-mer matching and alignment approaches.
- **Components**: bmtool (creates bitmask), srprism (aligns reads), bmfilter (filters reads).
- **Workflow**: Build database bitmask → align reads → filter based on matches.
- **Speed**: Very fast for removing known contaminant sequences.
- **Installation**: Install via bioconda: `conda install -c bioconda bmtagger`

## Pitfalls

- **Database Required**: Must create bitmask database from host genome before filtering.
- **Memory Usage**: Bitmask creation requires memory proportional to genome size.
- **False Positives**: May remove some non-host reads with high similarity to host sequences.
- **Paired-End Handling**: Both reads of a pair are removed if either matches.
- **Database Path**: Use BMTAGGER_DB environment variable or config file for database location.

## Examples

### Create bitmask database
**Args:** `bmtool -d human_genome.fa -o human.bitmask -w 18`
**Explanation:** Creates 18-mer bitmask database from human genome for read filtering.

### Create SRPRISM database
**Args:** `srprism mkindex -i human_genome.fa -o human.srprism`
**Explanation:** Creates SRPRISM index for alignment-based filtering.

### Filter single-end reads
**Args:** `bmfilter -b human.bitmask -x human.srprism -t 8 reads.fq > filtered.fq`
**Explanation:** Removes human reads using bitmask and SRPRISM databases with 8 threads.

### Filter paired-end reads
**Args:** `bmfilter -b human.bitmask -x human.srprism -1 R1.fq -2 R2.fq -t 8 -o filtered`
**Explanation:** Filters paired-end reads, outputting both filtered R1 and R2 files.

### Quick filtering with bitmask only
**Args:** `bmfilter -b human.bitmask reads.fq > filtered.fq`
**Explanation:** Fast k-mer based filtering without alignment step.

### Extract removed reads
**Args:** `bmfilter -b human.bitmask reads.fq -o filtered.fq -r removed.fq`
**Explanation:** Saves both filtered reads and removed contaminant reads.
