---
name: shapemapper
category: formatting
description: shapemapper - SHAPE reactivity analysis for RNA structure
tags: ["shapemapper", "formatting", "RNA-structure", "SHAPE"]
author: oxo-call-community
source_url: "http://www.chem.unc.edu/rna/software.html"
---

## Concepts

- **Tool Overview**: shapemapper (v1.2) converts raw sequencing files into mutational profiles.
- **Core Function**: Creates SHAPE reactivity plots and provides diagnostic information.
- **Algorithm**: Processes sequencing data to infer RNA structure.
- **Input/Output**: Accepts sequencing files and produces reactivity profiles.
- **RNA Structure Analysis**: Focuses on SHAPE-based RNA structure probing.
- **Applications**: RNA structure determination, transcriptomics, and molecular biology.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Input Format**: Requires correct sequencing data format.
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.

## Examples

### Run ShapeMapper
**Args:** `ShapeMapper --target target.fasta --out results/`
**Explanation:** `--target` target sequence; `--out` output directory.

### With reads
**Args:** `ShapeMapper --target target.fasta --fastq reads.fastq --out results/`
**Explanation:** `--fastq` input FASTQ reads.

### Paired-end
**Args:** `ShapeMapper --target target.fasta --fastq1 reads_1.fastq --fastq2 reads_2.fastq --out results/`
**Explanation:** `--fastq1/--fastq2` paired-end reads.

### Verbose logging
**Args:** `ShapeMapper -v --target target.fasta --out results/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `ShapeMapper --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `ShapeMapper --version`
**Explanation:** Shows current version.

### With primer
**Args:** `ShapeMapper --target target.fasta --primer primer.fasta --fastq reads.fastq --out results/`
**Explanation:** `--primer` primer sequence.