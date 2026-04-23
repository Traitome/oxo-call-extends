---
name: calib
category: assembly
description: Clustering without alignment using LSH and MinHashing of barcoded reads
tags: [calib, clustering, barcode, minhash, lsh]
author: oxo-call-community
source_url: "https://github.com/vpc-ccg/calib"
---

## Concepts

- **Tool Overview**: CALIB clusters reads without alignment using locality-sensitive hashing.
- **Core Function**: Groups similar barcoded reads using MinHash signatures.
- **Algorithm**: LSH and MinHash for alignment-free clustering.
- **Input**: Barcoded FASTQ files.
- **Output**: Clustered reads in FASTQ format.
- **Application**: Read clustering for metagenomics and single-cell analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda calib`

## Pitfalls

- **Barcoded Reads**: Requires reads with barcode information.
- **Parameter Tuning**: May need to adjust sensitivity parameters.
- **Memory Usage**: Large datasets require significant memory.

## Examples

### Cluster barcoded reads
**Args:** `calib -i reads.fq -o clustered.fq`
**Explanation:** Clusters reads using barcode similarity without alignment.

### Set sensitivity
**Args:** `calib -i reads.fq -s 0.9 -o clustered.fq`
**Explanation:** Uses 90% similarity threshold for clustering.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
