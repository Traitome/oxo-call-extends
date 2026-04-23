---
name: bs-seeker2
category: epigenomics
description: Accurate and fast mapping of bisulfite-treated short reads
tags: [bs-seeker2, bisulfite, methylation, alignment, wgbs]
author: oxo-call-community
source_url: "https://github.com/BSSeeker/BSseeker2"
---

## Concepts

- **Tool Overview**: BS Seeker 2 maps bisulfite-treated short reads accurately and efficiently.
- **Core Function**: Aligns bisulfite-converted reads to reference genome for methylation analysis.
- **Algorithm**: Three-letter alignment approach for efficient bisulfite read mapping.
- **Input**: Bisulfite-treated FASTQ files and reference genome.
- **Output**: Mapped reads and methylation calls.
- **Installation**: Install via bioconda: `conda install -c bioconda bs-seeker2`

## Pitfalls

- **Reference Indexing**: Must build BS Seeker index before alignment.
- **Strand Direction**: Specify library type (directional vs non-directional).
- **Bowtie/Bowtie2**: Requires Bowtie or Bowtie2 as alignment backend.
- **Memory Usage**: Large genomes require significant memory for indexing.

## Examples

### Build genome index
**Args:** `bs_seeker2-build.py -f genome.fa --aligner=bowtie2 -d genome_index/`
**Explanation:** Builds BS Seeker2 index using Bowtie2 as aligner.

### Align bisulfite reads
**Args:** `bs_seeker2-align.py -i reads.fq -d genome_index/ -o aligned.bam --aligner=bowtie2`
**Explanation:** Aligns bisulfite reads to indexed reference genome.

### Call methylation levels
**Args:** `bs_seeker2-call_methylation.py -i aligned.bam -o methylation.tsv`
**Explanation:** Extracts methylation levels from aligned bisulfite reads.

### Paired-end alignment
**Args:** `bs_seeker2-align.py -1 R1.fq -2 R2.fq -d genome_index/ -o paired.bam`
**Explanation:** Aligns paired-end bisulfite reads.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
