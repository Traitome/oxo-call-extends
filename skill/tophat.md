---
name: tophat
category: alignment
description: TopHat - Fast splice junction mapper for RNA-seq reads.
tags: [tophat, rna-seq, splice-junction, alignment, mapping]
author: oxo-call-community
source_url: "https://ccb.jhu.edu/software/tophat/index.shtml"
---

## Concepts

- **Tool Overview**: TopHat - A fast splice junction mapper for RNA-seq reads that aligns reads to a reference genome.
- **Core Function**: Aligns RNA-seq reads while identifying splice junctions and exon-exon boundaries.
- **Input**: RNA-seq reads (FASTQ), reference genome (FASTA).
- **Output**: Aligned reads (BAM), splice junction annotations.
- **Installation**: `conda install -c bioconda tophat`
- **Use Case**: RNA-seq alignment, transcriptome analysis, gene expression quantification.

## Pitfalls

- **Deprecated**: TopHat is no longer actively maintained; consider using HISAT2 or STAR.
- **Memory**: Requires significant memory for large genomes.

## Examples

### Align RNA-seq reads
**Args:** `tophat -o aligned/ genome.fasta reads_1.fastq reads_2.fastq`
**Explanation:** Align paired-end RNA-seq reads to reference genome.

### With known transcripts
**Args:** `tophat -G transcripts.gtf -o aligned/ genome.fasta reads.fastq`
**Explanation:** Use known transcript annotations to guide alignment.
