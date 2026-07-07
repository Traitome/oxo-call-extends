---
name: locidex
category: typing
description: Locidex - Common search engine for similarity-based typing applications
tags: [locidex, typing, search-engine, similarity, bioinformatics, typing-tools]
author: oxo-call-community
source_url: "https://pypi.org/project/locidex"
---

## Concepts

- **Similarity Search**: Similarity-based search for typing applications
- **Sequence Typing**: Sequence-based typing of organisms
- **Search Engine**: Built-in search engine for sequence comparison
- **Database Management**: Management of typing databases
- **Fast Search**: Fast similarity search algorithms
- **Multiple Databases**: Support for multiple typing databases

## Pitfalls

- **Database Quality**: Poor quality databases affect typing
- **Sequence Quality**: Poor quality sequences affect results
- **Memory Usage**: Memory-intensive for large databases
- **Parameter Tuning**: Requires careful parameter optimization
- **False Positives**: May produce false positive matches
- **Database Updates**: Database must be regularly updated

## Examples

### Search database
**Args:** `locidex search -i query.fasta -d database/ -o results.txt`
**Explanation:** Searches database for similar sequences.

### Build database
**Args:** `locidex build -i sequences.fasta -o database/`
**Explanation:** Builds typing database from sequences.

### Update database
**Args:** `locidex update -d database/ -i new_sequences.fasta`
**Explanation:** Updates existing database with new sequences.

### Threads
**Args:** `locidex search -i query.fasta -d database/ -o results.txt -t 8`
**Explanation:** Uses 8 threads for parallel processing.

### Similarity threshold
**Args:** `locidex search -i query.fasta -d database/ -o results.txt -s 0.95`
**Explanation:** Sets minimum similarity threshold to 95%.

### Output format
**Args:** `locidex search -i query.fasta -d database/ -o results.json -f json`
**Explanation:** Outputs results in JSON format.