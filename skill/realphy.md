---
name: realphy
category: alignment
description: RealPhy is a reference sequence alignment-based phylogeny tool for evolutionary analysis.
tags: [realphy, alignment, phylogenetics, reference-based]
author: oxo-call-community
source_url: "https://realphy.unibas.ch/realphy"
---

## Concepts

- **Tool Overview**: realphy builds phylogenies.
- **Core Function**: Reference-based phylogeny.
- **Algorithm**: Uses alignment methods.
- **Input Format**: Accepts sequence files.
- **Output**: Produces phylogenetic trees.
- **Use Case**: Phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Reference Quality**: Affects phylogeny.
- **Parameters**: Must be configured.
- **Runtime**: Phylogeny building may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `realphy --help`
**Explanation:** Shows available options and usage instructions.

### Build phylogeny
**Args:** `realphy build -i sequences.fasta -r reference.fasta -o tree.newick`
**Explanation:** Builds phylogenetic tree.

### With parameters
**Args:** `realphy build -i sequences.fasta -p params.yaml -o tree.newick`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `realphy -v build -i sequences.fasta -o tree.newick`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `realphy -t 4 build -i sequences.fasta -o tree.newick`
**Explanation:** Uses 4 threads for parallel processing.

### With reference
**Args:** `realphy build -i sequences.fasta -r reference.fasta -o tree.newick`
**Explanation:** Uses reference genome.

### Generate report
**Args:** `realphy build -i sequences.fasta -o tree.newick --report report.html`
**Explanation:** Generates HTML report.