---
name: circularmapper
category: alignment
description: Improve mappings on circular genomes using BWA mapper
tags: [circularmapper, alignment, circular-genome, bwa, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/apeltzer/CircularMapper"
---

## Concepts

- **Tool Overview**: CircularMapper improves read mapping on circular genomes by handling the circular nature of bacterial genomes, plasmids, and mitochondrial DNA.
- **Core Function**: Processes reads that span the origin of replication in circular genomes, ensuring proper alignment.
- **Algorithm**: Uses BWA for initial mapping and then fixes alignments that cross the circular boundary.
- **Input**: Sequencing reads (FASTQ) and circular reference genome (FASTA).
- **Output**: Improved alignment file (SAM/BAM) with proper handling of circular boundaries.
- **Application**: Bacterial genome analysis, plasmid sequencing, and mitochondrial DNA studies.
- **Installation**: Install via bioconda: `conda install -c bioconda circularmapper`

## Pitfalls

- **Reference Genome**: Must be a circular genome; not suitable for linear chromosomes.
- **BWA Dependency**: Requires BWA to be installed and available.
- **Memory Usage**: May require significant memory for large genomes.
- **Read Length**: Short reads may not span the origin of replication.
- **Indexing**: Requires BWA index to be built first.

## Examples

### Map reads to circular genome
**Args:** `circularmapper -i reads.fastq -r circular_genome.fasta -o alignments.sam`
**Explanation:** Maps reads to circular genome with proper boundary handling.

### With BWA options
**Args:** `circularmapper -i reads.fastq -r circular_genome.fasta -o alignments.sam -b "-t 4"`
**Explanation:** Passes additional BWA options (4 threads).

### Paired-end mapping
**Args:** `circularmapper -1 read1.fastq -2 read2.fastq -r circular_genome.fasta -o alignments.sam`
**Explanation:** Maps paired-end reads to circular genome.

### Display help
**Args:** `circularmapper --help`
**Explanation:** Shows all available options and usage information.