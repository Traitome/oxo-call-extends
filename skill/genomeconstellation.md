---
name: genomeconstellation
category: classification
description: Genome Constellation - Fast, accurate and versatile k-mer based classification system.
tags: [genomeconstellation, k-mer, classification, metagenomics]
author: oxo-call-community
source_url: "https://bitbucket.org/berkeleylab/jgi-genomeconstellation"
---

## Concepts
- **k-mer Classification**: Uses k-mer based classification.
- **Genome Classification**: Classifies genomes based on k-mer profiles.
- **Metagenomic Analysis**: Analyzes metagenomic data.
- **Fast Comparison**: Enables fast genome comparison.
- **Taxonomic Identification**: Identifies taxonomic relationships.

## Pitfalls
- **k-mer Size Selection**: Results depend on k-mer size.
- **Memory Usage**: Large k-mer databases require significant memory.
- **Database Building**: Requires time to build k-mer databases.
- **Sensitivity**: May miss divergent sequences.
- **False Positives**: May have false positive matches.

## Examples
### Build k-mer index
**Args:** `genomeconstellation build -i genomes.fasta -o index/`
**Explanation:** Builds k-mer index from reference genomes.

### Classify sequence
**Args:** `genomeconstellation classify -i query.fasta -d index/ -o results.txt`
**Explanation:** Classifies query sequence using k-mer index.

### Compare genomes
**Args:** `genomeconstellation compare -i genome1.fasta genome2.fasta -o comparison.txt`
**Explanation:** Compares two genomes using k-mers.

### Batch classification
**Args:** `genomeconstellation classify -i ./queries/ -d index/ -o ./results/`
**Explanation:** Classifies multiple sequences in batch.

### Generate report
**Args:** `genomeconstellation classify -i query.fasta -d index/ -r -o report.html`
**Explanation:** Generates detailed classification report.