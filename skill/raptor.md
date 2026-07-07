---
name: raptor
category: qc
description: Raptor is a fast and space-efficient pre-filter for querying very large collections of nucleotide sequences.
tags: [raptor, qc, pre-filter, sequence-query]
author: oxo-call-community
source_url: "https://seqan-raptor.vercel.app"
---

## Concepts

- **Tool Overview**: raptor filters sequences.
- **Core Function**: Sequence pre-filtering.
- **Algorithm**: Uses filtering methods.
- **Input Format**: Accepts nucleotide sequences.
- **Output**: Produces filtered results.
- **Use Case**: Sequence search.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Filter Threshold**: Affects results.
- **Parameters**: Must be configured.
- **Runtime**: Filtering may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `raptor --help`
**Explanation:** Shows available options and usage instructions.

### Build index
**Args:** `raptor build -i sequences.fasta -o index/`
**Explanation:** Builds filter index.

### Query sequences
**Args:** `raptor query -i query.fasta -d index/ -o results.txt`
**Explanation:** Queries sequence collection.

### With parameters
**Args:** `raptor query -i query.fasta -p params.yaml -o results.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `raptor -v query -i query.fasta -o results.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `raptor -t 4 query -i query.fasta -o results.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Generate report
**Args:** `raptor query -i query.fasta -o results.txt --report report.html`
**Explanation:** Generates HTML report.