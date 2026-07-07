---
name: tdrmapper
category: mapping
description: TDRMapper - DNA/RNA tandem repeat mapping tool for next-generation sequencing data.
tags: [tdrmapper, tandem-repeat, mapping, ngs, short-reads, repeat-elements]
author: oxo-call-community
source_url: "https://github.com/TDRM/TDRMapper"
---

## Concepts

- **Tool Overview**: TDRMapper (Tandem Repeat Mapper) - A tool for mapping and characterizing tandem repeats from next-generation sequencing data.
- **Core Function**: Aligns reads containing tandem repeats to reference genomes and characterizes repeat variation.
- **Input**: FASTQ files from NGS sequencing, reference genome.
- **Output**: Mapped reads, repeat characterization statistics, and allele frequency estimates.
- **Installation**: `conda install -c bioconda tdrmapper`
- **Use Case**: Population studies of tandem repeat expansions, evolutionary analysis of repeat variation.

## Pitfalls

- **Read Length**: Short reads may not span entire repeat units - adjust repeat unit size expectations.
- **Complex Repeats**: Highly complex or variable repeats may be difficult to map accurately.
- **Coverage**: Adequate sequencing depth needed for accurate allele frequency estimation.

## Examples

### Map reads to tandem repeats
**Args:** `tdrmapper -r reference.fasta -i reads.fastq -o results/`
**Explanation:** Map reads and characterize tandem repeats against reference.

### Specify repeat unit
**Args:** `tdrmapper -r genome.fasta -i sample.fastq -o output/ -u "ATG" -l 12`
**Explanation:** Specify expected repeat unit motif (ATG) and minimum repeat count (12).

### Paired-end mode
**Args:** `tdrmapper -r genome.fasta -1 R1.fastq.gz -2 R2.fastq.gz -o results/`
**Explanation:** Use paired-end read mapping for better repeat characterization.
