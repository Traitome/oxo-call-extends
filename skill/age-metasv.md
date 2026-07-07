---
name: age-metasv
category: alignment
description: Optimal alignment of sequences with structural variants (SVs), modified for MetaSV integration
tags: [age-metasv, alignment, structural-variant, sv, metasv]
author: oxo-call-community
source_url: "https://github.com/marghoob/AGE/tree/simple-parseable-output"
---

## Concepts

- **Tool Overview**: AGE (Alignment with Gaps and Extensions) is an optimal alignment tool for sequences containing structural variants, modified with simple parseable output for MetaSV integration.
- **Core Function**: Performs optimal sequence alignment that can handle structural variations including insertions, deletions, inversions, and translocations.
- **MetaSV Integration**: Modified version produces parseable output format specifically designed for MetaSV structural variant caller pipeline.
- **Input/Output**: Input: FASTQ/FASTA sequences and reference genome. Output: SAM/BAM alignment files with SV-aware alignments.
- **Installation**: Install via bioconda: `conda install -c bioconda age-metasv`
- **Citation**: Mohiyuddin, M., et al. (2015). MetaSV: An accurate and integrative structural-variant caller for next generation sequencing. Bioinformatics, 31(16), 2741-2744.

## Pitfalls

- **MetaSV Specific**: This is a modified version of AGE specifically for MetaSV - not intended for general use outside MetaSV pipeline.
- **Output Format**: Produces simple parseable output format that differs from standard AGE output.
- **Performance**: Optimal alignment algorithms can be computationally intensive for long sequences.
- **SV Complexity**: Complex structural variants may require careful parameter tuning for optimal alignment.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows all available command-line options and parameters.

### Basic alignment to reference
**Args:** `age-metasv -i input.fastq -r reference.fasta -o output.sam`
**Explanation:** Aligns input sequences to reference genome, producing SAM output.

### Align with custom gap penalties
**Args:** `age-metasv -i reads.fastq -r ref.fasta -o aligned.sam -a 10 -b 5`
**Explanation:** Uses custom gap open (-a) and gap extension (-b) penalties for alignment.

### Process paired-end reads
**Args:** `age-metasv -1 R1.fastq -2 R2.fastq -r reference.fasta -o paired.sam`
**Explanation:** Aligns paired-end reads to reference genome.

### Output in BAM format
**Args:** `age-metasv -i reads.fastq -r ref.fasta -o aligned.bam --format bam`
**Explanation:** Produces BAM format output directly for downstream analysis.

### Set minimum alignment score
**Args:** `age-metasv -i reads.fastq -r ref.fasta -o aligned.sam -s 50`
**Explanation:** Filters alignments with minimum score threshold of 50.

### Enable verbose output
**Args:** `age-metasv -i reads.fastq -r ref.fasta -o aligned.sam -v`
**Explanation:** Enables verbose mode for debugging and progress monitoring.