---
name: datafunk
category: formatting
description: Miscellaneous data manipulation tools for FASTA and SAM files
tags: [datafunk, formatting, FASTA, SAM, data-manipulation]
author: oxo-call-community
source_url: "https://github.com/cov-ert/datafunk"
---

## Concepts

- **Tool Overview**: datafunk (v0.1.0+) provides miscellaneous data manipulation tools for FASTA and SAM/BAM files.
- **Core Function**: Performs various sequence and alignment manipulation tasks for bioinformatics workflows.
- **Input/Output**: Input: FASTA sequences, SAM/BAM alignments. Output: Modified sequences, filtered alignments.
- **Algorithm**: Various sequence processing algorithms for filtering, transforming, and analyzing data.
- **Key Features**: Sequence filtering, alignment processing, format conversion.
- **Installation**: `conda install -c bioconda datafunk`

## Pitfalls

- **Input Format**: Requires properly formatted input files.
- **Memory Usage**: Large files may require careful memory management.
- **Filtering Criteria**: Appropriate filtering thresholds must be set.
- **Output Format**: Different output formats have different requirements.
- **Performance**: Complex operations may be slow on very large datasets.

## Examples

### Filter FASTA by length
**Args:** `datafunk filter-fasta -i input.fasta -o filtered.fasta --min-length 1000`
**Explanation:** Filter sequences by minimum length of 1000bp.

### Extract reads from SAM
**Args:** `datafunk extract-reads -i alignments.sam -o extracted.fastq --mapping-quality 30`
**Explanation:** Extract reads with mapping quality >= 30.

### Convert SAM to BAM
**Args:** `datafunk sam2bam -i input.sam -o output.bam`
**Explanation:** Convert SAM alignment file to BAM format.
