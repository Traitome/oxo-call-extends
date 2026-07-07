---
name: nohuman
category: utility
description: nohuman removes human reads from sequencing data to enrich non-human sequences.
tags: [nohuman, utility, filtering, human-removal]
author: oxo-call-community
source_url: "https://github.com/mbhall88/nohuman"
---

## Concepts

- **Tool Overview**: nohuman filters out human reads from sequencing data.
- **Core Function**: Removes human sequences to enrich non-human content.
- **Algorithm**: Uses alignment to human reference for read classification.
- **Input Format**: Accepts FASTQ reads.
- **Output**: Produces filtered FASTQ with non-human reads.
- **Use Case**: Metagenomics, pathogen detection, and contamination removal.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Reference Genome**: Requires human reference genome.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Alignment can be computationally intensive.
- **Sensitivity**: May miss some human reads.
- **False Positives**: May remove non-human reads.

## Examples

### Display help
**Args:** `nohuman --help`
**Explanation:** Shows available options and usage instructions.

### Filter human reads
**Args:** `nohuman -i reads.fastq -o filtered.fastq`
**Explanation:** Removes human reads from FASTQ.

### Paired-end reads
**Args:** `nohuman -i reads_1.fastq -i2 reads_2.fastq -o filtered/`
**Explanation:** Processes paired-end reads.

### Custom reference
**Args:** `nohuman -i reads.fastq -r human_reference.fasta -o filtered.fastq`
**Explanation:** Uses custom human reference.

### Threads
**Args:** `nohuman -i reads.fastq -t 8 -o filtered.fastq`
**Explanation:** Uses 8 threads for parallel processing.

### Output statistics
**Args:** `nohuman -i reads.fastq -o filtered.fastq --stats`
**Explanation:** Generates filtering statistics.

### Keep human reads
**Args:** `nohuman -i reads.fastq -o human.fastq --keep-human`
**Explanation:** Keeps human reads instead of removing them.