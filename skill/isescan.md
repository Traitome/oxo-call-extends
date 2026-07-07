---
name: isescan
category: annotation
description: Python pipeline to identify IS (Insertion Sequence) elements in genome and metagenome
tags: [isescan, insertion-sequence, IS-elements, genome-annotation]
author: oxo-call-community
source_url: "https://github.com/xiezhq/ISEScan"
---

## Concepts

- **Tool Overview**: ISEScan (v1.7.3) - A highly sensitive pipeline for identifying Insertion Sequence elements in prokaryotic genomes
- **Algorithm**: Based on profile Hidden Markov Models (pHMMs) constructed from manually curated IS elements
- **Detection Capabilities**: Identifies complete and incomplete IS elements with high sensitivity (100%)
- **Family Classification**: Automatically classifies IS elements into families using ISfinder database
- **Output Formats**: Generates CSV statistics and GFF annotation files for downstream analysis
- **Transposase Prediction**: Uses FragGeneScan for transposase ORF prediction

## Pitfalls

- **False Positives**: May report false positives for short or degenerate IS elements
- **Assembly Quality**: Requires well-assembled sequences for optimal performance
- **Database Dependencies**: Relies on pHMM database which may need periodic updates
- **Computational Requirements**: Memory-intensive for large metagenomic datasets
- **Output Interpretation**: Multiple overlapping predictions may require manual curation
- **Short IS Elements**: Default settings may miss very short IS elements (<400bp)

## Examples

### Basic IS element detection
**Args:** `isescan --input genome.fasta --output is_elements`
**Explanation:** Identifies IS elements in a prokaryotic genome and outputs results.

### Remove short IS elements
**Args:** `isescan --input assembly.fasta --output results --removeShortIS`
**Explanation:** Filters out incomplete or short IS elements (<400bp) from results.

### Metagenome analysis
**Args:** `isescan --input metagenome.fasta --output mg_results --meta`
**Explanation:** Processes metagenomic sequences to identify IS elements across multiple organisms.

### Output GFF format
**Args:** `isescan --input genome.fasta --output annot --gff`
**Explanation:** Generates GFF annotation file for visualization in genome browsers.

### Custom pHMM database
**Args:** `isescan --input genome.fasta --output results --hmmdb custom_hmms/`
**Explanation:** Uses a custom pHMM database for IS element detection.

### Verbose mode
**Args:** `isescan --input genome.fasta --output results --verbose`
**Explanation:** Provides detailed output including intermediate analysis steps.