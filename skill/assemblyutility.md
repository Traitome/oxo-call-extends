---
name: assemblyutility
category: assembly
description: AssemblyUtility - Utility tools for DBG2OLC genome assembler
tags: [assemblyutility, assembly, dbg2olc, utility, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/yechengxi/AssemblyUtility"
---

## Concepts

- **Tool Overview**: AssemblyUtility provides utility tools and helper scripts for the DBG2OLC genome assembler. Version 20160209.
- **Core Function**: Supports DBG2OLC assembly pipeline with preprocessing, postprocessing, and utility operations.
- **DBG2OLC Integration**: Works specifically with DBG2OLC assembler for hybrid assembly workflows.
- **Preprocessing**: Includes tools for read preparation and quality filtering before assembly.
- **Postprocessing**: Provides scripts for assembly polishing, scaffolding, and quality assessment.
- **Hybrid Assembly**: Supports combining short reads and long reads for improved assembly quality.
- **Input/Output**: Accepts sequencing reads (FASTQ) and assembly files (FASTA), outputs processed assemblies.
- **Installation**: `conda install -c bioconda assemblyutility` or install from GitHub.

## Pitfalls

- **DBG2OLC Dependency**: Designed specifically for DBG2OLC. May not work with other assemblers.
- **Version Compatibility**: Must match DBG2OLC version. Incompatible versions cause errors.
- **Input Requirements**: Specific input formats required by DBG2OLC must be followed.
- **Memory Requirements**: Assembly processes may require significant memory resources.
- **Long Read Support**: May require specific long read formats (PacBio, Nanopore).
- **Quality Control**: Poor quality reads significantly affect assembly results.

## Examples

### Display help
**Args:** `AssemblyUtility --help`
**Explanation:** Shows all available command-line options and usage information.

### Prepare reads for DBG2OLC
**Args:** `AssemblyUtility prepare --short-reads short.fastq --long-reads long.fastq --output prepared/`
**Explanation:** Preprocesses short and long reads for DBG2OLC assembly pipeline.

### Run DBG2OLC assembly
**Args:** `AssemblyUtility assemble --prepped-dir prepared/ --output assembly/ --kmer 63`
**Explanation:** Runs DBG2OLC assembly with specified k-mer size.

### Polish assembly
**Args:** `AssemblyUtility polish --assembly contigs.fasta --reads short.fastq --output polished.fasta`
**Explanation:** Polishes assembly using short reads for improved accuracy.

### Scaffold assembly
**Args:** `AssemblyUtility scaffold --assembly contigs.fasta --long-reads long.fastq --output scaffolded.fasta`
**Explanation:** Scaffolds contigs using long reads for improved contiguity.

### Quality assessment
**Args:** `AssemblyUtility qc --assembly contigs.fasta --reference ref.fasta --output qc_report.txt`
**Explanation:** Performs quality assessment of assembly against reference genome.

### Merge assemblies
**Args:** `AssemblyUtility merge --assemblies asm1.fasta asm2.fasta --output merged.fasta`
**Explanation:** Merges multiple assemblies into single consensus assembly.

### Extract contigs
**Args:** `AssemblyUtility extract --assembly contigs.fasta --min-length 1000 --output filtered.fasta`
**Explanation:** Extracts only contigs longer than specified minimum length.

### Generate assembly statistics
**Args:** `AssemblyUtility stats --assembly contigs.fasta --output stats.txt`
**Explanation:** Computes and outputs assembly statistics including N50 and contig count.