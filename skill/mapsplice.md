---
name: mapsplice
category: alignment
description: MapSplice is a software for mapping RNA-seq data to reference genome for splice junction discovery.
tags: [mapsplice, alignment, RNA-seq, splice-junctions]
author: oxo-call-community
source_url: "http://www.netlab.uky.edu/p/bioinfo/MapSplice2"
---

## Concepts

- **Tool Overview**: mapsplice v2.2.1 - MapSplice maps RNA-seq data to reference genome for splice junction discovery without requiring annotations.
- **Core Function**: Identifies splice junctions from RNA-seq reads aligned to reference genome.
- **Input/Output**: Input: FASTQ reads, reference genome; Output: Splice junctions, BAM alignment.
- **Installation**: `conda install -c bioconda mapsplice`
- **De novo Splice Discovery**: Discovers splice junctions without relying on existing annotations.
- **Reference-only**: Depends only on reference genome sequence, not gene annotations.

## Pitfalls

- **Read Quality**: Poor quality reads affect junction detection.
- **Reference Genome**: Must use appropriate reference genome.
- **Memory Usage**: Large datasets require significant memory.
- **Alternative Splicing**: Complex splicing patterns may be missed.
- **Parameter Tuning**: Incorrect parameters affect junction sensitivity.
- **False Positives**: May produce false positive splice junctions.

## Examples

### Run MapSplice
**Args:** `mapsplice.py --threads 8 --fusion --all-chromosomes-files ref.fa --bam-input input.bam --output-dir results/`
**Explanation:** Runs MapSplice with BAM input.

### With FASTQ input
**Args:** `mapsplice.py --threads 8 --fusion --all-chromosomes-files ref.fa --left-fastq reads_1.fastq --right-fastq reads_2.fastq --output-dir results/`
**Explanation:** Processes paired-end FASTQ reads.

### Single-end mode
**Args:** `mapsplice.py --threads 8 --all-chromosomes-files ref.fa --single-end-fastq reads.fastq --output-dir results/`
**Explanation:** Processes single-end reads.

### Verbose mode
**Args:** `mapsplice.py --threads 8 --all-chromosomes-files ref.fa --bam-input input.bam --output-dir results/ -v`
**Explanation:** Provides detailed logging during analysis.

### Fusion detection
**Args:** `mapsplice.py --threads 8 --fusion --all-chromosomes-files ref.fa --bam-input input.bam --output-dir results/`
**Explanation:** Enables fusion gene detection.

### Generate statistics
**Args:** `mapsplice.py --threads 8 --all-chromosomes-files ref.fa --bam-input input.bam --output-dir results/ --stats`
**Explanation:** Generates mapping statistics.