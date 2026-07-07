---
name: rmap
category: alignment
description: RMAP is a short-read mapping tool for next-generation sequencing data, supporting paired-end and bisulfite-treated reads.
tags: [rmap, alignment, short-read, ngs, bisulfite]
author: oxo-call-community
source_url: "http://smithlabresearch.org/software/rmap/"
---

## Concepts

- **Tool Overview**: RMAP is a short-read mapper for NGS data.
- **Core Function**: Maps Illumina/SOLiD/454 reads to a reference genome.
- **Algorithm**: Uses hash-based seed-and-extend with quality score integration.
- **Input Format**: Accepts FASTA, FASTQ, or FASTA+PRB read files; FASTA chromosome directory.
- **Output**: Produces BED format mapping results.
- **Use Case**: DNA-seq, bisulfite-seq, paired-end read alignment.

## Pitfalls

- **Read Format**: Reads must not span multiple lines; each read occupies exactly one sequence line.
- **Output Required**: If `-o` is not specified, large mapping results will be printed to terminal.
- **Paired-end Input**: Both ends must be concatenated in one FASTA file (read width × 2).
- **Bisulfite Limits**: `rmapbs` only supports single-end bisulfite-treated reads.
- **Mismatches**: Default allowed mismatches (`-m`) is 10; adjust for sensitive mapping.
- **Ambiguous Mappings**: Reads mapping to multiple locations are filtered by default; use `-M` and `-a` to report.

## Examples

### Display help
**Args:** `rmap -help`
**Explanation:** Shows all available flags and usage instructions.

### Basic single-end mapping
**Args:** `rmap -o mapped.bed -c chromosomes_dir reads.fa`
**Explanation:** `-o` specifies BED output file; `-c` specifies chromosome FASTA directory; final positional arg is the reads file.

### Tune seed and mismatches
**Args:** `rmap -S 4 -h 8 -m 20 -o mapped.bed -c chromosomes_dir reads.fa`
**Explanation:** `-S 4` uses 4 seeds; `-h 8` sets seed weight; `-m 20` allows up to 20 mismatches for sensitive mapping.

### Report ambiguously mapped reads
**Args:** `rmap -a amb_mapped.txt -M 10 -o mapped.bed -c chromosomes_dir reads.fa`
**Explanation:** `-M 10` reports reads mapping >10 times to amb_mapped.txt; uniquely mapping reads go to BED.

### Paired-end mapping
**Args:** `rmappe -min-sep 200 -max-sep 600 -o mapped_pe.bed -c chromosomes_dir pe_reads.fa`
**Explanation:** `-min-sep`/`-max-sep` set the expected insert size range; reads must be concatenated in one file.

### Bisulfite-treated reads
**Args:** `rmapbs -B -o mapped_bs.bed -c chromosomes_dir bs_reads.fa`
**Explanation:** `-B` allows unconverted cytosines at CpG positions to assist mapping specificity.

### With quality scores (FASTQ)
**Args:** `rmap -W -o mapped.bed -c chromosomes_dir reads.fq`
**Explanation:** `-W` enables wildcard quality-score-based matching using FASTQ quality values.