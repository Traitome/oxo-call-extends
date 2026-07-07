---
name: phyml
category: population-genomics
description: phyml estimates maximum likelihood phylogenies.
tags: [phyml, population-genomics, maximum-likelihood, phylogeny]
author: oxo-call-community
source_url: "http://www.atgc-montpellier.fr/phyml/"
---

## Concepts

- **Tool Overview**: phyml estimates phylogenetic trees.
- **Core Function**: Maximum likelihood phylogenetic estimation.
- **Algorithm**: Uses maximum likelihood methods.
- **Input Format**: Accepts sequence alignment files.
- **Output**: Produces phylogenetic tree results.
- **Use Case**: Phylogenetics, maximum likelihood analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large alignments require memory.
- **Alignment Quality**: Results depend on alignment quality.
- **ML Estimation**: May have estimation errors.
- **Runtime**: Estimation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phyml --help`
**Explanation:** Shows available options and usage instructions.

### Estimate phylogeny
**Args:** `phyml -i alignment.fasta -o phylogeny_tree.txt`
**Explanation:** Estimates maximum likelihood phylogeny.

### With parameters
**Args:** `phyml -i alignment.fasta -p params.yaml -o phylogeny_tree.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phyml -v -i alignment.fasta -o phylogeny_tree.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phyml -t 4 -i alignment.fasta -o phylogeny_tree.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phyml -i alignment.fasta -o phylogeny_tree.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `phyml -i alignment.fasta -o phylogeny_tree.txt --report report.html`
**Explanation:** Generates HTML report.