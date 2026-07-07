---
name: detonate
category: assembly
description: DETONATE - de novo transcriptome assembly evaluation toolkit with RSEM-EVAL and REF-EVAL.
tags: [detonate, assembly, transcriptome, evaluation, quality]
author: oxo-call-community
source_url: "http://deweylab.biostat.wisc.edu/detonate/"
---

## Concepts

- **Tool Overview**: detonate (v1.11+) is a toolkit for evaluating de novo transcriptome assemblies. It provides two complementary evaluation methods: RSEM-EVAL (reference-free) and REF-EVAL (reference-based).
- **Core Function**: Assesses the quality of transcriptome assemblies by comparing predicted expression levels against observed read data, providing quantitative quality metrics.
- **Input/Output**: Input: Transcriptome assembly (FASTA), RNA-seq reads (FASTQ), optional reference annotation. Output: Quality scores, assembly ranking, diagnostic statistics.
- **Algorithm**: RSEM-EVAL uses expectation-maximization to estimate transcript abundances and compares them with assembly predictions. REF-EVAL compares against a known reference transcriptome.
- **Key Features**: Reference-free evaluation, reference-based evaluation, quality scoring, assembly comparison, supports paired-end reads, strand-specific data.
- **Installation**: `conda install -c bioconda detonate`

## Pitfalls

- **Input Requirements**: Requires high-quality transcriptome assembly and properly aligned reads.
- **Memory Usage**: May require significant memory for large transcriptomes.
- **Computational Time**: Evaluation can be time-consuming for large datasets.
- **Reference Dependence**: REF-EVAL requires a reference annotation which may not always be available.
- **Strand Specificity**: Must specify strand-specific protocol if applicable.

## Examples

### Evaluate assembly with RSEM-EVAL
**Args:** `rsem-eval-calculate-score --paired reads_1.fq reads_2.fq assembly.fa sample_name`
**Explanation:** Evaluates transcriptome assembly quality using reference-free RSEM-EVAL method with paired-end reads.

### With strand-specific data
**Args:** `rsem-eval-calculate-score --paired reads_1.fq reads_2.fq assembly.fa sample_name --stranded`
**Explanation:** Specify strand-specific RNA-seq library preparation.

### Reference-based evaluation
**Args:** `ref-eval calculate-score --transcripts ref_transcripts.fa --genes ref_genes.gtf assembly.fa alignments.bam`
**Explanation:** Uses REF-EVAL to compare assembly against reference annotation.

### Generate evaluation plot
**Args:** `rsem-eval-plot-stats sample_name.genes.results plot.pdf`
**Explanation:** Generate visualization of evaluation statistics.

### Compare multiple assemblies
**Args:** `rsem-eval-compare-assemblies assembly1.stats assembly2.stats comparison.pdf`
**Explanation:** Compare quality metrics across multiple transcriptome assemblies.