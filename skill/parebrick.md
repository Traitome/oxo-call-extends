---
name: parebrick
category: utility
description: PareBrick detects genome rearrangements in bacterial genomes.
tags: [parebrick, utility, genome-rearrangement, bacteria]
author: oxo-call-community
source_url: "https://github.com/ctlab/parallel-rearrangements"
---

## Concepts

- **Tool Overview**: PareBrick identifies genome rearrangements.
- **Core Function**: Detects structural rearrangements in bacterial genomes.
- **Algorithm**: Uses comparative genomics approach.
- **Input Format**: Accepts genome sequences and annotations.
- **Output**: Produces rearrangement predictions.
- **Use Case**: Comparative genomics, bacterial evolution.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Assembly Quality**: Results depend on assembly quality.
- **Genome Complexity**: Complex genomes may affect accuracy.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `parebrick --help`
**Explanation:** Shows available options and usage instructions.

### Detect rearrangements
**Args:** `parebrick -i genome.fasta -o rearrangements.txt`
**Explanation:** Identifies genome rearrangements.

### With reference
**Args:** `parebrick -i genome.fasta -r reference.fasta -o rearrangements.txt`
**Explanation:** Compares against reference genome.

### Verbose mode
**Args:** `parebrick -v -i genome.fasta -o rearrangements.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `parebrick -t 4 -i genome.fasta -o rearrangements.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `parebrick -i genome.fasta -o rearrangements.gff --gff`
**Explanation:** Outputs in GFF format.

### Minimum size
**Args:** `parebrick -m 1000 -i genome.fasta -o rearrangements.txt`
**Explanation:** Sets minimum rearrangement size.