---
name: ceas
category: epigenomics
description: "CEAS: Cis-regulatory Element Annotation System"
tags: [ceas, cis-regulatory, annotation, chip-seq, epigenomics]
author: oxo-call-community
source_url: "http://liulab.dfci.harvard.edu/CEAS"
---
## Concepts

- **Tool Overview**: CEAS annotates cis-regulatory elements from ChIP-seq and other epigenomic data.
- **Core Function**: Identifies and annotates transcription factor binding sites and regulatory regions.
- **Algorithm**: Integrates peak calls with gene annotations for functional analysis.
- **Input**: ChIP-seq peak files (BED, narrowPeak, broadPeak) and genome annotation.
- **Output**: Annotated regulatory elements with gene associations.
- **Application**: ChIP-seq data analysis and regulatory element discovery.
- **Installation**: Install via bioconda: `conda install -c bioconda ceas`

## Pitfalls

- **Genome Build**: Must use matching genome assembly for annotations.
- **Peak Quality**: Depends on quality of input peak calls.
- **Annotation Sources**: Requires gene annotation files (RefSeq, Ensembl).
- **Memory Usage**: Large datasets may require significant memory.

## Examples

### Annotate ChIP-seq peaks
**Args:** `ceas -b peaks.bed -g hg38 -o annotation_results/`
**Explanation:** Annotates ChIP-seq peaks using hg38 genome assembly.

### With custom annotation
**Args:** `ceas -b peaks.bed -a genes.gtf -o results/`
**Explanation:** Uses custom gene annotation for peak annotation.

### Generate summary statistics
**Args:** `ceas -b peaks.bed -g mm10 --summary -o summary.txt`
**Explanation:** Generates summary statistics for ChIP-seq peaks.

### Display help
**Args:** `ceas --help`
**Explanation:** Shows all available options and usage information.