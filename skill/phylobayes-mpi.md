---
name: phylobayes-mpi
category: population-genomics
description: phylobayes-mpi performs Bayesian phylogenetic reconstruction.
tags: [phylobayes-mpi, population-genomics, bayesian, phylogeny]
author: oxo-call-community
source_url: "https://github.com/bayesiancook/pbmpi"
---

## Concepts

- **Tool Overview**: phylobayes-mpi reconstructs phylogenies.
- **Core Function**: Bayesian phylogenetic reconstruction.
- **Algorithm**: Uses mixture model methods.
- **Input Format**: Accepts sequence alignment files.
- **Output**: Produces phylogenetic tree results.
- **Use Case**: Phylogenetics, Bayesian analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Alignment Quality**: Results depend on alignment quality.
- **Bayesian Inference**: May have inference errors.
- **Runtime**: Reconstruction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylobayes-mpi --help`
**Explanation:** Shows available options and usage instructions.

### Reconstruct phylogeny
**Args:** `phylobayes-mpi -i alignment.fasta -o phylogeny_tree.txt`
**Explanation:** Reconstructs phylogenetic tree.

### With parameters
**Args:** `phylobayes-mpi -i alignment.fasta -p params.yaml -o phylogeny_tree.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phylobayes-mpi -v -i alignment.fasta -o phylogeny_tree.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylobayes-mpi -t 4 -i alignment.fasta -o phylogeny_tree.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylobayes-mpi -i alignment.fasta -o phylogeny_tree.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `phylobayes-mpi -i alignment.fasta -o phylogeny_tree.txt --report report.html`
**Explanation:** Generates HTML report.