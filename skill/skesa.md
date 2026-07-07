---
name: skesa
category: assembly
description: SKESA - Strategic Kmer Extension for Scrupulous Assemblies
tags: ["skesa", "assembly", "genome", "sequence"]
author: oxo-call-community
source_url: "https://github.com/ncbi/SKESA/blob/skesa.2.4.0_saute.1.3.0_2/README.md"
---

## Concepts

- **Tool Overview**: SKESA (v2.5.1) is a genome assembler using k-mer extension.
- **Core Function**: Assembles sequencing reads into contigs/scaffolds.
- **Algorithm**: Uses strategic k-mer extension for assembly.
- **Input/Output**: Accepts FASTQ reads and produces FASTA assemblies.
- **Genome Assembly**: Specialized for bacterial and small eukaryotic genomes.
- **Applications**: Genome sequencing, metagenomics, sequence assembly.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Computational Resources**: May require significant compute resources.
- **k-mer Size**: Choosing appropriate k-mer size is critical.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Assemble reads
**Args:** `skesa --reads reads.fastq --contigs_out assembly.fasta`
**Explanation:** Assembles reads into contigs.

### Paired-end assembly
**Args:** `skesa --reads reads_1.fastq,reads_2.fastq --contigs_out assembly.fasta`
**Explanation:** Assembles paired-end reads.

### With k-mer size
**Args:** `skesa --reads reads.fastq --kmer 31 --contigs_out assembly.fasta`
**Explanation:** `--kmer 31` k-mer size.

### Help command
**Args:** `skesa --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `skesa --version`
**Explanation:** Shows current version.

### Verbose mode
**Args:** `skesa --verbose --reads reads.fastq --contigs_out assembly.fasta`
**Explanation:** `--verbose` verbose output.

### Threaded mode
**Args:** `skesa --threads 8 --reads reads.fastq --contigs_out assembly.fasta`
**Explanation:** `--threads 8` uses 8 threads.
