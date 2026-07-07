---
name: strainseeker
category: metagenomics
description: A bacterial identification program for fast identification of bacterial strains from raw sequencing reads.
tags: [strainseeker, metagenomics, bacterial-identification, strain-typing]
author: oxo-call-community
source_url: "http://bioinfo.ut.ee/strainseeker"
---

## Concepts

- **Tool Overview**: strainseeker (v1.5.1) is a fast tool for identifying bacterial strains from sequencing reads.
- **Core Function**: Quickly identifies bacterial strains using reference genome matching and signature analysis.
- **Algorithm**: Uses k-mer based signature matching for rapid strain identification.
- **Input/Output**: Input: Sequencing reads (FASTQ); Output: Strain identification results with confidence scores.
- **Applications**: Clinical diagnostics, food safety testing, microbial identification.
- **Installation**: `conda install -c bioconda strainseeker` or download from website.

## Pitfalls

- **Reference Database**: Outdated or incomplete databases miss strains.
- **Read Quality**: Low-quality reads affect identification accuracy.
- **Strain Novelty**: Novel strains not in database cannot be identified.
- **Mixed Samples**: Mixed bacterial samples produce ambiguous results.
- **Memory Requirements**: Large databases require significant memory.
- **Computational Time**: Processing large datasets can be slow.

## Examples

### Display help
**Args:** `strainseeker --help`
**Explanation:** Shows available options and usage information.

### Basic strain identification
**Args:** `strainseeker -i reads.fastq -o results.txt`
**Explanation:** Identify bacterial strains from sequencing reads.

### With custom database
**Args:** `strainseeker -i reads.fastq -d custom_db/ -o results.txt`
**Explanation:** Use custom reference database for identification.

### Verbose mode
**Args:** `strainseeker -i reads.fastq -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output confidence scores
**Args:** `strainseeker -i reads.fastq -o results.txt --confidence`
**Explanation:** Output confidence scores for each identification.

### Custom thresholds
**Args:** `strainseeker -i reads.fastq -o results.txt -c 0.9`
**Explanation:** Minimum confidence threshold of 0.9.

### Batch processing
**Args:** `strainseeker -i batch/ -o results/`
**Explanation:** Process multiple sequencing samples together.

### Update database
**Args:** `strainseeker --update-db`
**Explanation:** Update reference database to latest version.

### Generate report
**Args:** `strainseeker -i reads.fastq -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
