---
name: ciri-full
category: expression
description: Full-length circRNA reconstruction and quantification using BSJ and reverse overlap features
tags: [ciri-full, circrna, rna-seq, bioinformatics]
author: oxo-call-community
source_url: "https://ciri-cookbook.readthedocs.io/en/latest/CIRI-full.html"
---

## Concepts

- **Tool Overview**: CIRI-full is a tool for full-length circRNA reconstruction and quantification using back-splice junction (BSJ) and reverse overlap (RO) features.
- **Core Function**: Reconstructs full-length circRNA sequences and quantifies their expression levels from RNA-seq data.
- **Algorithm**: Uses both BSJ reads and reverse overlap information to assemble complete circRNA sequences.
- **Input**: RNA-seq reads (FASTQ) and reference genome/transcriptome.
- **Output**: Full-length circRNA sequences and expression quantification.
- **Application**: Circular RNA characterization, expression profiling, and functional analysis.
- **Installation**: Install via bioconda: `conda install -c bioconda ciri-full`

## Pitfalls

- **Data Quality**: Requires high-quality RNA-seq data for accurate reconstruction.
- **Computational Resources**: May require significant memory for large datasets.
- **Reference Annotation**: Needs well-annotated reference for optimal results.
- **Expression Levels**: May miss lowly expressed circRNAs.
- **False Positives**: May reconstruct false circRNAs from technical artifacts.

## Examples

### Reconstruct full-length circRNAs
**Args:** `ciri-full -i reads.fastq -g genome.fasta -o circRNAs.fasta`
**Explanation:** Reconstructs full-length circRNA sequences from RNA-seq data.

### With quantification
**Args:** `ciri-full -i reads.fastq -g genome.fasta --quantify -o results.txt`
**Explanation:** Reconstructs and quantifies circRNA expression.

### Using annotation
**Args:** `ciri-full -i reads.fastq -g genome.fasta -a annotation.gtf -o circRNAs.fasta`
**Explanation:** Uses gene annotation to improve reconstruction.

### Display help
**Args:** `ciri-full --help`
**Explanation:** Shows all available options and usage information.