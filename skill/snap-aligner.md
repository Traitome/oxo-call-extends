---
name: snap-aligner
category: alignment
description: SNAP - Scalable Nucleotide Alignment Program for fast and accurate read alignment
tags: [snap-aligner, alignment, ngs, sequencing, mapping]
author: oxo-call-community
source_url: "https://www.microsoft.com/en-us/research/project/snap"
---

## Concepts

- **Tool Overview**: snap-aligner (v2.0.5) - A fast and accurate read aligner for high-throughput sequencing
- **Core Function**: Aligns sequencing reads to reference genome with high speed and accuracy
- **Input/Output**: Accepts FASTQ reads; outputs SAM/BAM aligned files
- **Algorithm**: Uses hash-based indexing for fast alignment with sensitivity optimization
- **Installation**: `conda install -c bioconda snap-aligner`
- **Key Features**: Fast alignment, accurate mapping, memory-efficient

## Pitfalls

- **Index Building**: Requires building SNAP index before alignment
- **Memory Requirements**: Large genomes require significant memory for indexing
- **Read Length**: Optimized for specific read length ranges
- **Reference Format**: Requires specific reference file format
- **Output Format**: Default output is SAM format
- **Paired-End**: Paired-end alignment requires specific parameters

## Examples

### Display help
**Args:** `snap-aligner --help`
**Explanation:** Shows available options and usage information.

### Build index
**Args:** `snap-aligner index reference.fasta index_dir/`
**Explanation:** Build SNAP index from reference genome.

### Single-end alignment
**Args:** `snap-aligner single index_dir/ reads.fastq -o aligned.sam`
**Explanation:** Align single-end reads to reference.

### Paired-end alignment
**Args:** `snap-aligner paired index_dir/ reads_1.fastq reads_2.fastq -o aligned.sam`
**Explanation:** Align paired-end reads to reference.

### With quality filtering
**Args:** `snap-aligner single index_dir/ reads.fastq -o aligned.sam -q 20`
**Explanation:** Filter alignments by minimum quality score.

### Output BAM format
**Args:** `snap-aligner single index_dir/ reads.fastq -o aligned.bam -b`
**Explanation:** Output alignments in BAM format.

### With thread count
**Args:** `snap-aligner single index_dir/ reads.fastq -o aligned.sam -t 8`
**Explanation:** Use 8 threads for alignment.

### With sensitivity mode
**Args:** `snap-aligner single index_dir/ reads.fastq -o aligned.sam -s sensitive`
**Explanation:** Run in sensitive mode for better accuracy.