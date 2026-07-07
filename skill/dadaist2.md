---
name: dadaist2
category: utility
description: Command line wrapper to run DADA2 on paired-end reads
tags: [dadaist2, utility, DADA2, amplicon-sequencing, bioinformatics]
author: oxo-call-community
source_url: "https://quadram-institute-bioscience.github.io/dadaist2"
---

## Concepts

- **Tool Overview**: dadaist2 (v1.3.1+) is a command-line wrapper for running DADA2 on paired-end sequencing reads, with additional tools for visualization and ecological analysis.
- **Core Function**: Performs amplicon sequence variant (ASV) inference using DADA2 algorithm.
- **Input/Output**: Input: Paired-end FASTQ reads. Output: ASV table, taxonomy assignments, visualization reports.
- **Algorithm**: Uses DADA2's error modeling and sequence inference algorithm.
- **Key Features**: Complete amplicon analysis pipeline, quality filtering, taxonomy assignment, diversity analysis.
- **Installation**: `conda install -c bioconda dadaist2`

## Pitfalls

- **Input Requirements**: Requires properly paired FASTQ files.
- **Reference Database**: Requires appropriate reference database for taxonomy assignment.
- **Quality Thresholds**: Adjust quality filtering parameters based on data quality.
- **Memory Usage**: Large datasets may require significant memory.
- **Runtime**: Analysis can be time-consuming for large datasets.

## Examples

### Run DADA2 pipeline
**Args:** `dadaist2 --input reads/ --output results/ --ref silva_db.fasta`
**Explanation:** Run complete DADA2 pipeline on paired-end reads with Silva reference.

### Skip taxonomy assignment
**Args:** `dadaist2 --input reads/ --output results/ --notax`
**Explanation:** Run DADA2 without taxonomy assignment.

### Generate visualization
**Args:** `dadaist2 --input reads/ --output results/ --ref silva_db.fasta --visualize`
**Explanation:** Run pipeline and generate visualization reports.
