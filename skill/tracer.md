---
name: tracer
category: analysis
description: Tracer - Tool for analyzing RNA-seq data for fusion transcripts.
tags: [tracer, fusion-transcripts, rna-seq, gene-fusion, cancer]
author: oxo-call-community
source_url: "https://github.com/compbio/tracer"
---

## Concepts

- **Tool Overview**: Tracer - A tool for detecting and analyzing fusion transcripts from RNA-seq data.
- **Core Function**: Identifies gene fusions and chimeric transcripts from sequencing data.
- **Input**: RNA-seq reads (FASTQ/BAM), reference genome, gene annotations.
- **Output**: Fusion transcript calls, breakpoint locations, supporting evidence.
- **Installation**: `pip install tracer` or `conda install -c bioconda tracer`
- **Use Case**: Cancer genomics, fusion gene detection, transcriptome analysis.

## Pitfalls

- **Coverage**: Requires sufficient coverage at fusion breakpoints.
- **False Positives**: May produce false positive fusion calls.

## Examples

### Detect fusions
**Args:** `tracer -i rnaseq.bam -o fusions/`
**Explanation:** Detect fusion transcripts from RNA-seq data.

### With annotations
**Args:** `tracer -i reads.fastq -g genome.fasta -a genes.gtf -o fusion_results/`
**Explanation:** Use gene annotations to improve fusion detection.
