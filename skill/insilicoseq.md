---
name: insilicoseq
category: sequencing
description: A sequencing simulator that generates realistic Illumina-like sequencing reads with pre-computed error models for HiSeq, MiSeq, NextSeq, and NovaSeq platforms.
tags: [insilicoseq, sequencing, simulator, Illumina]
author: oxo-call-community
source_url: "https://insilicoseq.readthedocs.io/en/latest/"
---

## Concepts

- **Sequencing Simulation**: InSilicoSeq generates synthetic sequencing reads that mimic real Illumina sequencing data, supporting metagenomics and amplicon sequencing modes.
- **Error Models**: Provides pre-computed error models for popular Illumina instruments (HiSeq, MiSeq, NextSeq, NovaSeq) and supports custom error model generation from BAM files.
- **Abundance Distributions**: Supports multiple abundance distributions including lognormal, uniform, halfnormal, exponential, and zero-inflated-lognormal.
- **Input Sources**: Can use local genome FASTA files, draft genomes, or download random genomes directly from NCBI (bacteria, viruses, archaea).
- **Output Formats**: Generates paired-end FASTQ files with optional gzip compression and abundance tracking files.

## Pitfalls

- **Model Compatibility**: Pre-computed error models are instrument-specific; using the wrong model for your data can produce unrealistic reads.
- **Genome Requirements**: The `--genomes` option expects complete genomes, while draft genomes should use `--draft` parameter.
- **Resource Usage**: Generating large read datasets can be memory-intensive; use `--cpus` to enable parallel processing.
- **Fragment Length**: For metagenomics mode, fragment length parameters may need adjustment based on library preparation.
- **Seed Reproducibility**: Without setting `--seed`, results are non-deterministic; use a fixed seed for reproducible simulations.

## Examples

### Generate MiSeq reads from genomes
**Args:** `iss generate --genomes SRS121011.fasta --model miseq --output miseq_reads --n_reads 1M`
**Explanation:** Generates 1 million paired-end MiSeq reads from the input genome file using the built-in MiSeq error model.

### Generate HiSeq reads with multiple CPUs
**Args:** `iss generate --cpus 8 --genomes genome.fasta --model hiseq --output hiseq_reads`
**Explanation:** Uses 8 CPUs to accelerate read generation with the HiSeq error model.

### Download genomes from NCBI and simulate
**Args:** `iss generate --ncbi bacteria viruses --n_genomes_ncbi 10 4 --model novaseq --output ncbi_reads`
**Explanation:** Downloads 10 bacterial and 4 viral genomes from NCBI, then generates NovaSeq reads from them.

### Generate amplicon reads
**Args:** `iss generate --genomes amplicons.fasta --readcount_file counts.txt --sequence_type amplicon --model nextseq --output amplicon_reads`
**Explanation:** Simulates amplicon sequencing reads using a read count file to specify abundances for each amplicon.

### Use custom error model
**Args:** `iss generate --genomes genome.fasta --model custom_model.npz --output custom_reads`
**Explanation:** Uses a user-generated error model file instead of built-in instrument models.

### Generate reads with GC bias
**Args:** `iss generate --genomes genome.fasta --model miseq --gc_bias --compress --output biased_reads`
**Explanation:** Introduces GC bias into simulated reads and compresses output FASTQ files.