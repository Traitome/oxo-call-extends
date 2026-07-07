---
name: stxtyper
category: typing
description: Accurately type both known and unknown Shiga toxin operons from assembled genomic sequence.
tags: [stxtyper, shiga-toxin, bacterial-typing, genomics]
author: oxo-call-community
source_url: "https://github.com/ncbi/stxtyper"
---

## Concepts

- **Tool Overview**: stxtyper (v1.0.25) is a tool for typing Shiga toxin operons from assembled genomic sequences.
- **Core Function**: Identifies and classifies Shiga toxin operons in bacterial genomes.
- **Algorithm**: Uses sequence comparison to identify toxin operon variants.
- **Input/Output**: Input: Assembled genome sequence (FASTA); Output: Toxin type classification.
- **Applications**: Food safety, bacterial typing, pathogen identification.
- **Installation**: `conda install -c bioconda stxtyper` or download from GitHub.

## Pitfalls

- **Assembly Quality**: Poor quality assemblies affect typing accuracy.
- **Sequence Quality**: Low-quality sequences affect detection.
- **Toxin Variants**: Novel toxin variants may not be detected.
- **Memory Requirements**: Large genomes require significant memory.
- **Computational Time**: Processing large genomes can be slow.
- **Database Quality**: Outdated toxin databases affect results.

## Examples

### Display help
**Args:** `stxtyper --help`
**Explanation:** Shows available options and usage information.

### Basic toxin typing
**Args:** `stxtyper -i genome.fasta -o results.txt`
**Explanation:** Type Shiga toxin operons from genome assembly.

### With custom database
**Args:** `stxtyper -i genome.fasta -d toxin_db/ -o results.txt`
**Explanation:** Use custom toxin database.

### Verbose mode
**Args:** `stxtyper -i genome.fasta -o results.txt -v`
**Explanation:** Run with detailed logging for debugging.

### Output VCF
**Args:** `stxtyper -i genome.fasta -o results.vcf --vcf`
**Explanation:** Output results in VCF format.

### Batch processing
**Args:** `stxtyper -i genomes/ -o results/`
**Explanation:** Process multiple genome assemblies together.

### Filter by quality
**Args:** `stxtyper -i genome.fasta -o results.txt -q 20`
**Explanation:** Filter by quality score.

### Include novel variants
**Args:** `stxtyper -i genome.fasta -o results.txt --novel`
**Explanation:** Report novel toxin variants.

### Generate report
**Args:** `stxtyper -i genome.fasta -o results.txt --report`
**Explanation:** Generate comprehensive HTML report.
