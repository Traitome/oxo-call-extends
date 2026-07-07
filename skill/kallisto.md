---
name: kallisto
category: expression
description: Quantifying abundances of transcripts from RNA-Seq data using pseudoalignment.
tags: [kallisto, expression, RNA-Seq, quantification, pseudoalignment]
author: oxo-call-community
source_url: "https://pachterlab.github.io/kallisto/manual.html"
---

## Concepts

- **Tool Overview**: kallisto (v0.52.0) - A fast RNA-Seq transcript quantification tool using pseudoalignment.
- **Pseudoalignment**: Maps reads to transcripts without full alignment.
- **Speed**: Designed for fast processing of large RNA-Seq datasets.
- **Abundance Estimation**: Estimates transcript-level expression abundances.
- **Bootstrap Support**: Provides confidence intervals via bootstrapping.
- **Compatibility**: Works with single-end and paired-end reads.

## Pitfalls

- **Reference Transcriptome**: Requires complete reference transcriptome.
- **Mapping Ambiguity**: Multi-mapping reads can affect accuracy.
- **Novel Transcripts**: Cannot detect novel transcripts.
- **Strand Specificity**: Requires proper handling for strand-specific data.
- **Version Compatibility**: Index format may change between versions.
- **Memory Usage**: Large indexes require significant memory.

## Examples

### Build index
**Args:** `kallisto index -i transcripts.idx transcripts.fasta`
**Explanation:** Builds kallisto index from transcript sequences.

### Quantify single-end
**Args:** `kallisto quant -i transcripts.idx -o output -b 100 reads.fastq`
**Explanation:** Quantifies single-end reads with 100 bootstrap samples.

### Quantify paired-end
**Args:** `kallisto quant -i transcripts.idx -o output -b 100 reads_1.fastq reads_2.fastq`
**Explanation:** Quantifies paired-end reads with bootstrapping.

### Strand-specific quantification
**Args:** `kallisto quant -i transcripts.idx -o output --stranded -b 100 reads.fastq`
**Explanation:** Handles strand-specific RNA-Seq data.

### Generate plain text output
**Args:** `kallisto quant -i transcripts.idx -o output --plaintext reads.fastq`
**Explanation:** Outputs results in plain text format.

### Merge bootstrap results
**Args:** `kallisto merge -o merged_abundance output1 output2 output3`
**Explanation:** Merges abundance estimates from multiple samples.