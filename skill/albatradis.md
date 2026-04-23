---
name: albatradis
category: annotation
description: Comparative analysis tool for large-scale Transposon Directed Insertion-site Sequencing (TraDIS) experiments
tags: [tradis, transposon, mutagenesis, comparative, essential-genes]
author: oxo-call-community
source_url: "https://github.com/quadram-institute-bioscience/albatradis"
---

## Concepts

- **Tool Overview**: AlbaTraDIS performs rapid large-scale comparative analysis of TraDIS experiments to identify genes influencing bacterial survival.
- **Core Function**: Compares multiple TraDIS datasets, predicting the impact of transposon insertions on nearby genes and identifying conditionally essential genes.
- **Input/Output**: Input: TraDIS BAM files and gene annotations. Output: Gene essentiality reports, comparative statistics.
- **Scalability**: Designed for comparing multiple conditions simultaneously, handling large TraDIS datasets efficiently.
- **Installation**: Install via bioconda: `conda install -c bioconda albatradis`

## Pitfalls

- **Insert Site Format**: Requires properly formatted TraDIS BAM files with insertion site information.
- **Gene Annotation**: Needs accurate gene annotation in GFF format for proper gene-level analysis.
- **Replicate Consistency**: Biological replicates should show consistent patterns - check before comparative analysis.
- **Statistical Thresholds**: Adjust statistical thresholds based on experimental design and coverage depth.

## Examples

### Display help information
**Args:** `--help`
**Explanation:** Shows available commands and options for AlbaTraDIS.

### Compare two conditions
**Args:** `compare -c control.bam -t treatment.bam -g annotation.gff -o comparison/`
**Explanation:** Compares TraDIS data between control and treatment conditions.

### Multi-condition analysis
**Args:** `compare -c control.bam -t cond1.bam cond2.bam cond3.bam -g annotation.gff -o multi_comp/`
**Explanation:** Compares multiple treatment conditions against a single control.

### Essential gene detection
**Args:** `essential -i tradis.bam -g annotation.gff -o essential_genes.tsv`
**Explanation:** Identifies essential genes from a single TraDIS experiment.

### Set insertion site threshold
**Args:** `compare -c control.bam -t treatment.bam -g annotation.gff --min-inserts 10 -o results/`
**Explanation:** Requires minimum 10 insertions per gene for statistical analysis.

### Output with gene context
**Args:** `compare -c control.bam -t treatment.bam -g annotation.gff --context 500 -o results/`
**Explanation:** Includes 500bp flanking context in gene impact analysis.

### Generate visualization
**Args:** `compare -c control.bam -t treatment.bam -g annotation.gff --plot -o results/`
**Explanation:** Generates insertion plots for significant genes.
