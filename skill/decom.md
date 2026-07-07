---
name: decom
category: formatting
description: decOM - Microbial source tracking of ancient oral samples using k-mers.
tags: [decom, formatting, microbial-source-tracking, ancient-dna, k-mer]
author: oxo-call-community
source_url: "https://github.com/CamilaDuitama/decOM"
---

## Concepts

- **Tool Overview**: decom (v0.0.32+) is a k-mer-based tool for microbial source tracking and contamination assessment in ancient oral samples. It identifies potential microbial contaminants and assigns sources to ancient DNA sequences.
- **Core Function**: Analyzes ancient DNA sequencing data to identify microbial contaminants and determine their likely sources using k-mer comparison with modern reference databases.
- **Input/Output**: Input: Ancient DNA sequencing reads (FASTQ), modern reference databases. Output: Contamination assessment, source assignments, k-mer matches.
- **Algorithm**: Uses k-mer counting and comparison to identify microbial signatures in ancient samples and match them to known sources in reference databases.
- **Key Features**: Ancient DNA-specific, contamination detection, source tracking, k-mer based, handles degraded DNA.
- **Installation**: `conda install -c bioconda decom`

## Pitfalls

- **DNA Degradation**: Ancient DNA degradation affects k-mer detection.
- **Reference Database**: Results depend on reference database completeness.
- **Contamination Levels**: Very low-level contamination may be undetectable.
- **Sequence Quality**: Poor quality sequences affect k-mer matching.
- **Database Updates**: Reference databases may require regular updates.

## Examples

### Assess contamination
**Args:** `decom -i ancient_reads.fastq -d reference_db/ -o contamination_report.txt`
**Explanation:** Assess microbial contamination in ancient DNA sample.

### Identify sources
**Args:** `decom -i ancient_reads.fastq -d reference_db/ --identify-sources -o sources.txt`
**Explanation:** Identify likely sources of microbial contaminants.

### Specify k-mer size
**Args:** `decom -i ancient_reads.fastq -d reference_db/ -k 21 -o report.txt`
**Explanation:** Use k-mer size of 21 for analysis.