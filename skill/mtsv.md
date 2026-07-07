---
name: mtsv
category: metagenomics
description: MTSv is a suite of metagenomic binning and analysis tools.
tags: [mtsv, metagenomics, taxonomic-classification, binning, pathogen-detection]
author: oxo-call-community
source_url: "https://github.com/FofanovLab/MTSv"
---

## Concepts

- **Tool Overview**: MTSv v1.0.6 is a suite of metagenomic binning and analysis tools using FM-index and SIMD-accelerated alignment.
- **Core Function**: Performs rapid alignment-based taxonomic classification for metagenomic reads.
- **Algorithm**: Uses FM-index assisted q-gram filter and SIMD accelerated Smith-Waterman algorithm.
- **Efficiency**: Stops alignment search once sufficient quality alignment is found, improving efficiency with large databases.
- **Accuracy**: Provides higher precision than exact k-mer matching approaches with full alignment capability.
- **Applications**: High-confidence pathogen detection, metagenomic analysis, microbiome profiling.

## Pitfalls

- **Database Size**: Performance depends on reference database size and sequence count per taxon.
- **Computational Resources**: Memory requirements increase with larger databases.
- **Read Quality**: Classification accuracy depends on sequencing read quality.
- **Threshold Tuning**: May require parameter adjustment for optimal sensitivity/specificity balance.
- **Draft Genomes**: Assumes properly assembled contigs; quality of input affects output.
- **Species Complexity**: Highly similar genomes may cause classification ambiguity.

## Examples

### Taxonomic classification
**Args:** `mtsv classify -i reads.fastq -o output/ -db reference_db`
**Explanation:** Performs taxonomic classification of metagenomic reads.

### Build reference index
**Args:** `mtsv index -d genomes/ -o index_output/`
**Explanation:** Builds FM-index from reference genome collection.

### Binning contigs
**Args:** `mtsv bin -c contigs.fna -o bins/ -t 8`
**Explanation:** Bins contigs into taxonomic groups using 8 threads.

### Display help
**Args:** `mtsv --help`
**Explanation:** Shows all available commands and options.

### List subcommands
**Args:** `mtsv --help`
**Explanation:** Lists all available subcommands for the tool.
