---
name: starcode
category: sequence-analysis
description: "Starcode: sequence clustering based on all-pairs search."
tags: [starcode, sequence-clustering, deduplication, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/gui11aume/starcode"
---
## Concepts

- **Tool Overview**: starcode (v1.4) is a fast sequence clustering tool that groups similar sequences based on edit distance.
- **Core Function**: Identifies clusters of nearly identical sequences for deduplication and error correction.
- **Algorithm**: Uses all-pairs search with efficient indexing to find sequences within specified edit distance.
- **Input/Output**: Input: FASTA/FASTQ sequences; Output: Clustered sequences with representative consensus.
- **Applications**: UMI deduplication, error correction, and sequence clustering in high-throughput sequencing.
- **Installation**: `conda install -c bioconda starcode` or compile from source.

## Pitfalls

- **Edit Distance**: Incorrect edit distance threshold affects clustering accuracy.
- **Memory Requirements**: Large datasets require significant memory for all-pairs comparison.
- **Computational Time**: All-pairs search is O(n²), which can be slow for very large datasets.
- **Sequence Length**: Optimal performance with sequences of similar lengths.
- **Duplicate Detection**: May miss duplicates with high edit distances.
- **Consensus Accuracy**: Poor quality sequences affect consensus sequence accuracy.

## Examples

### Display help
**Args:** `starcode --help`
**Explanation:** Shows available options and usage information.

### Basic clustering
**Args:** `starcode -i sequences.fasta -o clusters.txt`
**Explanation:** Cluster sequences with default settings.

### With edit distance
**Args:** `starcode -i sequences.fasta -o clusters.txt -d 2`
**Explanation:** Allow maximum edit distance of 2 between cluster members.

### UMI deduplication
**Args:** `starcode -i umis.fastq -o deduplicated.txt --umi`
**Explanation:** Deduplicate UMI sequences with error correction.

### Output consensus
**Args:** `starcode -i sequences.fasta -o clusters.txt --consensus`
**Explanation:** Output consensus sequence for each cluster.

### Count occurrences
**Args:** `starcode -i sequences.fasta -o clusters.txt --count`
**Explanation:** Include occurrence count for each cluster.

### Batch mode
**Args:** `starcode -i batch/ -o clusters/`
**Explanation:** Process multiple files in batch mode.

### Verbose mode
**Args:** `starcode -i sequences.fasta -o clusters.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Memory optimization
**Args:** `starcode -i sequences.fasta -o clusters.txt --low-memory`
**Explanation:** Use memory-efficient mode for large datasets.
