---
name: circminer
category: expression
description: Sensitive and fast computational tool for detecting circular RNAs (circRNAs) from RNA-Seq data
tags: [circminer, circrna, rna-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/vpc-ccg/circminer"
---

## Concepts

- **Tool Overview**: CircMiner is a sensitive and fast computational tool for detecting circular RNAs (circRNAs) from RNA-Seq data.
- **Core Function**: Identifies circRNAs by detecting back-spliced junctions in RNA-seq reads.
- **Algorithm**: Uses splice junction analysis and read mapping to detect circRNA candidates efficiently.
- **Input**: RNA-seq reads (FASTQ) and reference genome/transcriptome.
- **Output**: List of detected circRNAs with genomic coordinates and supporting evidence.
- **Application**: Circular RNA discovery and expression analysis in transcriptomics.
- **Installation**: Install via bioconda: `conda install -c bioconda circminer`

## Pitfalls

- **Mapping Quality**: Requires accurate read mapping for reliable detection.
- **Expression Levels**: May miss lowly expressed circRNAs.
- **Reference Annotation**: Needs well-annotated reference for accurate classification.
- **False Positives**: May detect false circRNAs from trans-splicing events.
- **Computational Resources**: May require significant memory for large datasets.

## Examples

### Detect circRNAs
**Args:** `circminer -i reads.fastq -g genome.fasta -o circRNAs.txt`
**Explanation:** Detects circular RNAs from RNA-seq data.

### With annotation
**Args:** `circminer -i reads.fastq -g genome.fasta -a annotation.gtf -o results.txt`
**Explanation:** Uses gene annotation for circRNA classification.

### Quantify expression
**Args:** `circminer -i reads.fastq -g genome.fasta --quantify -o expression.txt`
**Explanation:** Detects and quantifies circRNA expression levels.

### Display help
**Args:** `circminer --help`
**Explanation:** Shows all available options and usage information.