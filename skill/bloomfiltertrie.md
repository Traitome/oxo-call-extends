---
name: bloomfiltertrie
category: formatting
description: Alignment-free reference-free data structure for colored de Bruijn graph with pan-genome indexing
tags: [bloomfiltertrie, pangenome, debruijn, indexing, kmer]
author: oxo-call-community
source_url: "https://github.com/GuillaumeHolley/BloomFilterTrie"
---

## Concepts

- **Tool Overview**: BloomFilterTrie is a data structure for colored de Bruijn graphs for pan-genome indexing.
- **Core Function**: Indexes and queries pan-genome data using Bloom filter-based tries.
- **Features**: Alignment-free, reference-free, and incremental construction.
- **Input**: Collection of FASTA genomes.
- **Output**: Indexed pan-genome structure for efficient querying.
- **Installation**: Install via bioconda: `conda install -c bioconda bloomfiltertrie`

## Pitfalls

- **Memory Usage**: Large pan-genomes require significant memory for indexing.
- **K-mer Size**: Choose appropriate k-mer size for species complexity.
- **False Positives**: Bloom filters have inherent false positive rate.
- **Incremental Build**: Adding genomes incrementally may affect index quality.

## Examples

### Build pan-genome index
**Args:** `bloomfiltertrie build -i genomes_list.txt -o pangenome.idx`
**Explanation:** Builds pan-genome index from list of genome FASTA files.

### Query pan-genome
**Args:** `bloomfiltertrie query -i pangenome.idx -q query.fa -o results.tsv`
**Explanation:** Queries pan-genome index for k-mer presence.

### Set k-mer size
**Args:** `bloomfiltertrie build -i genomes.txt -k 31 -o pangenome.idx`
**Explanation:** Uses 31-mer for pan-genome index construction.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
