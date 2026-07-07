---
name: parent-map
category: alignment
description: ParentMap analyzes parental contributions to evolved or engineered sequences.
tags: [parent-map, alignment, sequence-analysis, evolution]
author: oxo-call-community
source_url: "https://github.com/damienmarsic/parent-map"
---

## Concepts

- **Tool Overview**: ParentMap traces parental contributions in sequences.
- **Core Function**: Identifies parental origins of sequence segments.
- **Algorithm**: Uses sequence alignment and comparison.
- **Input Format**: Accepts FASTA sequences from parents and offspring.
- **Output**: Produces parental contribution maps.
- **Use Case**: Protein engineering, sequence evolution analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Similarity**: Results depend on sequence similarity.
- **Ambiguity**: May have ambiguous assignments.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `parent-map --help`
**Explanation:** Shows available options and usage instructions.

### Analyze sequences
**Args:** `parent-map -p parents.fasta -o offspring.fasta -r result.txt`
**Explanation:** Analyzes parental contributions.

### With reference
**Args:** `parent-map -p parents.fasta -o offspring.fasta -r reference.fasta -o result.txt`
**Explanation:** Uses reference sequence.

### Verbose mode
**Args:** `parent-map -v -p parents.fasta -o offspring.fasta -r result.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `parent-map -t 4 -p parents.fasta -o offspring.fasta -r result.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `parent-map -p parents.fasta -o offspring.fasta -r result.json --json`
**Explanation:** Outputs in JSON format.

### Minimum identity
**Args:** `parent-map -i 90 -p parents.fasta -o offspring.fasta -r result.txt`
**Explanation:** Sets minimum identity threshold.