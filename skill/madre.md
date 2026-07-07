---
name: madre
category: assembly
description: Strain-level metagenomic classification with Metagenome Assembly driven Database Reduction approach.
tags: [madre, assembly, metagenomics, classification]
author: oxo-call-community
source_url: "https://github.com/lbcb-sci/MADRe"
---

## Concepts

- **Tool Overview**: madre v0.0.5 - A strain-level metagenomic classification tool using Metagenome Assembly driven Database Reduction (MADRe) approach.
- **Core Function**: Reduces reference database complexity by leveraging metagenome assembly, enabling more accurate strain-level classification.
- **Input/Output**: Input: Raw reads (FASTQ), assembled contigs (FASTA); Output: Classification results with strain-level resolution.
- **Installation**: `conda install -c bioconda madre`
- **Database Reduction**: Reduces the reference database size by removing redundant sequences based on assembly coverage.
- **Strain Resolution**: Achieves strain-level classification by focusing on unique genomic regions.

## Pitfalls

- **Assembly Quality**: Poor assembly quality can significantly impact classification accuracy.
- **Database Completeness**: Incomplete reference databases may miss novel strains.
- **Computational Resources**: Memory-intensive for large metagenomic datasets.
- **Contamination**: Contaminant sequences can lead to false positive classifications.
- **Read Length**: Short reads may not provide enough information for strain-level resolution.
- **Species Bias**: May perform poorly for underrepresented species in the reference database.

## Examples

### Classify metagenomic reads
**Args:** `madre classify -i reads.fastq -r reference_db -o output`
**Explanation:** Classifies metagenomic reads at strain level.

### With assembled contigs
**Args:** `madre classify -i reads.fastq -c contigs.fasta -r reference_db -o output`
**Explanation:** Uses assembled contigs to guide database reduction.

### Build reduced database
**Args:** `madre reduce -c contigs.fasta -r reference_db -o reduced_db`
**Explanation:** Creates a reduced reference database based on assembly coverage.

### Quick classification
**Args:** `madre classify -i reads.fastq -r reference_db -o output --quick`
**Explanation:** Runs quick classification with reduced sensitivity.

### With minimum coverage threshold
**Args:** `madre classify -i reads.fastq -r reference_db -o output --min-cov 10`
**Explanation:** Sets minimum coverage threshold for database reduction.

### Verbose mode
**Args:** `madre classify -i reads.fastq -r reference_db -o output -v`
**Explanation:** Provides detailed logging during classification.