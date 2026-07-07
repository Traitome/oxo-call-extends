---
name: decodiphy
category: programming
description: DecoDiPhy - consolidating millions of sequence reads into accurate phylogenetic placements.
tags: [decodiphy, programming, phylogenetics, sequence-placement, metagenomics]
author: oxo-call-community
source_url: "https://github.com/shayesteh99/DecoDiPhy"
---

## Concepts

- **Tool Overview**: decodiphy (v1.2.3+) is a Python tool for efficiently consolidating millions of sequence reads into a few accurate phylogenetic placements. It is particularly useful for metagenomic and environmental sequencing data.
- **Core Function**: Reduces computational complexity by grouping similar reads and placing representative sequences on a reference phylogenetic tree.
- **Input/Output**: Input: Sequence reads (FASTA/FASTQ), reference phylogenetic tree. Output: Consolidated placements, abundance estimates, tree with placements.
- **Algorithm**: Uses sequence clustering to reduce read count, then performs phylogenetic placement on representative sequences using evolutionary placement algorithms.
- **Key Features**: Scalable to millions of reads, reduces computational burden, maintains placement accuracy, supports diverse sequencing data types.
- **Installation**: `conda install -c bioconda decodiphy`

## Pitfalls

- **Reference Tree Quality**: Results depend on reference tree quality.
- **Clustering Threshold**: Clustering parameters affect placement accuracy.
- **Sequence Diversity**: Highly diverse datasets may require different parameters.
- **Memory Usage**: May require significant memory for very large datasets.
- **Phylogenetic Signal**: Requires sufficient phylogenetic signal in data.

## Examples

### Place reads on reference tree
**Args:** `decodiphy -i reads.fasta -t reference_tree.nwk -o placements.txt`
**Explanation:** Place sequence reads onto reference phylogenetic tree.

### Consolidate and place
**Args:** `decodiphy -i reads.fasta -t reference_tree.nwk --cluster -o placements.txt`
**Explanation:** Cluster similar reads before placement for efficiency.

### Specify clustering threshold
**Args:** `decodiphy -i reads.fasta -t reference_tree.nwk --identity 0.99 -o placements.txt`
**Explanation:** Use 99% identity threshold for read clustering.