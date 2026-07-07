---
name: dbg2olc
category: assembly
description: Efficient assembly of large genomes using long erroneous reads from third-generation sequencing.
tags: [dbg2olc, assembly, long-reads, genome, hybrid-assembly]
author: oxo-call-community
source_url: "https://github.com/yechengxi/DBG2OLC/raw/master/Manual.docx"
---

## Concepts

- **Tool Overview**: DBG2OLC (v20200723+) is a hybrid genome assembler that combines de Bruijn graph (DBG) construction from short reads with overlap-layout-consensus (OLC) assembly from long reads. It efficiently assembles large genomes using PacBio or Oxford Nanopore reads.
- **Core Function**: Assembles large genomes by using short reads to build a DBG for error correction and long reads for OLC-based scaffolding and consensus.
- **Input/Output**: Input: Long reads (FASTA/FASTQ), short reads (FASTQ). Output: Assembled contigs/scaffolds in FASTA format.
- **Algorithm**: Uses short reads to build a DBG for error correction of long reads, then applies OLC algorithm to corrected long reads for final assembly.
- **Key Features**: Handles noisy long reads, efficient for large genomes, hybrid assembly approach, produces high-quality contigs.
- **Installation**: `conda install -c bioconda dbg2olc`

## Pitfalls

- **Read Coverage**: Requires sufficient coverage of both long and short reads.
- **Memory Usage**: Large genomes require significant memory (100+ GB for human genome).
- **Long Read Quality**: Very noisy long reads may require pre-processing.
- **Parameter Tuning**: K-mer size and other parameters affect assembly quality.
- **Runtime**: Assembly of large genomes can take days.

## Examples

### Basic hybrid assembly
**Args:** `DBG2OLC -k 17 -K 1 -L long_reads.fasta -s short_reads.fasta -o assembly.fasta`
**Explanation:** Assemble genome using k-mer size 17 for DBG and long reads for OLC.

### Adjust parameters for large genome
**Args:** `DBG2OLC -k 21 -K 1 -L long_reads.fasta -s short_reads.fasta -o assembly.fasta -t 16`
**Explanation:** Use 16 threads and k-mer size 21 for large genome assembly.

### Use corrected long reads
**Args:** `DBG2OLC -k 17 -K 1 -L corrected_long_reads.fasta -s short_reads.fasta -o assembly.fasta`
**Explanation:** Assemble using pre-corrected long reads for improved quality.