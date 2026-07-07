---
name: krakenuniq
category: metagenomics
description: Metagenomics classifier with unique k-mer counting for precise results
tags: [krakenuniq, metagenomics, taxonomic-classification, unique-kmer, k-mer]
author: oxo-call-community
source_url: "https://github.com/fbreitwieser/krakenuniq"
---

## Concepts

- **Unique K-mer Counting**: Counts unique k-mers for precise abundance estimation
- **Probabilistic Data Structures**: Uses MinHash and bloom filters
- **Taxonomic Classification**: Assigns reads to taxonomic lineages
- **Cross-contamination Detection**: Identifies potential contamination
- **Abundance Estimation**: Provides accurate abundance estimates
- **Database Support**: Works with custom and standard databases

## Pitfalls

- **Database Building**: Building database with unique counting is slower
- **Memory Usage**: Probabilistic structures reduce but don't eliminate memory needs
- **Threshold Selection**: Confidence thresholds affect results
- **Novel Taxa**: Novel organisms may not be properly classified
- **Read Quality**: Low-quality reads affect classification
- **Computational Resources**: Larger datasets need more resources

## Examples

### Classify reads
**Args:** `krakenuniq --db database --threads 8 --fastq-input reads.fastq --output results.kraken`
**Explanation:** Classifies reads with unique k-mer counting.

### Build database
**Args:** `krakenuniq-build --build --db custom_db --threads 8`
**Explanation:** Builds KrakenUniq database with unique counting.

### Generate report
**Args:** `krakenuniq --db database --fastq-input reads.fastq --report results.report`
**Explanation:** Creates detailed taxonomic report.

### Paired-end processing
**Args:** `krakenuniq --db database --paired reads_1.fastq reads_2.fastq --output results.kraken`
**Explanation:** Processes paired-end reads.

### Confidence filtering
**Args:** `krakenuniq --db database --confidence 0.2 --fastq-input reads.fastq --output results.kraken`
**Explanation:** Filters by confidence threshold.

### Estimate abundances
**Args:** `krakenuniq --db database --fastq-input reads.fastq --output results.kraken --report results.report`
**Explanation:** Generates abundance estimates per taxon.