---
name: plant_tribes_gene_family_phylogeny_builder
category: population-genomics
description: plant_tribes_gene_family_phylogeny_builder builds gene family phylogenies.
tags: [plant_tribes_gene_family_phylogeny_builder, population-genomics, phylogeny, gene-family]
author: oxo-call-community
source_url: "https://github.com/dePamphilis/PlantTribes"
---

## Concepts

- **Tool Overview**: plant_tribes_gene_family_phylogeny_builder builds phylogenies.
- **Core Function**: Gene family phylogeny construction.
- **Algorithm**: Uses phylogenetic inference methods.
- **Input Format**: Accepts aligned sequence files.
- **Output**: Produces phylogenetic trees.
- **Use Case**: Plant phylogenomics, evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Alignment Quality**: Results depend on alignment quality.
- **Tree Accuracy**: May have topology errors.
- **Runtime**: Inference may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `plant_tribes_gene_family_phylogeny_builder --help`
**Explanation:** Shows available options and usage instructions.

### Build phylogeny
**Args:** `plant_tribes_gene_family_phylogeny_builder -i alignment.fasta -o tree.nwk`
**Explanation:** Builds gene family phylogenetic tree.

### With parameters
**Args:** `plant_tribes_gene_family_phylogeny_builder -i alignment.fasta -p params.yaml -o tree.nwk`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `plant_tribes_gene_family_phylogeny_builder -v -i alignment.fasta -o tree.nwk`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `plant_tribes_gene_family_phylogeny_builder -t 4 -i alignment.fasta -o tree.nwk`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `plant_tribes_gene_family_phylogeny_builder -i alignment.fasta -o tree.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `plant_tribes_gene_family_phylogeny_builder -i alignment.fasta -o tree.nwk --report report.html`
**Explanation:** Generates HTML report.