---
name: circle-map
category: utility
description: Circular DNA analysis tools
tags: [circle-map, circular-dna, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/iprada/Circle-Map"
---

## Concepts

- **Tool Overview**: Circle-Map provides tools for analyzing circular DNA elements from high-throughput sequencing data.
- **Core Function**: Detects and characterizes extrachromosomal circular DNA (eccDNA) and other circular DNA elements.
- **Algorithm**: Uses bioinformatic approaches to identify circular DNA junctions and characterize their genomic origin.
- **Input**: Sequencing reads (FASTQ) and alignment files (BAM).
- **Output**: Circular DNA candidates with genomic coordinates and annotations.
- **Application**: Circular DNA discovery, eccDNA analysis, and genome stability studies.
- **Installation**: Install via bioconda: `conda install -c bioconda circle-map`

## Pitfalls

- **Data Quality**: Requires high-quality sequencing data for reliable detection.
- **Mapping Quality**: Depends on accurate read mapping to reference genome.
- **Repeat Regions**: May produce false positives in repetitive genomic regions.
- **Novel Elements**: May miss circular elements not present in reference genome.
- **Computational Resources**: May require significant resources for large datasets.

## Examples

### Detect eccDNA
**Args:** `circle-map detect -i reads.fastq -r reference.fasta -o eccDNA.txt`
**Explanation:** Detects extrachromosomal circular DNA from sequencing reads.

### Analyze BAM file
**Args:** `circle-map analyze -b alignments.bam -o circular_elements.txt`
**Explanation:** Analyzes existing BAM alignment for circular DNA.

### Characterize circular DNA
**Args:** `circle-map characterize -i eccDNA.txt -g annotation.gtf -o results.txt`
**Explanation:** Characterizes detected circular DNA with genomic annotations.

### Display help
**Args:** `circle-map --help`
**Explanation:** Shows all available commands and options.