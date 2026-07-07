---
name: shortstack
category: expression
description: ShortStack - Comprehensive annotation and quantification of small RNA genes
tags: ["shortstack", "expression", "small-RNA", "annotation"]
author: oxo-call-community
source_url: "https://github.com/MikeAxtell/ShortStack"
---

## Concepts

- **Tool Overview**: ShortStack (v4.1.2) is a comprehensive tool for small RNA gene annotation and quantification.
- **Core Function**: Identifies and quantifies small RNA loci from sequencing data.
- **Algorithm**: Uses alignment-based approach with clustering for small RNA identification.
- **Input/Output**: Accepts BAM/FASTQ reads and produces annotation GTF and expression tables.
- **Small RNA Analysis**: Specialized for miRNA, siRNA, and other small RNA types.
- **Applications**: Plant and animal small RNA research, gene regulation studies.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Genome Indexing**: Requires pre-built genome index.
- **Parameter Tuning**: Requires careful adjustment for different species.
- **Input Quality**: Results depend on sequencing data quality.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some advanced features have limited documentation.

## Examples

### Annotate small RNA genes
**Args:** `shortstack --reads reads.fastq --genome genome.fasta --outdir output/`
**Explanation:** Basic small RNA annotation and quantification.

### With BAM input
**Args:** `shortstack --bam alignments.bam --genome genome.fasta --outdir output/`
**Explanation:** Use pre-aligned BAM file.

### With annotation
**Args:** `shortstack --reads reads.fastq --genome genome.fasta --annotation genes.gtf --outdir output/`
**Explanation:** `-annotation` provides known gene models.

### Help command
**Args:** `shortstack --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shortstack --version`
**Explanation:** Shows current version.

### Threaded mode
**Args:** `shortstack --reads reads.fastq --genome genome.fasta --threads 8 --outdir output/`
**Explanation:** `--threads 8` uses 8 threads.

### Minimal mode
**Args:** `shortstack --reads reads.fastq --genome genome.fasta --minimal --outdir output/`
**Explanation:** `--minimal` produces minimal output.
