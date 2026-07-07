---
name: rsem
category: rna-seq
description: RSEM (RNA-Seq by Expectation Maximization) is a software package for estimating gene and isoform expression levels from RNA-Seq data with or without a reference genome.
tags: ["rsem", "rna-seq", "expression-quantification", "isoform", "expectation-maximization", "transcriptome"]
author: oxo-call-community
source_url: "https://deweylab.github.io/RSEM/"
---

## Concepts

- **Tool Overview**: RSEM (v1.3.3, Dewey Lab) is a widely used RNA-Seq quantification tool that estimates gene and isoform abundances using an expectation-maximization (EM) algorithm. It handles multi-mapping reads probabilistically and works with or without a reference genome.
- **Core Function**: Takes raw sequencing reads or aligned BAM files and produces expression estimates at both gene and transcript levels. Outputs include TPM, FPKM, raw counts, and 95% credibility intervals.
- **Algorithm**: Uses EM to assign ambiguous reads to transcripts based on their likelihood of originating from each possible transcript. Incorporates fragment length distribution and quality scores for improved accuracy.
- **Input Format**: FASTQ files (single-end or paired-end), or pre-aligned SAM/BAM/CRAM files. Requires a reference transcriptome index built with `rsem-prepare-reference`.
- **Output Format**: Tab-delimited files with gene and isoform expression estimates (`sample.genes.results`, `sample.isoforms.results`), visualization files (Wiggle, BAM), and simulation data.
- **Use Case**: Transcript quantification for differential expression analysis, isoform usage analysis, RNA-Seq experiment design optimization, and de novo transcriptome analysis when combined with assemblers like Trinity.

## Pitfalls

- **Requires reference preparation**: Must run `rsem-prepare-reference` before quantification. Index building is computationally intensive for large transcriptomes.
- **Strandedness matters**: Incorrect `--strandedness` setting leads to quantification errors. Use `--strandedness reverse` for Illumina TruSeq Stranded protocols.
- **Memory intensive for large datasets**: Full human transcriptome analysis may require ≥32GB RAM when using STAR aligner.
- **Indel handling limited**: RSEM filters out reads with indels when using internal alignment. Pre-align with STAR or HISAT2 for indel-aware quantification.
- **Output files are large**: Multiple output files generated per sample. Use `--no-bam-output` to skip BAM generation if not needed.
- **EM convergence issues**: Rare cases with highly similar transcripts may fail to converge. Adjust `--max-em-iterations` if warnings occur.

## Examples

### Prepare reference with STAR
**Args:** `rsem-prepare-reference --star -p 8 transcripts.fa reference_name`
**Explanation:** `--star` builds STAR-compatible index; `-p 8` uses 8 threads; `transcripts.fa` is input FASTA; `reference_name` is output prefix. Creates index files for alignment and quantification.

### Quantify paired-end reads with STAR
**Args:** `rsem-calculate-expression --star -p 8 --paired-end read1.fastq read2.fastq reference_name sample_name`
**Explanation:** `--star` uses STAR aligner; `--paired-end` indicates paired reads; outputs gene/isoform results to `sample_name.genes.results` and `sample_name.isoforms.results`.

### Quantify from pre-aligned BAM
**Args:** `rsem-calculate-expression --alignments -p 8 input.bam reference_name sample_name`
**Explanation:** `--alignments` specifies input is pre-aligned BAM/SAM/CRAM. Useful when alignments are generated separately or need re-quantification.

### Stranded RNA-Seq quantification
**Args:** `rsem-calculate-expression --star -p 8 --paired-end --strandedness reverse read1.fastq read2.fastq reference_name sample_name`
**Explanation:** `--strandedness reverse` for Illumina TruSeq Stranded mRNA libraries. Use `forward` for other stranded protocols, `none` for unstranded.

### Generate visualization tracks
**Args:** `rsem-calculate-expression --star -p 8 --paired-end --wiggle read1.fastq read2.fastq reference_name sample_name`
**Explanation:** `--wiggle` generates Wiggle format files for genome browser visualization. Tracks show read coverage at both transcript and genomic coordinates.

### Simulate RNA-Seq data
**Args:** `rsem-simulate-reads reference_name model sample_name -p 1000000`
**Explanation:** Simulates 1 million reads from the reference transcriptome using the specified expression model. Useful for testing quantification accuracy or benchmarking.

### Calculate expression with HISAT2
**Args:** `rsem-calculate-expression --hisat2 -p 8 --paired-end read1.fastq read2.fastq reference_name sample_name`
**Explanation:** `--hisat2` uses HISAT2 aligner instead of STAR. HISAT2 is more memory-efficient for large genomes but slightly slower.