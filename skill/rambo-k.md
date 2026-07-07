---
name: rambo-k
category: programming
description: RAMBO-K is a reference-based tool for rapid and sensitive extraction of one organism's reads from a mixed NGS dataset.
tags: [rambo-k, programming, read-extraction, metagenomics]
author: oxo-call-community
source_url: "https://gitlab.com/SimonHTausch/RAMBO-K"
---

## Concepts

- **Tool Overview**: rambo-k extracts reads.
- **Core Function**: Read extraction.
- **Algorithm**: Uses k-mer matching.
- **Input Format**: Accepts NGS reads.
- **Output**: Produces extracted reads.
- **Use Case**: Metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Quality**: Affects extraction.
- **Parameters**: Must be configured.
- **Runtime**: Extraction may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rambo-k --help`
**Explanation:** Shows available options and usage instructions.

### Extract reads
**Args:** `rambo-k extract -i mixed_reads.fastq -r reference.fasta -o extracted.fastq`
**Explanation:** Extracts organism-specific reads.

### With parameters
**Args:** `rambo-k extract -i mixed_reads.fastq -p params.yaml -o extracted.fastq`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rambo-k -v extract -i mixed_reads.fastq -o extracted.fastq`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rambo-k -t 4 extract -i mixed_reads.fastq -o extracted.fastq`
**Explanation:** Uses 4 threads for parallel processing.

### With k-mer size
**Args:** `rambo-k extract -i mixed_reads.fastq -k 31 -o extracted.fastq`
**Explanation:** Uses specific k-mer size.

### Generate report
**Args:** `rambo-k extract -i mixed_reads.fastq -o extracted.fastq --report report.html`
**Explanation:** Generates HTML report.