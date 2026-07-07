---
name: ciriquant
category: expression
description: Circular RNA quantification pipeline
tags: [ciriquant, circrna, rna-seq, bioinformatics]
author: oxo-call-community
source_url: "https://ciri-cookbook.readthedocs.io/en/latest/CIRIquant_0_home.html"
---

## Concepts

- **Tool Overview**: CIRIquant is a comprehensive pipeline for quantifying circular RNA expression levels from RNA-seq data.
- **Core Function**: Quantifies circRNA expression using back-splice junction reads and provides expression estimates.
- **Algorithm**: Uses statistical methods to estimate circRNA expression levels from sequencing data.
- **Input**: RNA-seq reads (FASTQ) and reference genome/transcriptome.
- **Output**: circRNA expression levels in various formats (TPM, FPKM, raw counts).
- **Application**: Differential expression analysis, circRNA profiling, and transcriptomics studies.
- **Installation**: Install via bioconda: `conda install -c bioconda ciriquant`

## Pitfalls

- **Data Quality**: Requires high-quality RNA-seq data for accurate quantification.
- **Mapping Quality**: Depends on accurate read mapping to reference genome.
- **Expression Levels**: May underestimate lowly expressed circRNAs.
- **Reference Annotation**: Needs well-annotated reference for optimal results.
- **Computational Resources**: May require significant memory for large datasets.

## Examples

### Quantify circRNA expression
**Args:** `ciriquant -i reads.fastq -g genome.fasta -o expression.txt`
**Explanation:** Quantifies circRNA expression levels from RNA-seq data.

### With annotation
**Args:** `ciriquant -i reads.fastq -g genome.fasta -a annotation.gtf -o expression.txt`
**Explanation:** Uses gene annotation for improved quantification.

### Multiple samples
**Args:** `ciriquant -i sample1.fastq,sample2.fastq -g genome.fasta -o expression_matrix.txt`
**Explanation:** Quantifies expression across multiple samples.

### Display help
**Args:** `ciriquant --help`
**Explanation:** Shows all available options and usage information.