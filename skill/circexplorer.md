---
name: circexplorer
category: expression
description: Combined strategy to identify circular RNAs (circRNAs and ciRNAs)
tags: [circexplorer, circrna, circular-rna, rna-seq, bioinformatics]
author: oxo-call-community
source_url: "https://github.com/YangLab/CIRCexplorer"
---

## Concepts

- **Tool Overview**: CIRCexplorer is a computational pipeline for identifying circular RNAs (circRNAs and ciRNAs) from RNA-seq data.
- **Core Function**: Detects back-spliced junctions and identifies circular RNA transcripts using a combined strategy.
- **Algorithm**: Integrates multiple detection methods including TopHat-Fusion mapping and splice junction analysis.
- **Input**: RNA-seq reads and annotated genome.
- **Output**: List of identified circRNAs with genomic coordinates.
- **Application**: Circular RNA discovery and characterization in transcriptomics studies.
- **Installation**: Install via bioconda: `conda install -c bioconda circexplorer`

## Pitfalls

- **Alignment Requirements**: Requires fusion-aware aligners like TopHat-Fusion.
- **Reference Annotation**: Needs well-annotated reference genome for accurate detection.
- **Expression Levels**: circRNAs are often lowly expressed; requires deep sequencing.
- **False Positives**: May detect false positives from trans-splicing events.
- **Strand Specificity**: Strand information critical for accurate annotation.

## Examples

### Identify circRNAs
**Args:** `CIRCexplorer -f reads.fastq -g genome.fa -a annotation.gtf -o circRNAs.txt`
**Explanation:** Identifies circRNAs from RNA-seq data using reference annotation.

### With TopHat-Fusion
**Args:** `CIRCexplorer --tophat-fusion -f reads.fastq -o output_dir`
**Explanation:** Uses TopHat-Fusion for fusion junction detection.

### Filter by read count
**Args:** `CIRCexplorer -f reads.fastq -g genome.fa -c 2 -o filtered.txt`
**Explanation:** Filters circRNAs with minimum 2 supporting reads.

### Display help
**Args:** `CIRCexplorer --help`
**Explanation:** Shows all available options and usage information.