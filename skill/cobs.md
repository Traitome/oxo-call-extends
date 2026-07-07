---
name: cobs
category: utility
description: Compact Bit-Sliced Signature Index for genomic k-mer data
tags: [cobs, k-mer-indexing, sequence-search, bioinformatics, indexing]
author: oxo-call-community
source_url: "https://panthema.net/cobs"
---

## Concepts

- **Tool Overview**: COBS (Compact Bit-Sliced Signature Index) is a tool for building compact index structures for fast similarity search on genomic k-mer data.
- **Core Function**: Creates compact indexes for k-mer or q-gram data, enabling fast similarity searches.
- **Algorithm**: Uses bit-sliced signatures to create compact, efficient indexes for sequence similarity search.
- **Input**: FASTA or FASTQ sequence files.
- **Output**: Compact index files and search results.
- **Application**: Sequence similarity search, metagenomics, and genomic data indexing.
- **Installation**: Install via bioconda: `conda install -c bioconda cobs`

## Pitfalls

- **Memory Usage**: Index construction may require significant memory.
- **k-mer Selection**: k-mer size affects index size and search sensitivity.
- **Index Size**: Larger datasets produce larger indexes.
- **Search Speed**: Performance depends on index size and query complexity.
- **Disk Space**: Index files can be large for big datasets.

## Examples

### Build index from sequences
**Args:** `cobs build -i sequences.fasta -o index.cobs`
**Explanation:** Builds COBS index from FASTA sequences.

### Search index
**Args:** `cobs search -i index.cobs -q query.fasta -o results.txt`
**Explanation:** Searches COBS index with query sequences.

### Build with k-mer size
**Args:** `cobs build -k 25 -i sequences.fasta -o index.cobs`
**Explanation:** Builds index using 25-mers.

### Display help
**Args:** `cobs --help`
**Explanation:** Shows all available options and usage information.