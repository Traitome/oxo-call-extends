---
name: hulk
category: metagenomics
description: Histosketching Using Little Kmers for metagenomic similarity analysis
tags: [hulk, metagenomics, k-mer, sketching, similarity]
author: oxo-call-community
source_url: "https://github.com/will-rowe/hulk"
---

## Concepts

- **Tool Overview**: HULK (Histosketching Using Little Kmers) is a metagenomic analysis tool that creates compact k-mer spectrum sketches for rapid similarity comparisons between microbial communities.
- **Histogram Sketching**: Uses consistent weighted sampling to create fixed-size sketches that preserve k-mer frequency information, enabling efficient similarity calculations.
- **Streaming Processing**: Processes sequencing data in a streaming fashion without requiring complete data loading into memory.
- **Minimizer-based Approach**: Collects minimizers from sequences and assigns them to histogram bins using consistent jump hash for efficient storage.
- **Similarity Metrics**: Implements weighted Jaccard distance for comparing histosketches and estimating metagenomic dissimilarity.
- **Installation**: `conda install -c bioconda hulk`

## Pitfalls

- **k-mer Size Selection**: The choice of k-mer size significantly affects sketch accuracy and computational performance; typical values range from 21-31.
- **Memory Considerations**: While streaming, large sketch sizes can still consume significant memory; balance between sketch size and accuracy.
- **Data Format**: Currently supports FASTQ and FASTA formats; ensure input files are properly formatted and compressed.
- **Minimizer Sampling**: The sampling rate affects both speed and accuracy; higher sampling provides better accuracy but increases computation time.
- **Concept Drift**: The algorithm accounts for concept drift in streaming data, but rapid changes in community composition may affect results.
- **Version Compatibility**: HULK v1.0+ uses a different algorithm than earlier versions; be mindful of version-specific parameters.

## Examples

### Create a histosketch from FASTQ
**Args:** `hulk sketch -i input.fastq -o sample.hulk`
**Explanation:** Generates a histosketch from a FASTQ file and saves it to disk.

### Compare multiple samples
**Args:** `hulk smash -i sample1.hulk sample2.hulk sample3.hulk -o distance_matrix.csv`
**Explanation:** Computes pairwise distances between multiple histosketches and outputs a distance matrix.

### Stream processing with stdin
**Args:** `cat input.fastq | hulk sketch -i - -o streamed.hulk`
**Explanation:** Processes sequencing data from standard input in streaming mode.

### Generate multiple sketch types
**Args:** `hulk sketch -i input.fastq -o multi.hulk --kmv --hyperminhash`
**Explanation:** Creates a histosketch along with KMV MinHash and HyperMinHash sketches for comprehensive analysis.

### Query against reference database
**Args:** `hulk query -i query.hulk -d reference_database/ -o matches.txt`
**Explanation:** Queries a histosketch against a reference database to find similar metagenomic samples.