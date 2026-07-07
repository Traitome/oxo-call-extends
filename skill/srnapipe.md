---
name: srnapipe
category: rna-seq
description: Pipeline for bioinformatic in-depth exploration of small RNA-seq data.
tags: [srnapipe, small-rna, rna-seq, pipeline]
author: oxo-call-community
source_url: "https://github.com/GReD-Clermont/sRNAPipe-cli"
---

## Concepts

- **Tool Overview**: srnapipe (v1.2.1) is a comprehensive pipeline for small RNA-seq data analysis, supporting quality control, mapping, annotation, and differential expression analysis.
- **Core Function**: Provides end-to-end analysis of small RNA sequencing data including miRNA, piRNA, and snoRNA identification and quantification.
- **Workflow Components**: Quality trimming → adapter removal → mapping to reference → annotation → expression profiling → differential analysis.
- **Input/Output**: Input: FASTQ files; Output: annotated small RNA counts, differential expression results, and visualization reports.
- **Annotation Databases**: Supports miRBase, piRNA clusters, and custom annotation databases for small RNA classification.
- **Installation**: `conda install -c bioconda srnapipe` or via GitHub repository with `pip install git+https://github.com/GReD-Clermont/sRNAPipe-cli.git`.

## Pitfalls

- **Adapter Contamination**: Unremoved adapters can cause incorrect mapping and false positive identifications.
- **Low Quality Reads**: Poor quality sequences may lead to misclassification of small RNA species.
- **Reference Genome Compatibility**: Ensure reference genome matches the organism being studied.
- **Database Outdated**: Using outdated miRBase versions may miss newly discovered miRNAs.
- **Strand-Specific Protocol**: Small RNA-seq is often strand-specific; incorrect strand handling affects results.
- **Memory Requirements**: Large datasets may require significant memory allocation for mapping and quantification steps.

## Examples

### Display help
**Args:** `srnapipe --help`
**Explanation:** Shows available options and usage information.

### Basic small RNA analysis
**Args:** `srnapipe -i reads.fastq -o results/ -r reference.fasta`
**Explanation:** Run complete small RNA-seq analysis pipeline with reference genome.

### With miRNA annotation
**Args:** `srnapipe -i reads.fastq -o results/ -r reference.fasta --miRBase miRBase_v22`
**Explanation:** Analyze small RNA data with specific miRBase annotation database.

### Paired-end analysis
**Args:** `srnapipe -i read1.fastq -i2 read2.fastq -o results/ -r reference.fasta`
**Explanation:** Process paired-end small RNA sequencing data.

### Quality control only
**Args:** `srnapipe -i reads.fastq -o qc_results/ --qc-only`
**Explanation:** Run only quality control steps without mapping.

### Differential expression analysis
**Args:** `srnapipe -i group1/ -i group2/ -o de_results/ -r reference.fasta --diff-exp`
**Explanation:** Perform differential expression analysis between two sample groups.

### With custom annotations
**Args:** `srnapipe -i reads.fastq -o results/ -r reference.fasta --custom-annot custom_db.gff`
**Explanation:** Include custom small RNA annotations in the analysis.
