---
name: phylodm
category: population-genomics
description: phylodm calculates phylogenetic distance matrices efficiently.
tags: [phylodm, population-genomics, distance, matrix]
author: oxo-call-community
source_url: "https://github.com/aaronmussig/PhyloDM"
---

## Concepts

- **Tool Overview**: phylodm calculates distance matrices.
- **Core Function**: Phylogenetic distance calculation.
- **Algorithm**: Uses efficient matrix computation methods.
- **Input Format**: Accepts phylogenetic tree files.
- **Output**: Produces distance matrix results.
- **Use Case**: Phylogenetics, distance analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Tree Quality**: Results depend on tree quality.
- **Distance Calculation**: May have calculation errors.
- **Runtime**: Calculation may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phylodm --help`
**Explanation:** Shows available options and usage instructions.

### Calculate distances
**Args:** `phylodm -i phylogeny_tree.newick -o distance_matrix.txt`
**Explanation:** Calculates phylogenetic distances.

### With parameters
**Args:** `phylodm -i phylogeny_tree.newick -p params.yaml -o distance_matrix.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phylodm -v -i phylogeny_tree.newick -o distance_matrix.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phylodm -t 4 -i phylogeny_tree.newick -o distance_matrix.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phylodm -i phylogeny_tree.newick -o distance_matrix.tsv --tsv`
**Explanation:** Outputs in TSV format.

### Generate report
**Args:** `phylodm -i phylogeny_tree.newick -o distance_matrix.txt --report report.html`
**Explanation:** Generates HTML report.