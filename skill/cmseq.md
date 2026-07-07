---
name: cmseq
category: formatting
description: Set of utilities on sequences and BAM files
tags: [cmseq, sequence-analysis, bam-files, bioinformatics, genomics]
author: oxo-call-community
source_url: "https://github.com/SegataLab/cmseq"
---

## Concepts

- **Tool Overview**: cmseq is a collection of utilities for working with biological sequences and BAM files, providing various sequence manipulation and analysis functions.
- **Core Function**: Offers tools for sequence manipulation, BAM file processing, and sequence analysis tasks.
- **Algorithm**: Implements various sequence processing algorithms for manipulation and analysis.
- **Input**: FASTA/FASTQ sequences and BAM/SAM alignment files.
- **Output**: Processed sequences, alignment files, and analysis results.
- **Application**: Sequence analysis, alignment processing, and genomic data manipulation.
- **Installation**: Install via bioconda: `conda install -c bioconda cmseq`

## Pitfalls

- **BAM Format**: Requires properly formatted BAM files.
- **Sequence Quality**: Poor quality sequences may affect results.
- **Memory Usage**: May require significant memory for large BAM files.
- **Index Files**: BAM files need to be indexed for certain operations.
- **Tool Specificity**: Different subcommands have different requirements.

## Examples

### Extract sequences from BAM
**Args:** `cmseq extract -i alignments.bam -o sequences.fasta`
**Explanation:** Extracts sequences from BAM file.

### Filter BAM file
**Args:** `cmseq filter -i alignments.bam -o filtered.bam -q 30`
**Explanation:** Filters BAM file by mapping quality (>=30).

### Statistics on BAM
**Args:** `cmseq stats -i alignments.bam -o stats.txt`
**Explanation:** Generates statistics from BAM file.

### Display help
**Args:** `cmseq --help`
**Explanation:** Shows all available options and usage information.