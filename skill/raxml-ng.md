---
name: raxml-ng
category: utility
description: RAxML-NG is the next generation of RAxML, providing faster, easier-to-use and more flexible phylogenetic tree inference.
tags: [raxml-ng, utility, phylogenetics, maximum-likelihood]
author: oxo-call-community
source_url: "https://github.com/amkozlov/raxml-ng"
---

## Concepts

- **Tool Overview**: raxml-ng builds trees.
- **Core Function**: Phylogenetic inference.
- **Algorithm**: Uses maximum likelihood.
- **Input Format**: Accepts alignments.
- **Output**: Produces phylogenetic trees.
- **Use Case**: Phylogenetics.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Alignment Quality**: Affects tree building.
- **Parameters**: Must be configured.
- **Runtime**: Tree building may take time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `raxml-ng --help`
**Explanation:** Shows available options and usage instructions.

### Build tree
**Args:** `raxml-ng build -i alignment.fasta -m GTR+G -o tree.newick`
**Explanation:** Builds phylogenetic tree.

### With parameters
**Args:** `raxml-ng build -i alignment.fasta -p params.yaml -o tree.newick`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `raxml-ng -v build -i alignment.fasta -o tree.newick`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `raxml-ng -t 4 build -i alignment.fasta -o tree.newick`
**Explanation:** Uses 4 threads for parallel processing.

### With bootstrapping
**Args:** `raxml-ng build -i alignment.fasta -b 100 -o tree.newick`
**Explanation:** Uses 100 bootstrap replicates.

### Generate report
**Args:** `raxml-ng build -i alignment.fasta -o tree.newick --report report.html`
**Explanation:** Generates HTML report.