---
name: krakenhll
category: metagenomics
description: KrakenHLL - metagenomics classifier with HyperLogLog for unique k-mer counting
tags: [krakenhll, metagenomics, taxonomic-classification, HyperLogLog, k-mer]
author: oxo-call-community
source_url: "https://github.com/fbreitwieser/krakenhll"
---

## Concepts

- **HyperLogLog Integration**: Uses HyperLogLog for efficient cardinality estimation
- **Unique K-mer Counting**: Counts unique k-mers with probabilistic methods
- **Memory Efficiency**: Reduced memory footprint compared to standard Kraken
- **Taxonomic Classification**: Provides accurate taxonomic assignments
- **Large-scale Analysis**: Handles large metagenomic datasets efficiently
- **Streaming Processing**: Supports streaming-based processing

## Pitfalls

- **Probabilistic Counting**: Approximate counts have some error margin
- **Database Size**: Large databases still require significant storage
- **Classification Accuracy**: HyperLogLog trade-offs may affect accuracy
- **Parameter Tuning**: Default parameters may need adjustment
- **Novel Taxa**: Novel organisms may not be properly classified
- **Cross-talk**: Rare taxa may have interference effects

## Examples

### Classify reads
**Args:** `krakenhll --db database --threads 8 --fastq-input reads.fastq --output results.kraken`
**Explanation:** Classifies reads using HyperLogLog-enhanced Kraken.

### Build database
**Args:** `krakenhll-build --build --db custom_db --threads 8`
**Explanation:** Builds custom KrakenHLL database.

### Generate report
**Args:** `krakenhll --db database --fastq-input reads.fastq --report results.report`
**Explanation:** Creates detailed classification report.

### Paired-end mode
**Args:** `krakenhll --db database --paired reads_1.fastq reads_2.fastq --output results.kraken`
**Explanation:** Processes paired-end reads.

### Confidence filtering
**Args:** `krakenhll --db database --confidence 0.15 --fastq-input reads.fastq --output results.kraken`
**Explanation:** Filters by minimum confidence score.

### Estimate read count
**Args:** `krakenhll --db database --fastq-input reads.fastq --estimate-counts`
**Explanation:** Estimates unique read counts per taxon.