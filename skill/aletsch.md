---
name: aletsch
category: expression
description: Accurate and versatile assembler for multiple bulk or single-cell RNA-seq samples
tags: [rna-seq, assembly, transcriptome, single-cell, multi-sample]
author: oxo-call-community
source_url: "https://github.com/Shao-Group/aletsch"
---

## Concepts

- **Tool Overview**: Aletsch is a meta-assembler for precise assembly of multiple bulk or single-cell RNA-seq samples, harnessing information across samples.
- **Core Function**: Assembles transcripts from multiple RNA-seq samples simultaneously, improving assembly completeness through cross-sample information sharing.
- **Input/Output**: Input: Multiple RNA-seq sample BAM files. Output: Assembled transcriptome in FASTA/GTF format.
- **Bridging System**: Uses innovative "bridging" to connect transcripts across samples, recovering transcripts missed in single-sample assemblies.
- **Installation**: Install via bioconda: `conda install -c bioconda aletsch`

## Pitfalls

- **Memory Requirements**: Multi-sample assembly requires substantial memory - scale with sample count.
- **Sample Quality**: Poor quality samples may introduce noise - consider quality filtering before assembly.
- **Reference Optional**: Can work with or without reference genome, but reference improves accuracy.
- **Strand Specificity**: Specify correct library strandedness for accurate transcript assembly.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows assembly options and required parameters.

### Basic multi-sample assembly
**Args:** `assemble -i sample1.bam sample2.bam sample3.bam -o transcripts.gtf`
**Explanation:** Assembles transcripts from multiple RNA-seq samples.

### Assembly with reference genome
**Args:** `assemble -i *.bam -r genome.fa -o transcripts.gtf`
**Explanation:** Uses reference genome to guide transcript assembly.

### Assembly with strand information
**Args:** `assemble -i *.bam -r genome.fa --strand FR -o transcripts.gtf`
**Explanation:** Specifies forward-reverse strand library type for stranded RNA-seq.

### Set minimum transcript length
**Args:** `assemble -i *.bam -l 200 -o transcripts.gtf`
**Explanation:** Filters out transcripts shorter than 200bp.

### Output transcript sequences
**Args:** `assemble -i *.bam -r genome.fa -o transcripts.gtf -s transcripts.fa`
**Explanation:** Outputs both GTF annotation and FASTA sequence file.

### Specify number of threads
**Args:** `assemble -i *.bam -t 16 -o transcripts.gtf`
**Explanation:** Uses 16 threads for parallel assembly.

### Single-cell RNA-seq assembly
**Args:** `assemble -i cell*.bam --single-cell -o sc_transcripts.gtf`
**Explanation:** Optimizes assembly parameters for single-cell RNA-seq data.
