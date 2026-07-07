---
name: minimap2-coverage
category: alignment
description: A versatile pairwise aligner for genomic and spliced nucleotide sequences modified for use by LongQC
tags: [minimap2-coverage, alignment, long-read]
author: oxo-call-community
source_url: "https://github.com/yfukasawa/LongQC"
---

## Concepts

- **Tool Overview**: minimap2-coverage v1.2.0c is a minimap2 variant for LongQC coverage analysis.
- **Core Function**: Aligns sequencing reads and calculates coverage metrics.
- **Coverage Analysis**: Computes sequencing coverage statistics.
- **Long-read Support**: Optimized for PacBio and Nanopore reads.
- **Input/Output**: Accepts sequence reads; outputs alignment and coverage info.
- **Quality Control**: Supports long-read quality assessment workflows.

## Pitfalls

- **Long-read Specific**: Designed for long sequencing reads.
- **Computational Resources**: Processing large datasets may require significant resources.
- **Memory Requirements**: Memory usage can be high for large reference genomes.
- **Parameter Tuning**: May require parameter adjustment for optimal alignment.
- **Data Quality**: Results depend on input read quality.
- **Reference Genome**: Requires appropriate reference sequences.

## Examples

### Calculate coverage
**Args:** `minimap2-coverage -ax map-ont reference.fasta reads.fastq > alignments.sam`
**Explanation:** Aligns reads and calculates coverage.

### With custom parameters
**Args:** `minimap2-coverage -ax map-pb -k 17 reference.fasta reads.fastq > alignments.sam`
**Explanation:** Uses k-mer size of 17 for PacBio reads.

### Paired-end alignment
**Args:** `minimap2-coverage -ax sr reference.fasta reads_1.fastq reads_2.fastq > alignments.sam`
**Explanation:** Processes paired-end reads.

### Batch processing
**Args:** `minimap2-coverage -ax map-ont reference.fasta fastq/*.fastq > alignments.sam`
**Explanation:** Processes multiple read files.

### Generate BAM output
**Args:** `minimap2-coverage -ax map-ont reference.fasta reads.fastq | samtools view -bS -o alignments.bam`
**Explanation:** Generates BAM format output.