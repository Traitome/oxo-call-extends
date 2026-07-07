---
name: circtools
category: utility
description: Circular RNA toolbox for circRNA analysis
tags: [circtools, circrna, rna-seq, bioinformatics]
author: oxo-call-community
source_url: "https://docs.circ.tools/en/latest"
---

## Concepts

- **Tool Overview**: circtools is a comprehensive circular RNA toolbox for the analysis and characterization of circRNAs from RNA-seq data.
- **Core Function**: Provides a suite of tools for circRNA detection, quantification, and functional analysis.
- **Features**: circRNA detection, back-splice junction analysis, expression quantification, and downstream functional analysis.
- **Input**: RNA-seq reads, alignment files, and genomic annotations.
- **Output**: circRNA candidates, expression levels, and functional annotations.
- **Application**: Circular RNA analysis, expression profiling, and functional characterization.
- **Installation**: Install via bioconda: `conda install -c bioconda circtools`

## Pitfalls

- **Data Quality**: Requires high-quality RNA-seq data for reliable detection.
- **Mapping Requirements**: May require specific aligners for optimal results.
- **Computational Resources**: May require significant memory for large datasets.
- **Annotation Dependencies**: Functional analysis requires gene annotation files.
- **False Positives**: May detect false circRNAs from technical artifacts.

## Examples

### Detect circRNAs
**Args:** `circtools detect -i reads.fastq -g genome.fasta -o circRNAs.txt`
**Explanation:** Detects circular RNAs from RNA-seq data.

### Quantify expression
**Args:** `circtools quantify -i circRNAs.txt -b alignments.bam -o expression.txt`
**Explanation:** Quantifies circRNA expression levels.

### Functional analysis
**Args:** `circtools analyze -i circRNAs.txt -a annotation.gtf -o analysis.txt`
**Explanation:** Performs functional analysis of detected circRNAs.

### Display help
**Args:** `circtools --help`
**Explanation:** Shows all available tools and options.