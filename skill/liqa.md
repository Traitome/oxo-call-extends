---
name: liqa
category: expression
description: LIQA - Isoform-specific expression quantification using long-read RNA-seq
tags: [liqa, expression, isoform, RNA-seq, long-reads, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/WGLab/LIQA"
---

## Concepts

- **Isoform Quantification**: Quantifies isoform-specific expression levels
- **Long-read RNA-seq**: Optimized for long-read sequencing data
- **Splice Variants**: Identifies and quantifies splice variants
- **Transcript Assembly**: Assembles transcripts from long reads
- **Expression Estimation**: Estimates transcript expression levels
- **Alternative Splicing**: Analyzes alternative splicing events

## Pitfalls

- **Read Quality**: Poor quality reads affect quantification
- **Mapping Quality**: Requires accurate read mapping
- **Isoform Complexity**: Complex isoforms may be miscounted
- **Computational Time**: May be slow for large datasets
- **Memory Usage**: Memory-intensive for large transcriptomes
- **Parameter Tuning**: Requires careful parameter optimization

## Examples

### Quantify isoforms
**Args:** `liqa -i aligned.bam -g annotation.gtf -o expression.txt`
**Explanation:** Quantifies isoform expression from aligned reads.

### Long-read mode
**Args:** `liqa -i aligned.bam -g annotation.gtf -o expression.txt -l`
**Explanation:** Optimized for long-read sequencing data.

### Threads
**Args:** `liqa -i aligned.bam -g annotation.gtf -o expression.txt -p 8`
**Explanation:** Uses 8 threads for parallel processing.

### FPKM output
**Args:** `liqa -i aligned.bam -g annotation.gtf -o expression.txt -f`
**Explanation:** Outputs FPKM normalized expression values.

### Transcript assembly
**Args:** `liqa -i reads.fastq -g annotation.gtf -o transcripts.fasta -a`
**Explanation:** Assembles transcripts from long reads.

### Differential expression
**Args:** `liqa -i samples.txt -g annotation.gtf -o diff_expression.txt -d`
**Explanation:** Performs differential expression analysis.