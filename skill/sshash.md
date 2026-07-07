---
name: sshash
category: sequence-analysis
description: SSHash is a compressed dictionary data structure for k-mers based on Sparse and Skew Hashing.
tags: [sshash, k-mer, compressed-data-structure, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/jermp/sshash"
---

## Concepts

- **Tool Overview**: sshash (v5.1.0) is a compressed k-mer dictionary data structure optimized for bioinformatics applications.
- **Core Function**: Efficient storage and querying of k-mer sets with minimal memory footprint.
- **Algorithm**: Based on Sparse and Skew Hashing techniques for compressed representation.
- **Input/Output**: Input: FASTA/Q files or k-mer lists; Output: Compressed index file and query results.
- **Applications**: Genome indexing, sequence alignment, metagenomics classification, and variant calling.
- **Installation**: `conda install -c bioconda sshash` or compile from source.

## Pitfalls

- **k-mer Size**: Optimal k-mer size depends on application; too small increases false positives, too large reduces sensitivity.
- **Memory Usage**: Building large indexes requires sufficient memory; consider chunking for very large datasets.
- **False Positives**: Hash collisions can produce false positive k-mer matches.
- **Index Time**: Building indexes for large genomes can be time-consuming.
- **Query Performance**: Performance degrades with increasing k-mer size.
- **Compression Level**: Higher compression may reduce query speed.

## Examples

### Display help
**Args:** `sshash --help`
**Explanation:** Shows available options and usage information.

### Build k-mer index
**Args:** `sshash build -i genome.fasta -o genome.sshash -k 21`
**Explanation:** Build SSHash index for genome with k-mer size 21.

### Query k-mers
**Args:** `sshash query -i genome.sshash -q kmers.txt`
**Explanation:** Query k-mer presence in the index.

### Count k-mers
**Args:** `sshash count -i reads.fastq -k 31`
**Explanation:** Count k-mers in sequencing reads.

### Build with abundance
**Args:** `sshash build -i reads.fastq -o reads.sshash -k 27 --abundance`
**Explanation:** Build index with k-mer abundance information.

### Bulk query
**Args:** `sshash query -i index.sshash -q queries.fastq --bulk`
**Explanation:** Perform bulk k-mer queries from FASTQ file.

### Export k-mers
**Args:** `sshash export -i index.sshash -o kmers.txt`
**Explanation:** Export all k-mers from the index to text file.
