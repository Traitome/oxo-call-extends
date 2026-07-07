---
name: duphist
category: utility
description: "DupHIST: Duplication History Inference with Substitution-integrated Topology"
tags: [duphist, utility, gene-duplication, phylogenetics, evolutionary-analysis]
author: oxo-call-community
source_url: "https://github.com/minjeongjj/DupHIST"
---

## Concepts

- **Tool Overview**: DupHIST is a tool for inferring gene duplication history using substitution-integrated topology analysis.
- **Core Function**: Reconstructs the evolutionary history of gene duplications by integrating sequence substitution information with phylogenetic topology.
- **Input/Output**: Input: Gene sequences (FASTA), phylogenetic tree (Newick). Output: Duplication history, evolutionary parameters.
- **Algorithm**: Uses probabilistic models to infer duplication events and substitution rates.
- **Key Features**: Substitution-aware inference, topology integration, statistical confidence estimation, visualization.
- **Installation**: `conda install -c bioconda duphist`

## Pitfalls

- **Tree Quality**: Accurate duplication inference depends on input tree quality.
- **Sequence Alignment**: Poor alignment can affect substitution rate estimation.
- **Model Assumptions**: Evolutionary model assumptions may not fit all gene families.
- **Convergence**: MCMC chains may require long runs for convergence.
- **Paralogs vs Orthologs**: Distinguishing between paralogous and orthologous relationships is critical.

## Examples

### Basic duplication history inference
**Args:** `--sequences genes.fasta --tree tree.nwk --output history.txt`
**Explanation:** Infers duplication history from gene sequences and phylogenetic tree.

### With bootstrap support
**Args:** `--sequences genes.fasta --tree tree.nwk --output history.txt --bootstrap 100`
**Explanation:** Runs 100 bootstrap replicates for confidence estimation.

### Custom substitution model
**Args:** `--sequences genes.fasta --tree tree.nwk --output history.txt --model GTR`
**Explanation:** Uses GTR substitution model for analysis.

### Generate visualization
**Args:** `--sequences genes.fasta --tree tree.nwk --output history.txt --plot tree.png`
**Explanation:** Generates visualization of duplication history.

### Batch analysis
**Args:** `--sequence-dir genes/ --tree-dir trees/ --output results/ --batch`
**Explanation:** Processes multiple gene families in batch mode.