---
name: espresso
category: expression
description: "ESPRESSO (Error Statistics PRomoted Evaluator of Splice Site Options) processes long read RNA-seq data."
tags: [espresso, expression, RNA-seq, long-reads, splice-variants]
author: oxo-call-community
source_url: "https://github.com/Xinglab/espresso"
---

## Concepts

- **Tool Overview**: ESPRESSO is a computational tool for processing long-read RNA-seq data to accurately identify splice sites and splice variants.
- **Core Function**: Identifies splice junctions and alternative splicing events from long-read sequencing data, even with high error rates.
- **Input/Output**: Input: Long-read RNA-seq reads (FASTQ/BAM), reference genome (FASTA). Output: Splice junction calls, transcript isoforms, expression estimates.
- **Algorithm**: Uses error-aware mapping and statistical modeling to accurately identify splice sites despite sequencing errors in long reads.
- **Key Features**: Error-tolerant splice site detection, alternative splicing analysis, isoform reconstruction, expression quantification, support for PacBio/ONT data.
- **Installation**: `conda install -c bioconda espresso`

## Pitfalls

- **Read Quality**: Performance depends on long-read quality and error profiles.
- **Reference Genome**: Requires well-annotated reference genome.
- **Computation Resources**: Large datasets require significant computational resources.
- **Memory Usage**: May require substantial RAM for large transcriptomes.
- **Version Compatibility**: Options may vary between versions.

## Examples

### Basic splice site detection
**Args:** `espresso -i reads.fastq -r ref.fasta -o splice_sites.bed`
**Explanation:** Identifies splice sites from long-read RNA-seq data.

### Isoform reconstruction
**Args:** `espresso -i reads.fastq -r ref.fasta -o isoforms.fasta --isoforms`
**Explanation:** Reconstructs transcript isoforms from long reads.

### Expression quantification
**Args:** `espresso -i reads.fastq -r ref.fasta -o expression.txt --quantify`
**Explanation:** Quantifies expression levels of detected isoforms.

### With annotation
**Args:** `espresso -i reads.fastq -r ref.fasta -a genes.gtf -o results/`
**Explanation:** Uses gene annotation for improved splice site detection.

### Batch processing
**Args:** `espresso -i samples/ -r ref.fasta -o results/ --batch`
**Explanation:** Processes multiple samples in batch mode.