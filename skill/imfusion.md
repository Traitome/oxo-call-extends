---
name: imfusion
category: expression
description: IM-Fusion - Tool for identifying transposon insertions and their effects from RNA-sequencing data
tags: [imfusion, expression, transposon, RNA-seq]
author: oxo-call-community
source_url: "https://nki-ccb.github.io/imfusion"
---

## Concepts

- **Tool Overview**: imfusion (v0.3.2) - A computational pipeline for detecting transposon insertions and their effects on gene expression from RNA-seq data
- **Core Function**: Identifies transposon insertion sites, quantifies expression changes, and predicts functional consequences
- **Input/Output**: Accepts RNA-seq BAM files and transposon annotation, outputs insertion calls and expression analysis
- **Installation**: `conda install -c bioconda imfusion` or from GitHub
- **Key Features**: Supports multiple transposon types, integrates with gene expression data, identifies driver insertions

## Pitfalls

- **Transposon Annotation**: Requires accurate transposon reference annotations
- **Alignment Quality**: Poor mapping quality affects insertion detection
- **RNA-seq Strand**: Strand-specific protocols require special handling
- **Multiple Mapping**: Reads mapping to multiple locations can cause false positives
- **Expression Thresholds**: Appropriate thresholds needed for differential expression

## Examples

### Detect transposon insertions
**Args:** `imfusion detect -b aligned.bam -g genome.fasta -t transposons.gtf -o insertions.tsv`
**Explanation:** Detects transposon insertions from aligned RNA-seq reads.

### Quantify insertion expression
**Args:** `imfusion quantify -i insertions.tsv -b aligned.bam -o expression.tsv`
**Explanation:** Quantifies expression levels of transposon insertions.

### Identify driver insertions
**Args:** `imfusion drivers -i insertions.tsv -e expression.tsv -o drivers.tsv`
**Explanation:** Identifies potential driver insertions based on recurrence and expression.

### Generate visualization
**Args:** `imfusion plot -i insertions.tsv -g genome.fasta -o insertion_plot.pdf`
**Explanation:** Generates visualization of insertion sites across the genome.

### Run full pipeline
**Args:** `imfusion pipeline -b aligned.bam -g genome.fasta -t transposons.gtf -o results/`
**Explanation:** Runs complete pipeline from detection to driver identification.

### Filter insertions by quality
**Args:** `imfusion filter -i insertions.tsv -q 30 -o filtered.tsv`
**Explanation:** Filters insertions with mapping quality >= 30.