---
name: snvphyl-tools
category: phylogenetics
description: SNVPhyl - Pipeline for SNV-based phylogenomics of microbial genomes
tags: [snvphyl-tools, phylogenetics, microbial, snvs, pipeline]
author: oxo-call-community
source_url: "https://github.com/phac-nml/snvphyl-tools"
---

## Concepts

- **Tool Overview**: snvphyl-tools (v1.8.2) - A pipeline for microbial phylogenomics
- **Core Function**: Identifies SNVs and constructs phylogenetic trees from microbial genomes
- **Input/Output**: Accepts FASTQ/BAM files; outputs SNV matrix and phylogeny
- **Algorithm**: Integrates SNV calling, filtering, and tree construction
- **Installation**: `conda install -c bioconda snvphyl-tools`
- **Key Features**: SNV identification, phylogenetic tree, microbial analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted sequence files
- **Reference Genome**: Must use compatible reference genome
- **Filtering Parameters**: Filtering parameters affect SNV quality
- **Tree Method**: Choice of tree method affects phylogeny
- **Computation Time**: Large datasets can be slow to process
- **Memory Usage**: May require significant memory for large datasets

## Examples

### Display help
**Args:** `snvphyl --help`
**Explanation:** Shows available options and usage information.

### Basic pipeline run
**Args:** `snvphyl --input-dir reads/ --reference reference.fasta --output-dir results/`
**Explanation:** Run SNVPhyl pipeline on reads.

### With BAM input
**Args:** `snvphyl --bam-dir alignments/ --reference reference.fasta --output-dir results/`
**Explanation:** Run pipeline on BAM alignments.

### With filtering
**Args:** `snvphyl --input-dir reads/ --reference reference.fasta --output-dir results/ --min-coverage 10`
**Explanation:** Set minimum coverage filter.

### With phylogeny
**Args:** `snvphyl --input-dir reads/ --reference reference.fasta --output-dir results/ --phylogeny`
**Explanation:** Generate phylogenetic tree.

### With bootstrap
**Args:** `snvphyl --input-dir reads/ --reference reference.fasta --output-dir results/ --bootstrap 100`
**Explanation:** Generate tree with bootstrap support.

### Export SNV matrix
**Args:** `snvphyl --input-dir reads/ --reference reference.fasta --output-dir results/ --matrix`
**Explanation:** Export SNV matrix.

### Generate report
**Args:** `snvphyl --input-dir reads/ --reference reference.fasta --output-dir results/ --report`
**Explanation:** Generate pipeline report.