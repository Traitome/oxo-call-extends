---
name: ryuto
category: transcriptomics
description: Network-Flow based Transcriptome Reconstruction
tags: ["ryuto", "transcriptomics", "RNA-seq", "transcript reconstruction", "network flow"]
author: oxo-call-community
source_url: "https://github.com/studla/RYUTO/"
---

## Concepts

- **Tool Overview**: RYUTO (v1.6.3) is a network-flow based transcriptome reconstruction tool that integrates RNA-seq data with gene annotation to identify expressed transcripts and quantify their abundances.
- **Core Function**: Uses network flow algorithms to reconstruct transcript isoforms from RNA-seq reads, considering both annotated and novel transcripts.
- **Algorithm**: Implements a maximum flow/minimum cut algorithm to model transcript reconstruction as a flow network problem, optimizing for parsimony and read support.
- **Input Format**: RNA-seq reads (FASTQ/BAM), gene annotation (GTF/GFF), optional reference genome (FASTA).
- **Output Format**: Reconstructed transcripts in GTF format, expression quantification estimates, visualization of transcript structures.
- **Use Case**: Transcriptome assembly, isoform discovery, differential expression analysis, alternative splicing analysis.

## Pitfalls

- **Annotation dependency**: Performance depends on the quality of input gene annotations.
- **Computational complexity**: Network flow algorithms can be computationally intensive for large datasets.
- **Memory requirements**: Large genomes require significant memory for graph construction.
- **Sensitivity to parameters**: Flow network parameters may need tuning for different datasets.
- **Novel transcript discovery**: May miss rare or low-expression transcripts.
- **Read coverage requirements**: Requires sufficient read coverage for reliable transcript reconstruction.

## Examples

### Basic transcript reconstruction
**Args:** `ryuto -i reads.bam -g genes.gtf -o transcripts.gtf`
**Explanation:** `-i` input BAM with aligned reads; `-g` gene annotation; `-o` output GTF with reconstructed transcripts.

### With reference genome
**Args:** `ryuto -i reads.bam -g genes.gtf -r reference.fasta -o transcripts.gtf`
**Explanation:** `-r` reference genome for splice junction validation.

### Include novel transcripts
**Args:** `ryuto -i reads.bam -g genes.gtf -o transcripts.gtf --novel`
**Explanation:** `--novel` enables discovery of novel transcript isoforms.

### Quantify expression
**Args:** `ryuto -i reads.bam -g genes.gtf -o transcripts.gtf --quant`
**Explanation:** `--quant` outputs expression quantification along with transcripts.

### Threaded processing
**Args:** `ryuto -i reads.bam -g genes.gtf -o transcripts.gtf -t 8`
**Explanation:** `-t` number of threads for parallel processing.

### Filter by expression
**Args:** `ryuto -i reads.bam -g genes.gtf -o transcripts.gtf -m 1.0`
**Explanation:** `-m` minimum expression threshold (FPKM).

### Output visualization
**Args:** `ryuto -i reads.bam -g genes.gtf -o transcripts.gtf --viz`
**Explanation:** `--viz` generates visualization of transcript structures.
