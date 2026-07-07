---
name: fetchmgs
category: metagenomics
description: "FetchMGs extracts the 40 marker genes from genomes and metagenomes in an easy and accurate manner."
tags: [fetchmgs, metagenomics, marker-genes, phylogenetics, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/motu-tool/FetchMGs"
---

## Concepts

- **Tool Overview**: FetchMGs is a tool for extracting the 40 universal marker genes from genomes and metagenomes for phylogenetic analysis.
- **Core Function**: Extracts conserved marker genes from genomic and metagenomic sequences.
- **Input/Output**: Input: Genome or metagenome sequences. Output: Marker gene sequences, annotations.
- **Algorithm**: Uses HMM models for marker gene identification.
- **Key Features**: 40 marker genes, phylogenetic analysis, metagenome support, genome comparison, automatic annotation.
- **Installation**: `conda install -c bioconda fetchmgs`

## Pitfalls

- **Sequence Quality**: Requires high-quality sequence data.
- **Gene Detection**: Some organisms may lack certain marker genes.
- **Memory Usage**: Large datasets may require significant memory.
- **Annotation Accuracy**: Results depend on HMM model quality.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic marker gene extraction
**Args:** `fetchmgs -i genome.fasta -o marker_genes/`
**Explanation:** Extracts marker genes from genome.

### Metagenome analysis
**Args:** `fetchmgs -i metagenome.fasta -o results/ --metagenome`
**Explanation:** Analyzes metagenome data.

### Batch processing
**Args:** `fetchmgs -i genomes/ -o results/ --batch`
**Explanation:** Processes multiple genomes.

### Specify markers
**Args:** `fetchmgs -i genome.fasta -o results/ --markers ribosome`
**Explanation:** Extracts specific marker types.

### Output format
**Args:** `fetchmgs -i genome.fasta -o results/ -f fasta`
**Explanation:** Sets output format.