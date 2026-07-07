---
name: hops
category: metagenomics
description: Java tool to work with ancient metagenomics - automated detection and authentication of pathogen DNA in archaeological remains
tags: [hops, metagenomics, ancient_dna, pathogen, contamination]
author: oxo-call-community
source_url: "https://github.com/rhuebler/HOPS/"
---

## Concepts

- **Ancient DNA Analysis**: Specialized pipeline for processing degraded DNA from archaeological remains
- **Pathogen Detection**: Automated screening pipeline for identifying ancient microbial pathogens
- **Contamination Authentication**: Robust scoring system to validate authenticity of ancient DNA sequences
- **MALT Integration**: Uses MEGAN Alignment Tool for accurate taxonomic classification
- **KrakenUniq Support**: Incorporates KrakenUniq for sensitive and specific species identification
- **aDNA Damage Patterns**: Detects characteristic C->T and G->A damage patterns in ancient DNA

## Pitfalls

- **Contamination Risk**: Modern DNA contamination can severely affect results; strict laboratory protocols required
- **Low Coverage**: Ancient samples often have low DNA yield, requiring sensitive detection methods
- **DNA Damage**: Post-mortem DNA damage can introduce sequencing errors and false positives
- **Reference Database Quality**: Results depend heavily on the completeness of reference databases
- **Memory Requirements**: High memory consumption on large datasets compared to alternative tools
- **Computational Time**: Processing large ancient metagenomic datasets can be computationally intensive

## Examples

### Basic ancient pathogen screening
**Args:** `hops -i ancient_reads.fastq -o pathogen_results/ -d /path/to/reference/db`
**Explanation:** Runs the complete HOPS pipeline for pathogen detection in ancient DNA samples.

### With contamination filtering
**Args:** `hops -i ancient_reads.fastq -o pathogen_results/ -d /path/to/db --filter-contamination`
**Explanation:** Applies contamination filtering to remove potential modern DNA contaminants.

### Taxonomic profiling mode
**Args:** `hops -i ancient_reads.fastq -o profiling_results/ --mode profile`
**Explanation:** Runs in taxonomic profiling mode to generate comprehensive microbial community composition.

### Custom authentication threshold
**Args:** `hops -i ancient_reads.fastq -o results/ -d /path/to/db --auth-threshold 0.8`
**Explanation:** Sets a custom authentication threshold (0.8) for determining sequence authenticity.

### Batch processing mode
**Args:** `hops --batch sample_list.txt -o batch_results/ -d /path/to/db`
**Explanation:** Processes multiple samples in batch mode using a sample list file.