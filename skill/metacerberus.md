---
name: metacerberus
category: annotation
description: Versatile Functional Ontology Assignments for Metagenomes via Hidden Markov Model (HMM) searching with environmental focus of shotgun meta'omics data
tags: [metacerberus, annotation, metagenomics, HMM, functional-analysis]
author: oxo-call-community
source_url: "https://github.com/raw-lab/metacerberus"
---

## Concepts

- **Tool Overview**: MetaCerberus v1.4.0 is a comprehensive tool for functional annotation of metagenomic sequences using Hidden Markov Model (HMM) searching with a focus on environmental metagenomics.
- **Core Function**: Assigns functional ontology terms to metagenomic sequences through HMM-based searches against comprehensive protein databases.
- **Environmental Focus**: Optimized for environmental metagenomics data with specialized databases for environmental microbes and ecosystems.
- **Multi-omics Support**: Handles both metagenomic and metatranscriptomic data for functional analysis.
- **Input/Output**: Accepts FASTA-formatted nucleotide or protein sequences; outputs detailed functional annotations including ontology terms, EC numbers, and pathway assignments.
- **Integrated Workflow**: Includes preprocessing, annotation, and post-processing steps for complete functional analysis.

## Pitfalls

- **Database Completeness**: Annotation quality depends on database completeness and updates.
- **Computational Resources**: HMM searches can be computationally intensive for large datasets.
- **False Positives**: Low-quality sequences may produce false positive annotations.
- **Annotation Overlap**: Multiple ontology terms may map to the same sequence.
- **Memory Requirements**: Building and loading large HMM databases requires significant memory.
- **Runtime**: Complete annotation of large metagenomic datasets can be time-consuming.

## Examples

### Run complete annotation workflow
**Args:** `metacerberus -i metagenome.fasta -o annotations/`
**Explanation:** Runs the complete functional annotation workflow on input sequences.

### Annotate metatranscriptome
**Args:** `metacerberus -i transcripts.fasta -m metatranscriptome -o annotations/`
**Explanation:** Performs functional annotation on metatranscriptomic data.

### Specify output format
**Args:** `metacerberus -i sequences.fasta -o annotations.tsv -f tsv`
**Explanation:** Outputs annotations in tab-separated value format.

### Include pathway analysis
**Args:** `metacerberus -i sequences.fasta -o annotations/ --pathways`
**Explanation:** Includes pathway analysis in the annotation output.

### Run with verbose logging
**Args:** `metacerberus -i sequences.fasta -o annotations/ -v`
**Explanation:** Enables verbose logging for debugging and progress tracking.