---
name: ssdrippipeline
category: rna-seq
description: Useful tools for the analysis of ssDRIP-seq data.
tags: [ssdrippipeline, ssDRIP-seq, rna-seq, dna-damage]
author: oxo-call-community
source_url: "https://github.com/PEHGP/ssDripPipeline/wiki"
---

## Concepts

- **Tool Overview**: ssdrippipeline (v0.0.5) is a pipeline for analyzing single-strand DNA damage and repair sequencing (ssDRIP-seq) data.
- **Core Function**: Identifies DNA damage sites and repair patterns from high-throughput sequencing data.
- **Workflow Components**: Quality control → alignment → peak calling → damage site annotation → visualization.
- **Input/Output**: Input: FASTQ files from ssDRIP-seq experiment; Output: Damage site coordinates, coverage profiles, and analysis reports.
- **Damage Detection**: Uses unique molecular identifiers (UMIs) to reduce PCR duplicates and improve accuracy.
- **Installation**: `conda install -c bioconda ssdrippipeline` or download from GitHub repository.

## Pitfalls

- **UMI Quality**: Low-quality UMIs can lead to incorrect deduplication and false positive damage calls.
- **Input Quality**: Poor sequencing quality affects damage site identification accuracy.
- **Reference Genome**: Must use the correct reference genome matching the experimental organism.
- **Control Samples**: Without proper input controls, distinguishing real damage from background is difficult.
- **PCR Bias**: Amplification bias can skew damage site distribution.
- **Library Prep Artifacts**: Adapter dimers and chimeric reads may affect analysis.

## Examples

### Display help
**Args:** `ssdrippipeline --help`
**Explanation:** Shows available options and usage information.

### Basic ssDRIP-seq analysis
**Args:** `ssdrippipeline -i reads.fastq -o results/ -r reference.fasta`
**Explanation:** Run complete ssDRIP-seq analysis pipeline.

### With UMI processing
**Args:** `ssdrippipeline -i reads.fastq -o results/ -r reference.fasta --umi`
**Explanation:** Enable UMI-based deduplication for improved accuracy.

### With control sample
**Args:** `ssdrippipeline -i treated.fastq -c control.fastq -o results/ -r reference.fasta`
**Explanation:** Compare treated sample against control for differential damage analysis.

### Peak calling only
**Args:** `ssdrippipeline -i aligned.bam -o peaks.bed --peak-only`
**Explanation:** Run only peak calling on pre-aligned BAM file.

### Generate visualization
**Args:** `ssdrippipeline -i reads.fastq -o results/ -r reference.fasta --visualize`
**Explanation:** Generate coverage plots and damage site visualizations.

### Quality filtering
**Args:** `ssdrippipeline -i reads.fastq -o results/ -r reference.fasta -q 20`
**Explanation:** Apply quality filtering with minimum Phred score.
