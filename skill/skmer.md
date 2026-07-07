---
name: skmer
category: alignment
description: Assembly-free and alignment-free tool for estimating genomic distances between genome-skims
tags: [skmer, alignment, genome-distance, assembly-free]
author: oxo-call-community
source_url: "https://github.com/shahab-sarmashghi/Skmer"
---

## Concepts

- **Tool Overview**: skmer (v3.3.0) - An alignment-free tool for computing genomic distances from low-coverage genome skims
- **Core Function**: Estimates genomic distances using k-mer frequencies without requiring assembly or alignment
- **Input/Output**: Accepts FASTA/FASTQ files; outputs distance matrices and closest reference matches
- **Algorithm**: Combines k-mer counting with statistical methods to estimate Jaccard similarity
- **Installation**: `conda install -c bioconda skmer`
- **Key Features**: Designed for low-coverage data; provides accurate species identification

## Pitfalls

- **Coverage Dependence**: Performance degrades with very low coverage (<0.1x)
- **k-mer Selection**: Default k-mer size may not be optimal for all datasets
- **Reference Database**: Requires properly formatted reference database
- **Memory Usage**: Large reference databases require significant memory
- **Taxonomic Resolution**: Limited by reference database completeness
- **Computation Time**: Large datasets may require substantial computation time

## Examples

### Display help
**Args:** `skmer --help`
**Explanation:** Shows available options and usage information.

### Build reference database
**Args:** `skmer build -d reference_genomes/ -o skmer_db`
**Explanation:** Build a skmer reference database from a directory of genome sequences.

### Query against database
**Args:** `skmer query -d skmer_db -i query.fastq -o results.txt`
**Explanation:** Query a genome skim against the reference database.

### Compute pairwise distance
**Args:** `skmer distance -a genome1.fasta -b genome2.fasta`
**Explanation:** Compute genomic distance between two genomes.

### Batch query
**Args:** `skmer batch -d skmer_db -i queries/ -o batch_results/`
**Explanation:** Process multiple query samples in batch mode.

### With custom k-mer size
**Args:** `skmer query -k 21 -d skmer_db -i query.fastq -o results.txt`
**Explanation:** Use k-mer size of 21 for distance calculation.

### Generate phylogenetic tree
**Args:** `skmer tree -d skmer_db -i samples/ -o tree.nwk`
**Explanation:** Generate a phylogenetic tree from distance matrix.