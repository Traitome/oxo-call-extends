---
name: panacota
category: alignment
description: PanACoTA provides tools for large-scale comparative genomics and pangenome analysis.
tags: [panacota, alignment, pangenome, comparative-genomics]
author: oxo-call-community
source_url: "https://github.com/gem-pasteur/PanACoTA"
---

## Concepts

- **Tool Overview**: PanACoTA performs pangenome and comparative genomic analysis.
- **Core Function**: Analyzes multiple genomes for pangenome construction.
- **Algorithm**: Uses homology detection and alignment methods.
- **Input Format**: Accepts genome sequences in FASTA format.
- **Output**: Produces pangenome statistics and phylogenetic trees.
- **Use Case**: Comparative genomics, pangenomics, and evolutionary analysis.

## Pitfalls

- **Version Differences**: Options may vary between versions.
- **Memory Usage**: Large datasets require memory.
- **Computational Cost**: Analysis can be computationally intensive.
- **Genome Quality**: Results depend on input genome quality.
- **Runtime**: Analysis may take significant time.
- **Validation**: Results should be validated for correctness.

## Examples

### Display help
**Args:** `PanACoTA --help`
**Explanation:** Shows available options and usage instructions.

### Run pangenome analysis
**Args:** `PanACoTA pangenome -i genomes/ -o results/`
**Explanation:** Performs pangenome analysis.

### Annotate genomes
**Args:** `PanACoTA annotate -i genomes/ -o annotations/`
**Explanation:** Annotates genome sequences.

### Align core genome
**Args:** `PanACoTA align -i core_genes/ -o alignments/`
**Explanation:** Aligns core genome genes.

### Build phylogeny
**Args:** `PanACoTA tree -i alignments/ -o tree.nwk`
**Explanation:** Infers phylogenetic tree.

### Verbose mode
**Args:** `PanACoTA pangenome -v -i genomes/ -o results/`
**Explanation:** Runs with verbose output.

### Number of threads
**Args:** `PanACoTA pangenome -t 16 -i genomes/ -o results/`
**Explanation:** Uses 16 threads for parallel processing.