---
name: phyclone
category: population-genomics
description: phyclone reconstructs cancer phylogenies from bulk sequencing.
tags: [phyclone, population-genomics, cancer, phylogeny]
author: oxo-call-community
source_url: "https://github.com/Roth-Lab/PhyClone"
---

## Concepts

- **Tool Overview**: phyclone reconstructs cancer phylogenies.
- **Core Function**: Bayesian phylogeny reconstruction.
- **Algorithm**: Uses Bayesian inference methods.
- **Input Format**: Accepts bulk sequencing data.
- **Output**: Produces cancer phylogeny trees.
- **Use Case**: Cancer analysis, phylogeny reconstruction.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Sequencing Quality**: Results depend on sequencing quality.
- **Bayesian Inference**: May have inference errors.
- **Runtime**: Reconstruction may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phyclone --help`
**Explanation:** Shows available options and usage instructions.

### Reconstruct phylogeny
**Args:** `phyclone -i sequencing_data.txt -o phylogeny_tree.txt`
**Explanation:** Reconstructs cancer phylogeny.

### With parameters
**Args:** `phyclone -i sequencing_data.txt -p params.yaml -o phylogeny_tree.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phyclone -v -i sequencing_data.txt -o phylogeny_tree.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phyclone -t 4 -i sequencing_data.txt -o phylogeny_tree.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phyclone -i sequencing_data.txt -o phylogeny_tree.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `phyclone -i sequencing_data.txt -o phylogeny_tree.txt --report report.html`
**Explanation:** Generates HTML report.