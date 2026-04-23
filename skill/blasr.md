---
name: blasr
category: alignment
description: PacBio long read aligner for mapping long reads to reference genomes
tags: [blasr, pacbio, long-read, alignment, smrt]
author: oxo-call-community
source_url: "https://github.com/PacificBiosciences/blasr"
---

## Concepts

- **Tool Overview**: BLASR is a long-read aligner developed by PacBio for mapping SMRT sequencing reads.
- **Core Function**: Aligns long, noisy reads (10kb-50kb) to reference genomes with high accuracy.
- **Algorithm**: Uses suffix array indexing for fast seed lookup followed by banded alignment.
- **Input Types**: FASTA/FASTQ files from PacBio sequencing; supports subread filtering.
- **Output Formats**: SAM, BAM, and custom output formats for downstream analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda blasr`

## Pitfalls

- **Read Length**: Optimized for long reads; short reads may have lower accuracy.
- **Error Profile**: Handles PacBio error profile; may not be optimal for ONT reads.
- **Memory Usage**: Large reference genomes require significant memory for indexing.
- **Thread Count**: Use multiple threads for faster alignment of large datasets.
- **Output Sorting**: Output is not sorted by default; use samtools for sorting.

## Examples

### Basic long read alignment
**Args:** `blasr reads.fa reference.fa -o aligned.sam`
**Explanation:** Aligns PacBio long reads to reference genome outputting SAM format.

### Output BAM format
**Args:** `blasr reads.fa reference.fa -bam -o aligned.bam`
**Explanation:** Outputs alignment directly in BAM format for smaller file size.

### Multi-threaded alignment
**Args:** `blasr reads.fa reference.fa -nproc 8 -o aligned.sam`
**Explanation:** Uses 8 threads for parallel alignment processing.

### Best N alignments
**Args:** `blasr reads.fa reference.fa -bestn 5 -o aligned.sam`
**Explanation:** Reports up to 5 best alignments per read for multi-mapping analysis.

### Adjust minimum alignment length
**Args:** `blasr reads.fa reference.fa -minMatch 15 -o aligned.sam`
**Explanation:** Sets minimum match length to 15bp for more sensitive alignment.

### SAM output with headers
**Args:** `blasr reads.fa reference.fa -sam -out aligned.sam -header`
**Explanation:** Outputs SAM format with proper header for downstream compatibility.

### Filter by alignment score
**Args:** `blasr reads.fa reference.fa -minAlnLength 1000 -o aligned.sam`
**Explanation:** Only reports alignments with minimum 1000bp aligned length.
