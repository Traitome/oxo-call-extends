---
name: metawrap-kraken
category: metagenomics
description: MetaWRAP requirements for kraken step
tags: [metawrap-kraken, metagenomics, classification]
author: oxo-call-community
source_url: "https://github.com/bxlab/metaWRAP"
---

## Concepts

- **Tool Overview**: MetaWRAP Kraken v1.3.0 provides Kraken-based taxonomic classification as part of the MetaWRAP pipeline.
- **Core Function**: Performs taxonomic classification using the Kraken algorithm.
- **Kraken Integration**: Integrates the Kraken taxonomic classifier into MetaWRAP.
- **MetaWRAP Integration**: Works as part of the MetaWRAP metagenomic analysis pipeline.
- **Input/Output**: Accepts sequencing reads; outputs taxonomic classifications.
- **High-Speed Classification**: Leverages Kraken's fast k-mer based classification.

## Pitfalls

- **MetaWRAP Dependency**: Designed to work within the MetaWRAP pipeline.
- **Database Size**: Kraken databases can be large and require significant storage.
- **Computational Resources**: Processing large datasets may require significant computational resources.
- **Memory Requirements**: Memory usage can be high for large input datasets.
- **Parameter Tuning**: May require parameter adjustment for optimal results.
- **Database Completeness**: Classification accuracy depends on reference database completeness.

## Examples

### Classify reads with Kraken
**Args:** `metawrap-kraken -i reads.fastq -o classifications.txt`
**Explanation:** Classifies metagenomic reads using Kraken.

### With custom database
**Args:** `metawrap-kraken -i reads.fastq -d kraken_db/ -o classifications.txt`
**Explanation:** Uses custom Kraken database for classification.

### Paired-end analysis
**Args:** `metawrap-kraken -i reads_1.fastq -r reads_2.fastq -o classifications.txt`
**Explanation:** Processes paired-end sequencing data.

### Generate report
**Args:** `metawrap-kraken -i reads.fastq -o classifications.txt -r report.html`
**Explanation:** Generates comprehensive classification report.

### Batch processing
**Args:** `metawrap-kraken -i fastq/ -o classifications/`
**Explanation:** Processes multiple samples in batch mode.