---
name: circle-map-cpp
category: utility
description: C++ implementation of Circle-Map for circular DNA analysis
tags: [circle-map-cpp, circular-dna, bioinformatics, c++]
author: oxo-call-community
source_url: "https://github.com/BGI-Qingdao/Circle-Map-cpp"
---

## Concepts

- **Tool Overview**: Circle-Map-cpp is the C++ implementation of Circle-Map for analyzing circular DNA from sequencing data.
- **Core Function**: Identifies and characterizes circular DNA elements including plasmids, mitochondrial DNA, and extrachromosomal circular DNA (eccDNA).
- **Algorithm**: Uses split-read mapping and paired-end analysis to detect circular DNA junctions.
- **Input**: Sequencing reads (FASTQ/BAM) and reference genome.
- **Output**: Circular DNA candidates with coordinates and supporting evidence.
- **Application**: Circular DNA detection, plasmid analysis, and eccDNA characterization.
- **Installation**: Install via bioconda: `conda install -c bioconda circle-map-cpp`

## Pitfalls

- **Read Quality**: Requires high-quality sequencing data for accurate detection.
- **Reference Bias**: May miss novel circular elements not in reference.
- **Repeat Regions**: Repetitive sequences can interfere with mapping.
- **False Positives**: May detect false circular signals from chimeric reads.
- **Memory Usage**: May require significant memory for large datasets.

## Examples

### Detect circular DNA
**Args:** `circle-map-cpp -i reads.fastq -r reference.fasta -o circular_dna.txt`
**Explanation:** Detects circular DNA elements from sequencing reads.

### With BAM input
**Args:** `circle-map-cpp -b alignments.bam -o circular_dna.txt`
**Explanation:** Analyzes existing BAM alignment for circular DNA.

### Filter by confidence
**Args:** `circle-map-cpp -i reads.fastq -r reference.fasta -c high -o filtered.txt`
**Explanation:** Filters results by confidence level.

### Display help
**Args:** `circle-map-cpp --help`
**Explanation:** Shows all available options and usage information.