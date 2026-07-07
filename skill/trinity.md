---
name: trinity
category: expression
description: Trinity assembles transcript sequences from Illumina RNA-Seq data.
tags: [trinity, expression, rna-seq, transcriptome, assembly]
author: oxo-call-community
source_url: "https://github.com/trinityrnaseq/trinityrnaseq/wiki"
---

## Concepts

- **Tool Overview**: Trinity (v2.15.2+) is a comprehensive de novo transcriptome assembler designed specifically for Illumina RNA-Seq data. It reconstructs full-length transcripts and alternative splicing isoforms.
- **Core Function**: Assembles RNA-Seq reads into complete transcript sequences using a three-step process: Inchworm, Chrysalis, and Butterfly.
- **Input/Output**: Input: FASTQ reads (paired-end or single-end). Output: Assembled transcripts (Trinity.fasta), assembly statistics, and optional abundance estimates.
- **Algorithm**: Three-stage process: Inchworm (k-mer based contig assembly), Chrysalis (de Bruijn graph clustering), and Butterfly (path traversal for full-length transcripts).
- **Key Features**: Handles alternative splicing, supports strand-specific RNA-seq, integrates with downstream analysis tools (RSEM, Salmon), and includes quality assessment.
- **Installation**: `conda install -c bioconda trinity`

## Pitfalls

- **Memory Requirements**: Trinity requires substantial memory (minimum 8GB, recommended 32GB+ for large datasets). Use `--max_memory` to specify memory allocation.
- **Compute Time**: Assembly can take hours to days for large datasets. Use `--CPU` to parallelize across multiple cores.
- **Input Quality**: Poor quality reads can affect assembly. Pre-process reads with Trimmomatic or Fastp before assembly.
- **Strand-Specific Data**: For strand-specific RNA-seq, use `--SS_lib_type` flag (RF or FR) to improve accuracy.
- **Output Size**: Assembly outputs can be large. Compress output files if storage is limited.
- **Abundance Estimation**: Use RSEM or Salmon for accurate transcript quantification after assembly.

## Examples

### Display help
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information.

### Basic paired-end assembly
**Args:** `--seqType fq --left reads_1.fastq --right reads_2.fastq --output trinity_out --CPU 8 --max_memory 32G`
**Explanation:** Assembles paired-end RNA-Seq reads using 8 CPUs and 32GB memory.

### Single-end assembly
**Args:** `--seqType fq --single reads.fastq --output trinity_out --CPU 12 --max_memory 48G`
**Explanation:** Assembles single-end reads with 12 CPUs and 48GB memory.

### Strand-specific assembly
**Args:** `--seqType fq --left reads_1.fastq --right reads_2.fastq --SS_lib_type RF --output trinity_out --CPU 8`
**Explanation:** Assembles strand-specific RNA-Seq data where reads are in RF orientation (second strand).

### Assembly with quality trimming
**Args:** `--seqType fq --left reads_1.fastq --right reads_2.fastq --output trinity_out --trimmomatic --CPU 8`
**Explanation:** Runs Trimmomatic quality trimming before assembly to remove low-quality bases.

### Assembly with normalization
**Args:** `--seqType fq --left reads_1.fastq --right reads_2.fastq --output trinity_out --normalize_reads --CPU 8`
**Explanation:** Normalizes read coverage to reduce computational complexity for highly expressed transcripts.

### Generate assembly statistics
**Args:** `$TRINITY_HOME/util/TrinityStats.pl trinity_out/Trinity.fasta`
**Explanation:** Generates summary statistics (number of transcripts, N50, GC content) for the assembly.

### Quantify transcript abundance with RSEM
**Args:** `$TRINITY_HOME/util/align_and_estimate_abundance.pl --transcripts Trinity.fasta --seqType fq --left reads_1.fastq --right reads_2.fastq --est_method RSEM --output_dir rsem_out`
**Explanation:** Uses RSEM to estimate transcript-level abundances from the assembly.

### Differential expression analysis
**Args:** `$TRINITY_HOME/Analysis/DifferentialExpression/run_DE_analysis.pl --matrix rsem_out/RSEM.isoforms.results --samples_file samples.txt --method DESeq2`
**Explanation:** Performs differential expression analysis using DESeq2 on quantified transcript abundances.