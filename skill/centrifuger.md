---
name: centrifuger
category: metagenomics
description: Lossless compression of microbial genomes for efficient metagenomic sequence classification
tags: [centrifuger, centrifuge, metagenomics, compression, sequence-classification]
author: oxo-call-community
source_url: "https://github.com/mourisl/centrifuger"
---

## Concepts

- **Tool Overview**: Centrifuger provides lossless compression of microbial genomes for efficient metagenomic sequence classification.
- **Core Function**: Compresses reference genomes to reduce memory usage while maintaining classification accuracy.
- **Algorithm**: Uses lossless compression techniques optimized for genomic sequences.
- **Input**: Microbial genome sequences in FASTA format.
- **Output**: Compressed genome index for rapid sequence classification.
- **Application**: Memory-efficient metagenomic classification.
- **Installation**: Install via bioconda: `conda install -c bioconda centrifuger`

## Pitfalls

- **Compression Time**: Initial compression may take time for large databases.
- **Index Size**: Compressed indexes still require storage space.
- **Compatibility**: Ensure compatibility with Centrifuge classification.
- **Database Updates**: May need re-compression when updating reference databases.

## Examples

### Build compressed index
**Args:** `centrifuger-build -p 8 genomes.fasta compressed_index`
**Explanation:** Builds compressed Centrifuge index from reference genomes.

### Classify with compressed index
**Args:** `centrifuger -x compressed_index -1 reads_1.fq -2 reads_2.fq -o results.tsv`
**Explanation:** Classifies reads using compressed index for memory efficiency.

### Compress existing index
**Args:** `centrifuger-compress -i existing_index -o compressed_index`
**Explanation:** Compresses existing Centrifuge index.

### Display help
**Args:** `centrifuger --help`
**Explanation:** Shows all available options and usage information.