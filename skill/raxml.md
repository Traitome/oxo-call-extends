---
name: raxml
category: utility
description: RAxML (Randomized Axelerated Maximum Likelihood) performs maximum likelihood phylogenetic tree inference.
tags: [raxml, utility, phylogenetics, maximum-likelihood]
author: oxo-call-community
source_url: "http://sco.h-its.org/exelixis/web/software/raxml/index.html"
---

## Concepts

- **Tool Overview**: raxml builds trees.
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
**Args:** `raxml --help`
**Explanation:** Shows available options and usage instructions.

### Build tree
**Args:** `raxml build -i alignment.fasta -m GTRGAMMA -o tree.newick`
**Explanation:** Builds phylogenetic tree.

### With parameters
**Args:** `raxml build -i alignment.fasta -p params.yaml -o tree.newick`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `raxml -v build -i alignment.fasta -o tree.newick`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `raxml -t 4 build -i alignment.fasta -o tree.newick`
**Explanation:** Uses 4 threads for parallel processing.

### With bootstrapping
**Args:** `raxml build -i alignment.fasta -b 100 -o tree.newick`
**Explanation:** Uses 100 bootstrap replicates.

### Generate report
**Args:** `raxml build -i alignment.fasta -o tree.newick --report report.html`
**Explanation:** Generates HTML report.