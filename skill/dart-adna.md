---
name: dart-adna
category: metagenomics
description: DART - Damage-Aware Read Translation for ancient DNA metagenomics
tags: [dart-adna, metagenomics, ancient-DNA, read-translation, metagenomics]
author: oxo-call-community
source_url: "https://github.com/genomewalker/dart/wiki"
---

## Concepts

- **Tool Overview**: dart-adna (v1.0.4+) is a tool for damage-aware read translation specifically designed for ancient DNA metagenomics.
- **Core Function**: Translates sequencing reads while accounting for ancient DNA damage patterns to improve taxonomic classification.
- **Input/Output**: Input: FASTQ reads from ancient samples. Output: Translated reads, taxonomic assignments.
- **Algorithm**: Incorporates damage models into read translation for improved microbial identification.
- **Key Features**: Damage-aware translation, ancient DNA optimization, metagenomic classification.
- **Installation**: `conda install -c bioconda dart-adna`

## Pitfalls

- **Ancient DNA Damage**: Requires appropriate damage models for accurate translation.
- **Reference Database**: Needs comprehensive microbial reference database.
- **Fragment Length**: Ancient DNA fragmentation affects translation accuracy.
- **Contamination Control**: Pre-modern contamination can affect results.
- **Validation**: Results require careful interpretation and validation.

## Examples

### Translate ancient DNA reads
**Args:** `dart-adna translate -i ancient_reads.fastq -o translated_reads.fastq`
**Explanation:** Perform damage-aware translation of ancient DNA reads.

### Classify metagenome
**Args:** `dart-adna classify -i translated.fastq -d microbes.db -o classification.txt`
**Explanation:** Classify translated reads against microbial database.

### Adjust damage parameters
**Args:** `dart-adna translate -i reads.fastq -o output.fastq --damage-rate 0.03`
**Explanation:** Use custom damage rate for read translation.
