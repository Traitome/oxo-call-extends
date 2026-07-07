---
name: a5-miseq
category: assembly
description: A5-miseq is a pipeline for assembling DNA sequence data generated on the Illumina sequencing platform, specifically designed for microbial genomes.
tags: [a5-miseq, assembly, illumina, microbial-genomics, dna-sequencing, genome-assembly]
author: oxo-call-community
source_url: "https://sourceforge.net/projects/ngopt"
---

## Concepts

- **Tool Overview**: a5-miseq (v20160825) is a fully automated pipeline for assembling microbial genomes from Illumina MiSeq data. It performs error correction, adapter trimming, contig assembly, scaffolding, and misassembly detection in a single run.
- **Core Function**: The pipeline runs in 5 stages: (1) Quality trimming and error correction, (2) Contig assembly using IDBA, (3) Scaffolding with paired-read/mate-pair information, (4) Misassembly detection and breaking, (5) Rescaffolding of broken contigs.
- **Input/Output**: Input is paired-end FASTQ files or a library file listing multiple libraries. Output includes contigs, final scaffolds (FASTA and FASTQ), quality values (QVL), and assembly statistics.
- **Installation**: `conda install -c bioconda a5-miseq`
- **Platform Support**: Linux (x86_64), requires Perl and Java
- **Threading**: Supports multi-threading via `--threads` option (default: 4)
- **Version**: Latest stable version is 20160825 (date-based versioning)

## Pitfalls

- **CRITICAL: Command Name**: The actual command is `a5_pipeline.pl`, not `a5-miseq`. When installed via conda, use `a5_pipeline.pl` directly.
- **Read Length Requirement**: A5-miseq works best with Illumina reads ≥80 nt. Shorter reads may produce poor results.
- **Genome Type Limitation**: Designed for homozygous haploid microbial genomes. Not suitable for metagenomes, heterozygous diploid, or polyploid organisms.
- **Quality Requirements**: Requires high-quality reads. Poor quality data (low base qualities before 60 nt) should be filtered before assembly.
- **Memory Requirements**: Requires significant memory (~4GB recommended), especially for larger genomes.

## Examples

### Basic paired-end assembly
**Args:** `read1.fastq read2.fastq my_assembly`
**Explanation:** Assembles paired-end Illumina reads into scaffolds. Output files will be prefixed with "my_assembly", including my_assembly.final.scaffolds.fasta.

### Specify number of threads
**Args:** `--threads=8 read1.fastq read2.fastq my_assembly`
**Explanation:** Uses 8 threads for faster processing. Threads improve performance in error correction and assembly stages.

### Run with a library file (multiple libraries)
**Args:** `libraries.txt my_assembly`
**Explanation:** Assembles using multiple libraries specified in a library file. The library file format requires columns: id, p1, p2, shuf, up, rc, ins, err.

### Run only specific pipeline stages
**Args:** `--begin=2 --end=4 read1.fastq read2.fastq my_assembly`
**Explanation:** Runs stages 2-4 only (skips quality trimming and final scaffolding). Useful for restarting failed runs or testing specific stages.

### Metagenome mode
**Args:** `--metagenome read1.fastq read2.fastq metagenome_assembly`
**Explanation:** Enables metagenome-specific processing. While A5-miseq is primarily designed for isolate genomes, this mode can help with metagenomic assembly.

### Debug mode for troubleshooting
**Args:** `--debug read1.fastq read2.fastq my_assembly`
**Explanation:** Runs in debug mode, producing additional log files for troubleshooting pipeline issues.

### Using preprocessed reads
**Args:** `--preprocessed cleaned_reads1.fastq cleaned_reads2.fastq my_assembly`
**Explanation:** Skips the initial quality trimming and error correction steps, assuming reads are already preprocessed. Useful when using custom preprocessing workflows.