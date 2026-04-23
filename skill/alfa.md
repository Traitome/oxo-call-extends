---
name: alfa
category: qc
description: Software for quick overview of features composing NGS datasets through feature annotation
tags: [ngs, feature-annotation, overview, statistics, alignment]
author: oxo-call-community
source_url: "https://github.com/biocompibens/ALFA"
---

## Concepts

- **Tool Overview**: ALFA provides a quick overview of features composing NGS datasets by annotating reads with genomic feature categories.
- **Core Function**: Classifies sequencing reads by genomic feature type (exon, intron, intergenic, etc.) to assess dataset composition.
- **Input/Output**: Input: BAM file and GTF/GFF annotation. Output: Feature distribution statistics and visualization.
- **Use Cases**: Quality control of RNA-seq libraries, assessment of enrichment protocols, comparison of sequencing strategies.
- **Installation**: Install via bioconda: `conda install -c bioconda alfa`

## Pitfalls

- **Annotation Required**: Requires GTF/GFF annotation file matching the reference genome used for alignment.
- **BAM Sorting**: Input BAM must be coordinate-sorted and indexed.
- **Feature Hierarchy**: Reads overlapping multiple features are assigned based on feature priority hierarchy.
- **Strand Specificity**: Specify correct strandedness for accurate feature assignment in stranded libraries.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available options for ALFA feature analysis.

### Basic feature analysis
**Args:** `alfa -i aligned.bam -g annotation.gtf -o results/`
**Explanation:** Annotates reads with genomic features and generates distribution report.

### Analysis with strand specificity
**Args:** `alfa -i aligned.bam -g annotation.gtf --strand FR -o results/`
**Explanation:** Uses forward-reverse strandedness for accurate feature assignment.

### Generate visualization
**Args:** `alfa -i aligned.bam -g annotation.gtf --plot -o results/`
**Explanation:** Creates feature distribution plots alongside statistics.

### Compare multiple samples
**Args:** `alfa -i sample1.bam sample2.bam -g annotation.gtf -o comparison/`
**Explanation:** Compares feature distributions across multiple samples.

### Custom feature categories
**Args:** `alfa -i aligned.bam -g annotation.gtf --categories custom_cats.tsv -o results/`
**Explanation:** Uses custom feature category definitions for annotation.

### Output raw counts
**Args:** `alfa -i aligned.bam -g annotation.gtf --raw-counts -o results/`
**Explanation:** Outputs raw read counts per feature category for custom analysis.

### Set minimum mapping quality
**Args:** `alfa -i aligned.bam -g annotation.gtf -q 20 -o results/`
**Explanation:** Only counts reads with mapping quality ≥Q20 for feature distribution.
