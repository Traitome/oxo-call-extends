---
name: galru
category: programming
description: Rapid spoligotyping for Mycobacterium tuberculosis directly from long read sequencing.
tags: [galru, Mycobacterium tuberculosis, spoligotyping, long read]
author: oxo-call-community
source_url: "https://github.com/quadram-institute-bioscience/galru"
---

## Concepts
- **Spoligotyping**: Genotyping method for Mycobacterium tuberculosis.
- **Long-read Analysis**: Analyzes long-read sequencing data.
- **Direct Analysis**: Performs analysis directly from sequencing data.
- **Strain Identification**: Identifies M. tuberculosis strains.
- **Spoligotype Patterns**: Detects spacer oligonucleotide types.

## Pitfalls
- **Long-read Quality**: Requires high-quality long reads.
- **Species Specific**: Designed specifically for M. tuberculosis.
- **Database Dependency**: Requires updated spoligotype database.
- **Coverage**: Requires sufficient sequencing coverage.
- **Complex Samples**: May struggle with mixed infections.

## Examples
### Run spoligotyping
**Args:** `galru -i reads.fastq -o spoligotype.txt`
**Explanation:** Performs spoligotyping from long reads.

### With reference database
**Args:** `galru -i reads.fastq -d database.fasta -o spoligotype.txt`
**Explanation:** Uses custom reference database.

### Specify genome position
**Args:** `galru -i reads.fastq -r chr:1000-5000 -o spoligotype.txt`
**Explanation:** Analyzes specific genomic region.

### Output JSON
**Args:** `galru -i reads.fastq -o results.json -f json`
**Explanation:** Outputs results in JSON format.

### Verbose mode
**Args:** `galru -i reads.fastq -v -o spoligotype.txt`
**Explanation:** Runs in verbose mode with detailed output.