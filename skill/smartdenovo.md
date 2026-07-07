---
name: smartdenovo
category: assembly
description: Ultra-fast de novo assembler using long noisy reads from Oxford Nanopore or PacBio
tags: [smartdenovo, assembly, long-reads, nanopore, pacbio]
author: oxo-call-community
source_url: "https://github.com/ruanjue/smartdenovo"
---

## Concepts

- **Tool Overview**: smartdenovo (v1.0.0) - An ultra-fast de novo assembler optimized for long noisy reads
- **Core Function**: Assembles long sequencing reads into contiguous sequences (contigs)
- **Input/Output**: Accepts FASTQ/FASTA reads; outputs assembled contigs in FASTA format
- **Algorithm**: Uses overlap-layout-consensus (OLC) approach optimized for noisy long reads
- **Installation**: `conda install -c bioconda smartdenovo`
- **Key Features**: Ultra-fast assembly, supports Nanopore/PacBio reads, memory-efficient

## Pitfalls

- **Read Quality**: Noisy reads can affect assembly quality
- **Computation Time**: Large datasets may require significant time
- **Memory Usage**: Large genomes require significant memory
- **Parameter Tuning**: Requires careful parameter adjustment for optimal results
- **Repeat Regions**: Struggles with highly repetitive regions
- **Contig Quality**: May produce fragmented assemblies for complex genomes

## Examples

### Display help
**Args:** `smartdenovo --help`
**Explanation:** Shows available options and usage information.

### Basic assembly
**Args:** `smartdenovo -i reads.fastq -o assembly`
**Explanation:** Run de novo assembly on long reads.

### With preset parameters
**Args:** `smartdenovo -i reads.fastq -o assembly -p nano`
**Explanation:** Use preset parameters for Nanopore data.

### With quality filtering
**Args:** `smartdenovo -i reads.fastq -o assembly -q 10`
**Explanation:** Filter reads by quality score >= 10.

### Specify k-mer size
**Args:** `smartdenovo -i reads.fastq -o assembly -k 17`
**Explanation:** Set k-mer size for overlap detection.

### Multi-threaded assembly
**Args:** `smartdenovo -i reads.fastq -o assembly -t 8`
**Explanation:** Use 8 threads for parallel processing.

### With reference-guided assembly
**Args:** `smartdenovo -i reads.fastq -r reference.fasta -o assembly`
**Explanation:** Use reference genome to guide assembly.

### Generate assembly graph
**Args:** `smartdenovo -i reads.fastq -o assembly -g`
**Explanation:** Output assembly graph in GFA format.