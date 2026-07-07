---
name: phylip
category: population-genomics
description: phylip provides programs for inferring phylogenies.
tags: [phylip, population-genomics, phylogeny, inference]
author: oxo-call-community
source_url: "http://evolution.genetics.washington.edu/phylip/"
---

## Concepts

- **Tool Overview**: phylip infers phylogenetic trees.
- **Core Function**: Phylogeny inference package.
- **Algorithm**: Uses phylogenetic inference methods.
- **Input Format**: Accepts sequence alignment files.
- **Output**: Produces phylogenetic tree results.
- **Use Case**: Phylogenetics, tree inference.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Alignment Quality**: Results depend on alignment quality.
- **Inference Method**: Requires proper method selection.
- **Runtime**: Inference may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylip --help`
**Explanation:** Shows available options and usage instructions.

### Infer phylogeny
**Args:** `phylip -i alignment.fasta -o phylogeny_tree.txt`
**Explanation:** Infers phylogenetic tree.

### With parameters
**Args:** `phylip -i alignment.fasta -p params.yaml -o phylogeny_tree.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phylip -v -i alignment.fasta -o phylogeny_tree.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylip -t 4 -i alignment.fasta -o phylogeny_tree.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylip -i alignment.fasta -o phylogeny_tree.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `phylip -i alignment.fasta -o phylogeny_tree.txt --report report.html`
**Explanation:** Generates HTML report.