---
name: fastml
category: formatting
description: "FastML is a bioinformatics tool for the reconstruction of ancestral sequences based on the phylogenetic relations between homologous sequences"
tags: [fastml, formatting, ancestral-sequences, phylogenetics, bioinformatics]
author: oxo-call-community
source_url: "http://fastml.tau.ac.il/"
---

## Concepts

- **Tool Overview**: FastML is a tool for reconstructing ancestral sequences based on phylogenetic relationships between homologous sequences.
- **Core Function**: Infers ancestral sequences using maximum likelihood or parsimony methods.
- **Input/Output**: Input: Aligned sequences, phylogenetic tree. Output: Ancestral sequences, posterior probabilities.
- **Algorithm**: Uses maximum likelihood or Bayesian methods for ancestral sequence reconstruction.
- **Key Features**: Ancestral sequence reconstruction, maximum likelihood, parsimony, posterior probabilities, visualization.
- **Installation**: `conda install -c bioconda fastml`

## Pitfalls

- **Alignment Quality**: Requires high-quality sequence alignment.
- **Tree Quality**: Results depend on input tree quality.
- **Memory Usage**: Large datasets may require significant memory.
- **Computation Time**: Complex analyses may require substantial processing time.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic ancestral reconstruction
**Args:** `fastml -i alignment.fasta -t tree.newick -o ancestral.fasta`
**Explanation:** Reconstructs ancestral sequences.

### With maximum likelihood
**Args:** `fastml -i alignment.fasta -t tree.newick -o ancestral.fasta -m ML`
**Explanation:** Uses maximum likelihood method.

### With parsimony
**Args:** `fastml -i alignment.fasta -t tree.newick -o ancestral.fasta -m MP`
**Explanation:** Uses maximum parsimony method.

### Output posterior probabilities
**Args:** `fastml -i alignment.fasta -t tree.newick -o ancestral.fasta -p`
**Explanation:** Outputs posterior probabilities.

### Visualization
**Args:** `fastml -i alignment.fasta -t tree.newick -o ancestral.fasta --visualize tree.png`
**Explanation:** Generates visualization of results.