---
name: tcontig
category: assembly
description: Tool for processing and analyzing genome assembly contigs.
tags: [tcontig, assembly, contigs, genome-assembly, scaffolding]
author: oxo-call-community
source_url: "https://github.com/cmdoret/tcontig"
---

## Concepts

- **Tool Overview**: tcontig - A command-line tool for processing genome assembly contigs, including filtering, sorting, and analyzing contig statistics.
- **Core Function**: Performs various operations on assembled contigs: filtering by length, sorting, renaming, and generating summary statistics.
- **Input**: FASTA files containing assembled contigs from genome assembly tools.
- **Output**: Processed FASTA files and summary statistics reports.
- **Installation**: `pip install tcontig` or `conda install -c bioconda tcontig`
- **Use Case**: Post-processing of genome assemblies to filter short contigs, sort by length, or rename contigs for downstream analysis.

## Pitfalls

- **Input Quality**: Effective analysis depends on quality of input assembly - contaminated or poor assemblies may give misleading statistics.
- **Length Threshold**: Filtering by length requires careful selection of threshold based on expected genome size and assembly quality.
- **File Format**: Strictly requires valid FASTA format - malformed headers or sequences will cause errors.
- **Memory Usage**: Large genomes with many contigs may require significant memory for processing.

## Examples

### Filter contigs by length
**Args:** `tcontig filter -i assembly.fasta -o filtered.fasta -l 1000`
**Explanation:** Remove contigs shorter than 1000 bp from the assembly.

### Sort contigs by length
**Args:** `tcontig sort -i assembly.fasta -o sorted.fasta`
**Explanation:** Sort contigs in descending order by sequence length.

### Contig statistics
**Args:** `tcontig stats -i assembly.fasta`
**Explanation:** Display summary statistics including N50, L50, total length, and contig count.

### Rename contigs
**Args:** `tcontig rename -i assembly.fasta -o renamed.fasta -p mygenome`
**Explanation:** Rename contigs with a custom prefix for standardization.

### Combined operations
**Args:** `tcontig filter -i assembly.fasta -l 500 | tcontig sort -o cleaned_sorted.fasta`
**Explanation:** Pipe-based combination of filtering and sorting operations.
