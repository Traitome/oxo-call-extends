---
name: shigeifinder
category: assembly
description: shigeifinder - Shigella and EIEC serotyping tool
tags: ["shigeifinder", "assembly", "serotyping", "Shigella"]
author: oxo-call-community
source_url: "https://github.com/LanLab/ShigEiFinder"
---

## Concepts

- **Tool Overview**: shigeifinder (v1.3.5) performs cluster-informed Shigella and EIEC serotyping.
- **Core Function**: Identifies Shigella and EIEC serotypes from sequencing data.
- **Algorithm**: Uses clustering approach for serotype prediction.
- **Input/Output**: Accepts FASTQ reads or assemblies and produces serotype predictions.
- **Serotyping**: Focuses on Shigella and EIEC identification.
- **Applications**: Clinical microbiology, epidemiology, and pathogen detection.

## Pitfalls

- **Memory Usage**: High memory requirements for large datasets.
- **Input Format**: Requires correct input format (FASTQ or FASTA).
- **Parameter Tuning**: Requires careful adjustment for optimal results.
- **Version Compatibility**: Different versions may have breaking changes.
- **Documentation**: Some features have limited documentation.
- **Database Updates**: Requires up-to-date database.

## Examples

### Run serotyping
**Args:** `shigeifinder -i reads.fastq -o results/`
**Explanation:** `-i` input reads; `-o` output directory.

### From assembly
**Args:** `shigeifinder -i assembly.fasta -a -o results/`
**Explanation:** `-a` indicates input is assembly.

### Verbose logging
**Args:** `shigeifinder -v -i reads.fastq -o results/`
**Explanation:** `-v` enables verbose output for debugging.

### Help command
**Args:** `shigeifinder --help`
**Explanation:** Shows available commands and options.

### Version check
**Args:** `shigeifinder --version`
**Explanation:** Shows current version.

### Paired-end
**Args:** `shigeifinder -1 reads_1.fastq -2 reads_2.fastq -o results/`
**Explanation:** `-1/-2` paired-end reads.

### Custom database
**Args:** `shigeifinder -i reads.fastq -d custom_db -o results/`
**Explanation:** `-d` custom database directory.