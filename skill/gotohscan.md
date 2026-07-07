---
name: gotohscan
category: alignment
description: GotohScan is a sequence search tool that finds shorter sequences in large database sequences by computing all semi-global alignments.
tags: [gotohscan, sequence-search, alignment, bioinformatics]
author: oxo-call-community
source_url: "https://www.bioinf.uni-leipzig.de/Software/GotohScan/"
---

## Concepts

- **Semi-Global Alignment**: GotohScan performs semi-global alignments to find shorter sequences (queries) within larger database sequences (targets).

- **Exact Matching**: Identifies exact matches between query and target sequences using dynamic programming.

- **Multiple Query Support**: Supports searching multiple query sequences against a database in a single run.

- **Gap Penalties**: Configurable gap opening and extension penalties for flexible alignment scoring.

- **Output Formats**: Generates output in various formats including custom tabular format and BLAST-like output.

- **Performance Optimization**: Optimized for speed using efficient dynamic programming implementations.

## Pitfalls

- **Memory Usage**: Searching large databases may require significant memory. Consider splitting large databases.

- **Time Complexity**: Semi-global alignment has O(n*m) time complexity. Expect longer run times for very long sequences.

- **Gap Penalty Selection**: Poorly chosen gap penalties can significantly affect alignment quality. Use default values or optimize for your data.

- **Database Format**: Ensure the database is in the correct format. Convert FASTA files using provided utilities.

- **Query Length**: Very short queries may produce many false positives. Consider setting minimum hit length thresholds.

## Examples

### Basic sequence search
**Args:** `gotohscan -q query.fasta -d database.fasta -o results.txt`
**Explanation:** Searches query sequences against a database and outputs matches.

### Adjust gap penalties
**Args:** `gotohscan -q query.fasta -d database.fasta -gop -10 -gep -2 -o results.txt`
**Explanation:** Sets gap opening penalty to -10 and gap extension penalty to -2.

### Set minimum score threshold
**Args:** `gotohscan -q query.fasta -d database.fasta -s 50 -o results.txt`
**Explanation:** Only reports matches with alignment scores above 50.

### BLAST-like output
**Args:** `gotohscan -q query.fasta -d database.fasta -b -o blast_output.txt`
**Explanation:** Generates output in BLAST-like format for compatibility with downstream tools.

### Search multiple databases
**Args:** `gotohscan -q query.fasta -d db1.fasta db2.fasta db3.fasta -o results.txt`
**Explanation:** Searches queries against multiple databases simultaneously.

### Threaded execution
**Args:** `gotohscan -q query.fasta -d database.fasta -t 4 -o results.txt`
**Explanation:** Uses 4 threads for parallel processing to accelerate searches.

### Generate alignment report
**Args:** `gotohscan -q query.fasta -d database.fasta -a -o alignments.txt`
**Explanation:** Outputs full alignments along with match statistics.