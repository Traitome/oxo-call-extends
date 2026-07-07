---
name: transindel
category: analysis
description: TransIndel - Tool for analyzing indels in transcript sequences.
tags: [transindel, indel, variant-calling, rna-seq, transcriptome]
author: oxo-call-community
source_url: "https://github.com/compbio/transindel"
---

## Concepts

- **Tool Overview**: TransIndel - A tool for detecting and analyzing insertions and deletions in transcript sequences.
- **Core Function**: Identifies indel variants from RNA-seq data and characterizes their impact.
- **Input**: RNA-seq alignments (BAM), reference genome, gene annotations.
- **Output**: Indel calls, functional impact predictions, variant statistics.
- **Installation**: `pip install transindel` or `conda install -c bioconda transindel`
- **Use Case**: Variant analysis, RNA editing, transcriptome variation.

## Pitfalls

- **Alignment Quality**: Indel detection depends on alignment quality.
- **False Positives**: May produce false positive indel calls.

## Examples

### Detect indels
**Args:** `transindel -i rnaseq.bam -r genome.fasta -o indels.vcf`
**Explanation:** Detect indel variants from RNA-seq data.

### Functional impact
**Args:** `transindel impact -i indels.vcf -a genes.gtf -o impact/`
**Explanation:** Predict functional impact of indel variants.
