---
name: lambda
category: alignment
description: Local aligner optimized for many query sequences searching in protein space
tags: [lambda, alignment, protein-alignment, sequence-search, BLAST, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/seqan/lambda"
---

## Concepts

- **Protein Sequence Alignment**: Local aligner for protein sequences
- **Massive Query Support**: Optimized for large numbers of queries
- **BLAST-like Search**: Similar to BLASTP but faster
- **Index-based**: Uses indexing for fast similarity search
- **DNA to Protein**: Can translate DNA queries to protein space
- **Database Search**: Searches against protein sequence databases

## Pitfalls

- **Database Size**: Large databases increase search time
- **Memory Usage**: Index construction requires significant memory
- **Scoring Matrix**: Matrix selection affects alignment quality
- **Gap Penalties**: Gap penalty tuning needed for best results
- **Query Length**: Very short queries may give poor results
- **E-value Threshold**: E-value cutoff affects sensitivity/specificity

## Examples

### Search protein database
**Args:** `lambda -q queries.fasta -d database.fasta -o results.m8`
**Explanation:** Searches queries against protein database.

### DNA query to protein DB
**Args:** `lambda -q queries.fna -d database.faa -o results.m8 -s`
**Explanation:** Translates DNA queries before search.

### Specify scoring matrix
**Args:** `lambda -q queries.fasta -d db.fasta -o results -mat BLOSUM62`
**Explanation:** Uses BLOSUM62 scoring matrix.

### Set E-value cutoff
**Args:** `lambda -q queries.fasta -d db.fasta -e 1e-10 -o results.m8`
**Explanation:** Only reports matches with E-value < 1e-10.

### Adjust gap penalties
**Args:** `lambda -q queries.fasta -d db.fasta -g 11 -e 1 -o results.m8`
**Explanation:** Sets gap open=11, gap extend=1.

### Paired-end output
**Args:** `lambda -q queries.fasta -d db.fasta -o results --tabbed`
**Explanation:** Outputs in tabbed format for easy parsing.