---
name: mtsv-tools
category: alignment
description: mtsv_tools contains core tools for alignment-based metagenomic/metatranscriptomic assignment.
tags: [mtsv-tools, metagenomics, alignment, metatranscriptomics, taxonomic]
author: oxo-call-community
source_url: "https://github.com/FofanovLab/mtsv_tools"
---

## Concepts

- **Tool Overview**: mtsv-tools v2.1.1 provides core alignment-based tools for metagenomic and metatranscriptomic analysis.
- **Core Function**: Performs taxonomic assignment using alignment-based approaches.
- **Input**: Accepts FASTA/FASTQ reads and reference databases.
- **Output**: Provides taxonomic assignments and abundance estimates.
- **Integration**: Part of the MTSv ecosystem for comprehensive metagenomics.
- **Installation**: Available via Bioconda (`conda install -c bioconda mtsv-tools`).

## Pitfalls

- **Reference Quality**: Classification accuracy depends on reference database completeness.
- **Memory Usage**: Large read sets require substantial memory for alignment processing.
- **E-value Selection**: Appropriate E-value cutoff is crucial for balancing sensitivity/specificity.
- **Input Format**: Requires properly formatted FASTA/FASTQ input.
- **Species Representation**: May miss taxa not represented in reference database.
- **Computational Time**: Full alignment approach is slower than k-mer methods.

## Examples

### Metagenomic assignment
**Args:** `mtsv-tools assign -i sample.fastq -o results/ -db refdb`
**Explanation:** Assigns taxonomic labels to input reads.

### Build custom database
**Args:** `mtsv-tools build-db -i genomes/ -o custom_db/`
**Explanation:** Builds custom reference database from genome files.

### Abundance profiling
**Args:** `mtsv-tools profile -i alignments.bam -o abundance.tsv`
**Explanation:** Generates taxonomic abundance profile from alignments.

### Display help
**Args:** `mtsv-tools --help`
**Explanation:** Shows usage information and available options.

### Filter low-confidence hits
**Args:** `mtsv-tools filter -i assignments.tsv -o filtered.tsv -c 0.8`
**Explanation:** Filters assignments below 80% confidence threshold.
