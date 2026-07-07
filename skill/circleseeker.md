---
name: circleseeker
category: assembly
description: Comprehensive eccDNA detection from PacBio HiFi sequencing data
tags: [circleseeker, eccdna, pacbio, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/leoxqy/CircleSeeker#readme"
---

## Concepts

- **Tool Overview**: CircleSeeker is a specialized bioinformatics pipeline for identifying, classifying, and characterizing extrachromosomal circular DNA (eccDNA) from PacBio HiFi long-read sequencing data.
- **Core Function**: Detects eccDNA molecules by analyzing circular consensus sequencing (CCS) reads from PacBio platforms.
- **Algorithm**: Uses alignment-free and alignment-based approaches to identify circular DNA signatures.
- **Input**: PacBio HiFi reads in FASTQ format.
- **Output**: eccDNA candidates with sequence information and genomic annotations.
- **Application**: eccDNA discovery, genome stability research, and cancer genomics.
- **Installation**: Install via bioconda: `conda install -c bioconda circleseeker`

## Pitfalls

- **Data Quality**: Requires high-quality HiFi reads for accurate detection.
- **Sequencing Depth**: May miss low-abundance eccDNA without sufficient coverage.
- **Reference Bias**: May miss eccDNA from unannotated genomic regions.
- **Computational Resources**: May require significant memory and processing time.
- **False Positives**: May detect false circular signals from chimeric reads.

## Examples

### Detect eccDNA from HiFi reads
**Args:** `circleseeker -i hifi_reads.fastq -o eccDNA_results.txt`
**Explanation:** Detects extrachromosomal circular DNA from PacBio HiFi reads.

### With reference genome
**Args:** `circleseeker -i hifi_reads.fastq -r reference.fasta -o results.txt`
**Explanation:** Uses reference genome for eccDNA characterization.

### Classify eccDNA types
**Args:** `circleseeker -i hifi_reads.fastq --classify -o classified.txt`
**Explanation:** Classifies detected eccDNA into different categories.

### Display help
**Args:** `circleseeker --help`
**Explanation:** Shows all available options and usage information.