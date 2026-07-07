---
name: paragone
category: utility
description: ParaGone identifies ortholog groups from paralog sequences across taxa.
tags: [paragone, utility, orthologs, paralogs]
author: oxo-call-community
source_url: "https://github.com/chrisjackson-pellicle/ParaGone"
---

## Concepts

- **Tool Overview**: ParaGone identifies ortholog groups from paralog sequences.
- **Core Function**: Classifies orthologs from multi-species paralog data.
- **Algorithm**: Uses phylogenetic and sequence similarity approaches.
- **Input Format**: Accepts FASTA sequences from multiple taxa.
- **Output**: Produces ortholog group assignments.
- **Use Case**: Comparative genomics, gene family analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequence Quality**: Results depend on input sequence quality.
- **Taxon Sampling**: Requires adequate taxon representation.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `paragone --help`
**Explanation:** Shows available options and usage instructions.

### Run analysis
**Args:** `paragone -i sequences.fasta -o orthologs/`
**Explanation:** Identifies ortholog groups.

### With species mapping
**Args:** `paragone -i sequences.fasta -s species.txt -o orthologs/`
**Explanation:** Uses species mapping file.

### Verbose mode
**Args:** `paragone -v -i sequences.fasta -o orthologs/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `paragone -t 8 -i sequences.fasta -o orthologs/`
**Explanation:** Uses 8 threads for parallel processing.

### Output format
**Args:** `paragone -i sequences.fasta -o orthologs.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Minimum support
**Args:** `paragone -m 3 -i sequences.fasta -o orthologs/`
**Explanation:** Requires minimum 3 taxa per ortholog group.