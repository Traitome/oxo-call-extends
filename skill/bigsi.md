---
name: bigsi
category: alignment
description: BIGSI - BItsliced Genomic Signature Index for fast sequence search
tags: [sequence-search, indexing, k-mer, bloom-filter]
author: oxo-call-community
source_url: "https://github.com/Phelimb/BIGSI"
---

## Concepts
- **Tool Overview**: BIGSI (Bitsliced Genomic Signature Index) is a method for indexing large collections of genomes for fast sequence search. It uses Bloom filters and bitslicing to enable rapid k-mer queries across thousands of genomes.
- **Indexing Strategy**: Converts each genome into a Bloom filter of k-mers, then bitslices the Bloom filters for efficient intersection queries.
- **Performance**: Can search across 450,000 bacterial genomes in milliseconds.
- **Use Cases**: Finding which genomes contain specific sequences, AMR gene detection, outbreak tracking.

## Pitfalls
- **K-mer Size**: Choice of k-mer size affects sensitivity and specificity.
- **False Positives**: Bloom filters have inherent false positive rate; results may need validation.
- **Memory**: Building indexes for large collections requires substantial memory.

## Examples
### Build BIGSI index
**Args:** `bigsi build --sample-dir genomes/ --k 31 --output index.bigsi`
**Explanation:** Builds a BIGSI index from a directory of genome files.

### Query sequence
**Args:** `bigsi search --index index.bigsi --seq AMR_gene.fa`
**Explanation:** Searches for a sequence across all indexed genomes.
