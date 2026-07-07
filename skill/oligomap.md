---
name: oligomap
category: alignment
description: Oligomap is a program for fast identification of nearly-perfect matches of small RNAs in sequence databases.
tags: [oligomap, alignment, small-rna, sequence-search]
author: oxo-call-community
source_url: "https://github.com/zavolanlab/oligomap"
---

## Concepts

- **Tool Overview**: Oligomap identifies small RNA matches in sequence databases.
- **Core Function**: Finds nearly-perfect matches of small RNAs.
- **Algorithm**: Uses efficient sequence matching for small RNA detection.
- **Input Format**: Accepts small RNA sequences and sequence databases.
- **Output**: Produces matching results with locations and scores.
- **Use Case**: Small RNA analysis, RNA interference, and gene regulation studies.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Sequence Length**: Optimized for small RNAs, not long sequences.
- **Database Size**: Large databases require memory.
- **Mismatch Tolerance**: Limited mismatch handling.
- **Computational Cost**: Search can be intensive for large databases.
- **Validation**: Results should be validated experimentally.

## Examples

### Display help
**Args:** `oligomap --help`
**Explanation:** Shows available options and usage instructions.

### Search database
**Args:** `oligomap -i small_rnas.fasta -d genome.fasta -o matches.txt`
**Explanation:** Searches for small RNA matches in genome.

### With mismatches
**Args:** `oligomap -i small_rnas.fasta -d genome.fasta -m 2 -o matches.txt`
**Explanation:** Allows up to 2 mismatches.

### Output format
**Args:** `oligomap -i small_rnas.fasta -d genome.fasta -o matches.csv --csv`
**Explanation:** Outputs results in CSV format.

### Verbose mode
**Args:** `oligomap -i small_rnas.fasta -d genome.fasta -v -o matches.txt`
**Explanation:** Runs with verbose output.

### Build index
**Args:** `oligomap index -d genome.fasta -o index`
**Explanation:** Creates index for faster searching.

### Threads
**Args:** `oligomap -i small_rnas.fasta -d genome.fasta -t 4 -o matches.txt`
**Explanation:** Uses 4 threads for parallel processing.