---
name: abeona
category: assembly
description: A simple transcriptome assembler based on kallisto and Cortex graphs.
tags: [abeona, assembly, transcriptome, kallisto, cortex, rna-seq]
author: oxo-call-community
source_url: "https://github.com/winni2k/abeona"
---

## Concepts

- **Tool Overview**: Abeona is a transcriptome assembler that combines kallisto quantification with Cortex graph-based assembly. Version 0.45.0.
- **Core Function**: Assembles transcriptomes using kallisto for quantification guidance and Cortex de Bruijn graphs for assembly.
- **Assembly Pipeline**: 
  1. Assembles reads into a De Bruijn graph
  2. Prunes tips and low-coverage unitigs
  3. Partitions the De Bruijn graph into subgraphs
  4. Generates candidate transcripts by simple path traversal
  5. Filters candidates by kallisto quantification
- **Input/Output**: Input is RNA-seq reads (FASTQ); output is assembled transcripts (FASTA).
- **Installation**: Install via bioconda: `conda install -c bioconda abeona`
- **Platform Support**: Linux (requires Python >= 3.6)
- **Dependencies**: Requires bwa, cortexpy (0.45.7), kallisto (0.44.0), mccortex (1.0), nextflow, pandas, progressbar2

## Pitfalls

- **Version Differences**: Command-line options may vary between versions. Always check `--help` for your installed version.
- **Kallisto Dependency**: Requires kallisto to be installed and in PATH.
- **Memory Usage**: Cortex graph construction can be memory-intensive for large transcriptomes.
- **Nextflow Pipeline**: Abeona uses Nextflow for workflow management.

## Examples

### Display help and version information
**Args:** `abeona --help`
**Explanation:** Shows all available command-line options and usage information.

### Basic transcriptome assembly
**Args:** `abeona assemble --reads reads_1.fastq reads_2.fastq --output assembly_output/`
**Explanation:** Assembles transcripts from paired-end RNA-seq reads using kallisto-guided Cortex graph assembly.

### Assembly with custom k-mer size
**Args:** `abeona assemble --kmer 31 --reads reads.fastq --output results/`
**Explanation:** Uses 31-mers for the de Bruijn graph construction. K-mer size affects assembly contiguity and error rate.

### Run with multiple threads
**Args:** `abeona assemble --threads 8 --reads R1.fastq R2.fastq --output output/`
**Explanation:** Uses 8 threads for parallel processing to speed up assembly.

### Specify temporary directory
**Args:** `abeona assemble --reads reads.fastq --tmp-dir /scratch/tmp --output results/`
**Explanation:** Uses a specific temporary directory for intermediate files, useful for large datasets.