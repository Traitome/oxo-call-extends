---
name: blast-legacy
category: alignment
description: Legacy version of BLAST for local similarity search between sequences
tags: [blast, legacy, alignment, sequence-search]
author: oxo-call-community
source_url: "https://blast.ncbi.nlm.nih.gov"
---

## Concepts

- **Tool Overview**: BLAST legacy (v2.2.26) is the original C toolkit version of BLAST for sequence similarity searching.
- **Core Function**: Finds regions of local similarity between nucleotide or protein sequences.
- **Programs**: blastall, formatdb, megablast, and other legacy tools.
- **Difference from BLAST+**: Uses C toolkit instead of C++; different command syntax.
- **Installation**: Install via bioconda: `conda install -c bioconda blast-legacy`

## Pitfalls

- **Deprecated**: Legacy version; use BLAST+ (blast package) for new analyses.
- **Command Syntax**: Uses blastall instead of blastn/blastp; different flag conventions.
- **Database Format**: Uses formatdb instead of makeblastdb for database creation.
- **Performance**: Slower than BLAST+ for most operations.

## Examples

### Format database
**Args:** `formatdb -i sequences.fa -p F`
**Explanation:** Creates nucleotide database (-p F) from FASTA file using legacy formatdb.

### Run blastall nucleotide search
**Args:** `blastall -p blastn -d database -i query.fa -o results.txt`
**Explanation:** Runs nucleotide BLAST search using legacy blastall command.

### Run megablast
**Args:** `blastall -p megablast -d database -i query.fa -o results.txt`
**Explanation:** Runs megablast for fast nucleotide search of similar sequences.

### Set e-value threshold
**Args:** `blastall -p blastn -d database -i query.fa -e 1e-5 -o results.txt`
**Explanation:** Sets e-value threshold to 1e-5 for significant matches.
