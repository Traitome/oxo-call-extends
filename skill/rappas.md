---
name: rappas
category: alignment
description: RAPPAS (Rapid Alignment-free Phylogenetic Placement via Ancestral Sequences) performs phylogenetic placement of metagenomic reads on reference trees using phylo-kmers without alignment.
tags: [rappas, alignment, phylogenetics, phylo-kmers]
author: oxo-call-community
source_url: "https://github.com/blinard-BIOINFO/RAPPAS"
---

## Concepts

- **Tool Overview**: rappas places reads.
- **Core Function**: Phylogenetic placement.
- **Algorithm**: Uses phylo-kmers.
- **Input Format**: Accepts metagenomic reads.
- **Output**: Produces placement results.
- **Use Case**: Metagenomics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Tree Quality**: Affects placement.
- **Parameters**: Must be configured.
- **Runtime**: Placement may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `rappas --help`
**Explanation:** Shows available options and usage instructions.

### Build database
**Args:** `rappas build -i tree.newick -a alignment.fasta -o database/`
**Explanation:** Builds phylo-kmer database.

### Place reads
**Args:** `rappas place -i reads.fasta -d database/ -o placements.jplace`
**Explanation:** Places reads on tree.

### With parameters
**Args:** `rappas place -i reads.fasta -p params.yaml -o placements.jplace`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `rappas -v place -i reads.fasta -o placements.jplace`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `rappas -t 4 place -i reads.fasta -o placements.jplace`
**Explanation:** Uses 4 threads for parallel processing.

### Generate report
**Args:** `rappas place -i reads.fasta -o placements.jplace --report report.html`
**Explanation:** Generates HTML report.