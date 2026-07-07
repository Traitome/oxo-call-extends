---
name: ctseq
category: epigenomics
description: ctSeq is a pipeline to analyze methylation patch PCR data
tags: [ctseq, epigenomics, methylation, PCR, bisulfite-seq]
author: oxo-call-community
source_url: "https://github.com/ryanhmiller/ctseq"
---

## Concepts

- **Tool Overview**: ctseq (v0.0.2+) is a pipeline for analyzing methylation patch PCR data to study DNA methylation patterns.
- **Core Function**: Processes bisulfite sequencing data from methylation patch PCR experiments to quantify methylation levels.
- **Input/Output**: Input: FASTQ reads, reference sequences. Output: Methylation calls, coverage statistics, visualization.
- **Algorithm**: Uses Bismark for alignment and methylation calling, with custom post-processing for patch-specific analysis.
- **Key Features**: Handles both single-end and paired-end data, provides strand-specific methylation calls, generates summary reports.
- **Installation**: `conda install -c bioconda ctseq`

## Pitfalls

- **Bisulfite Conversion**: Requires properly converted bisulfite sequencing data; unconverted reads affect accuracy.
- **Reference Preparation**: Reference genome must be bisulfite-converted before alignment; use `bismark_genome_preparation`.
- **PCR Bias**: Methylation patch PCR may introduce bias; include appropriate controls.
- **Quality Trimming**: Low-quality bases can affect methylation calls; pre-process reads.
- **Output Files**: Generates multiple output files; organize results in dedicated directory.

## Examples

### Run ctSeq pipeline
**Args:** `ctseq -i reads.fastq -r reference.fasta -o results/ --threads 8`
**Explanation:** Process methylation patch PCR data with 8 threads.

### Analyze paired-end data
**Args:** `ctseq -1 reads_R1.fastq -2 reads_R2.fastq -r reference.fasta -o pe_results/`
**Explanation:** Analyze paired-end bisulfite sequencing data.

### Generate methylation report
**Args:** `ctseq -i reads.fastq -r reference.fasta -o results/ --report`
**Explanation:** Generate comprehensive methylation analysis report.
