---
name: abruijn
category: assembly
description: Long read assembly via A-Bruijn graph (deprecated, now Flye)
tags: [abruijn, assembly, long-read, de-bruijn, pacbio, nanopore, flye]
author: oxo-call-community
source_url: "https://github.com/fenderglass/Flye/"
---

## Concepts

- **Tool Overview**: ABruijn is the original name of what is now known as Flye, a de novo assembler for single-molecule sequencing reads (PacBio and Oxford Nanopore). The tool uses an A-Bruijn graph approach that handles higher error rates of long reads.
- **Renamed**: ABruijn version 2.1b was the final release under this name; development continues as Flye. The command name `abruijn` may still be available in some installations.
- **Core Function**: Assembles long reads into contigs using an A-Bruijn graph structure with built-in repeat analysis and polishing.
- **Input/Output**: Input is long reads (FASTA/FASTQ, gzipped supported); output is polished contigs (FASTA).
- **Installation**: Install via bioconda: `conda install -c bioconda abruijn` or use the newer Flye: `conda install -c bioconda flye`
- **Platform Support**: Linux (x86_64) and macOS (x86_64)
- **Long Read Optimized**: Designed specifically for error-prone long reads from PacBio and Oxford Nanopore.

## Pitfalls

- **Deprecated**: ABruijn is deprecated; new projects should use Flye instead. The `abruijn` command may not receive updates.
- **Read Type Required**: Must specify read type with `--pacbio-raw`, `--nano-raw`, or other read type flags - bare reads.fasta is not valid.
- **Genome Size Required**: The `-g/--genome-size` parameter must be provided for proper k-mer selection.
- **Long Read Only**: Not designed for short read assembly. Use other assemblers for Illumina data.
- **Memory Requirements**: Large assemblies may require significant RAM (human ONT assembly can use 400-500 GB).

## Examples

### Display help and version information
**Args:** `--help`
**Explanation:** Shows all available command-line options and usage information. For ABruijn 2.1b, this includes read type flags and output options.

### Basic PacBio raw read assembly
**Args:** `--pacbio-raw reads.fasta -g 5m -o assembly_output/ -t 4`
**Explanation:** Assembles PacBio raw reads from a 5 million base genome using 4 threads. The `-g` flag specifies genome size estimate for k-mer selection, and `-t` sets parallel threads.

### Oxford Nanopore assembly with custom overlap
**Args:** `--nano-raw nanopore_reads.fastq -g 3g -o results/ --min-ovlp 3000`
**Explanation:** Assembles Oxford Nanopore reads from a 3 gigabase genome with a minimum overlap of 3000bp. Higher min-overlap values reduce misassemblies but may fragment the assembly.

### Resume interrupted assembly
**Args:** `--pacbio-raw reads.fasta -g 100m -o assembly_output/ --resume`
**Explanation:** Resumes an assembly from where it was interrupted, preserving intermediate results in the output directory.

### Multiple input files assembly
**Args:** `--pacbio-raw read1.fasta read2.fasta read3.fasta -g 2.6g -o out_dir/ -t 16`
**Explanation:** Assembles multiple FASTQ/FASTA files simultaneously from a 2.6 gigabase genome using 16 threads for parallel processing.