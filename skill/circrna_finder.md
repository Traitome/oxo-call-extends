---
name: circrna_finder
category: expression
description: Pipeline to find circular RNAs from RNA-seq data
tags: [circrna_finder, circrna, rna-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/orzechoj/circRNA_finder"
---

## Concepts

- **Tool Overview**: circRNA_finder provides scripts for running a pipeline to find circular RNAs from RNA-seq data.
- **Core Function**: Identifies circRNAs by detecting back-spliced junctions and analyzing RNA-seq alignments.
- **Algorithm**: Uses splice junction mapping and filtering to detect circRNA candidates.
- **Input**: RNA-seq reads (FASTQ) and reference genome/transcriptome.
- **Output**: List of detected circRNAs with genomic coordinates.
- **Application**: Circular RNA discovery and characterization in transcriptomics studies.
- **Installation**: Install via bioconda: `conda install -c bioconda circrna_finder`

## Pitfalls

- **Data Quality**: Requires high-quality RNA-seq data for reliable detection.
- **Mapping Quality**: Depends on accurate read mapping to reference genome.
- **Expression Levels**: May miss lowly expressed circRNAs.
- **False Positives**: May detect false circRNAs from trans-splicing events.
- **Computational Resources**: May require significant memory for large datasets.

## Examples

### Run circRNA detection pipeline
**Args:** `circRNA_finder -i reads.fastq -g genome.fasta -o circRNAs.txt`
**Explanation:** Runs the complete pipeline to detect circular RNAs from RNA-seq data.

### With annotation
**Args:** `circRNA_finder -i reads.fastq -g genome.fasta -a annotation.gtf -o results.txt`
**Explanation:** Uses gene annotation for circRNA classification.

### Filter by read count
**Args:** `circRNA_finder -i reads.fastq -g genome.fasta -c 2 -o filtered.txt`
**Explanation:** Filters circRNAs with minimum 2 supporting reads.

### Display help
**Args:** `circRNA_finder --help`
**Explanation:** Shows all available options and usage information.