---
name: cistrome-ceas
category: annotation
description: Cis-regulatory Element Annotation System for ChIP-seq analysis
tags: [cistrome-ceas, chip-seq, annotation, regulatory-elements, bioinformatics]
author: oxo-call-community
source_url: "http://liulab.dfci.harvard.edu/CEAS/"
---

## Concepts

- **Tool Overview**: Cistrome-CEAS is a Cis-regulatory Element Annotation System for characterizing genome-wide protein-DNA interaction patterns from ChIP-chip and ChIP-Seq data.
- **Core Function**: Annotates ChIP-seq peaks to genomic features and characterizes binding patterns of transcription factors and histone modifications.
- **Algorithm**: Maps peaks to promoters, enhancers, exons, introns, and other genomic regions; performs statistical analysis of binding distributions.
- **Input**: ChIP-seq peak files (BED/GFF) and gene annotation files.
- **Output**: Annotated peaks with genomic location information and statistical summaries.
- **Application**: ChIP-seq data analysis, regulatory element identification, and transcription factor binding characterization.
- **Installation**: Install via bioconda: `conda install -c bioconda cistrome-ceas`

## Pitfalls

- **Peak Quality**: Requires high-quality peak calls for accurate annotation.
- **Annotation Version**: Must use compatible gene annotation version.
- **Genome Assembly**: Must match the reference genome assembly.
- **Data Format**: Input files must be properly formatted.
- **Statistical Significance**: Appropriate thresholds must be applied.

## Examples

### Annotate ChIP-seq peaks
**Args:** `ceas -i peaks.bed -g genome.fasta -a annotation.gtf -o annotation_results.txt`
**Explanation:** Annotates ChIP-seq peaks to genomic features.

### Analyze binding patterns
**Args:** `ceas -i peaks.bed -a annotation.gtf --distplot -o binding_dist.txt`
**Explanation:** Generates distribution plots of binding sites relative to TSS.

### With multiple peak files
**Args:** `ceas -i peaks1.bed,peaks2.bed -a annotation.gtf -o comparison.txt`
**Explanation:** Compares binding patterns across multiple samples.

### Display help
**Args:** `ceas --help`
**Explanation:** Shows all available options and usage information.