---
name: stecfinder
category: typing
description: Cluster informed Shigatoxin producing E. coli (STEC) serotyping tool.
tags: [stecfinder, stec, ecoli, serotyping]
author: oxo-call-community
source_url: "https://github.com/LanLab/STECFinder"
---

## Concepts

- **Tool Overview**: stecfinder (v1.1.2) is a tool for serotyping Shigatoxin-producing E. coli (STEC) from sequencing data.
- **Core Function**: Identifies STEC serotypes using cluster-informed approach based on O-antigen and H-antigen typing.
- **Algorithm**: Uses BLAST-based approach to detect serotype-specific genes and infer serotype from cluster patterns.
- **Input/Output**: Input: Illumina reads or genome assembly; Output: STEC serotype prediction with confidence scores.
- **Database**: Uses curated database of O-antigen and H-antigen gene sequences for typing.
- **Installation**: `conda install -c bioconda stecfinder` or download from GitHub.

## Pitfalls

- **Sequencing Quality**: Low-quality reads affect serotype calling accuracy.
- **Assembly Quality**: Poor assembly affects detection of serotype-specific genes.
- **Novel Serotypes**: May miss newly discovered STEC serotypes not in database.
- **Mixed Infections**: Multiple serotypes in sample produce ambiguous results.
- **Database Updates**: Outdated database may miss new serotypes.
- **Coverage Depth**: Insufficient coverage may miss serotype-specific genes.

## Examples

### Display help
**Args:** `stecfinder --help`
**Explanation:** Shows available options and usage information.

### Basic serotyping from reads
**Args:** `stecfinder -i reads.fastq -o results.txt`
**Explanation:** Serotype STEC from Illumina sequencing reads.

### With genome assembly
**Args:** `stecfinder -i assembly.fasta -o results.txt --assembly`
**Explanation:** Serotype from pre-assembled genome.

### Verbose output
**Args:** `stecfinder -i reads.fastq -o results.txt -v`
**Explanation:** Run with detailed logging including intermediate results.

### Output GFF format
**Args:** `stecfinder -i assembly.fasta -o results.gff --gff`
**Explanation:** Output results in GFF annotation format.

### Custom database
**Args:** `stecfinder -i reads.fastq -o results.txt -d custom_db/`
**Explanation:** Use custom serotype database.

### Quality filtering
**Args:** `stecfinder -i reads.fastq -o results.txt -q 20`
**Explanation:** Apply quality filter to reads before analysis.

### Batch processing
**Args:** `stecfinder -i sample1.fastq sample2.fastq -o results/`
**Explanation:** Process multiple samples together.

### Update database
**Args:** `stecfinder --update-db`
**Explanation:** Update STEC serotype database to latest version.
