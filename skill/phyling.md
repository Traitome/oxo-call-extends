---
name: phyling
category: population-genomics
description: phyling infers phylogenies from protein-coding genomic sequences.
tags: [phyling, population-genomics, phylogeny, orthologs]
author: oxo-call-community
source_url: "https://github.com/stajichlab/Phyling"
---

## Concepts

- **Tool Overview**: phyling infers species phylogenies.
- **Core Function**: Phylogenetic inference from proteins.
- **Algorithm**: Uses ortholog identification methods.
- **Input Format**: Accepts protein sequence files.
- **Output**: Produces species phylogeny trees.
- **Use Case**: Phylogenetics, ortholog analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Protein Quality**: Results depend on protein quality.
- **Ortholog Detection**: May have detection errors.
- **Runtime**: Inference may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `phyling --help`
**Explanation:** Shows available options and usage instructions.

### Infer phylogeny
**Args:** `phyling -i protein_sequences.fasta -o phylogeny_tree.txt`
**Explanation:** Infers species phylogeny.

### With parameters
**Args:** `phyling -i protein_sequences.fasta -p params.yaml -o phylogeny_tree.txt`
**Explanation:** Uses parameter configuration.

### Verbose mode
**Args:** `phyling -v -i protein_sequences.fasta -o phylogeny_tree.txt`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `phyling -t 4 -i protein_sequences.fasta -o phylogeny_tree.txt`
**Explanation:** Uses 4 threads for parallel processing.

### Output format
**Args:** `phyling -i protein_sequences.fasta -o phylogeny_tree.newick --newick`
**Explanation:** Outputs in Newick format.

### Generate report
**Args:** `phyling -i protein_sequences.fasta -o phylogeny_tree.txt --report report.html`
**Explanation:** Generates HTML report.