---
name: ntsm
category: utility
description: ntsm matches nucleotide sequences or samples for comparison and identification.
tags: [ntsm, utility, sequence-matching, sample-comparison]
author: oxo-call-community
source_url: "https://github.com/JustinChu/ntsm"
---

## Concepts

- **Tool Overview**: ntsm matches and compares nucleotide sequences or samples.
- **Core Function**: Identifies matches between sequences or samples.
- **Algorithm**: Uses sequence alignment and comparison methods.
- **Input Format**: Accepts FASTA sequences or sample identifiers.
- **Output**: Produces matching results and similarity scores.
- **Use Case**: Sequence identification, sample matching, and comparison.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Sequence Quality**: Results depend on input sequence quality.
- **Database Size**: Large databases require memory.
- **Computational Cost**: Matching can be computationally intensive.
- **False Positives**: May report incorrect matches.
- **Validation**: Results should be validated for accuracy.

## Examples

### Display help
**Args:** `ntsm --help`
**Explanation:** Shows available options and usage instructions.

### Match sequences
**Args:** `ntsm -i query.fasta -d database.fasta -o matches.txt`
**Explanation:** Matches query sequences against database.

### Sample matching
**Args:** `ntsm -s sample1.fastq -s2 sample2.fastq -o comparison.txt`
**Explanation:** Compares two samples for similarity.

### Output scores
**Args:** `ntsm -i query.fasta -d database.fasta -o matches.txt --scores`
**Explanation:** Outputs similarity scores.

### Threshold filtering
**Args:** `ntsm -i query.fasta -d database.fasta -t 0.9 -o matches.txt`
**Explanation:** Filters matches by similarity threshold.

### Threads
**Args:** `ntsm -i query.fasta -d database.fasta -t 8 -o matches.txt`
**Explanation:** Uses 8 threads for parallel processing.

### Verbose mode
**Args:** `ntsm -i query.fasta -d database.fasta -v -o matches.txt`
**Explanation:** Runs with verbose output.