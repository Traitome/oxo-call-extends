---
name: blockclust
category: annotation
description: Efficient clustering and classification of non-coding RNAs from short read RNA-seq
tags: [blockclust, ncrna, rna-seq, clustering, annotation]
author: oxo-call-community
source_url: "https://github.com/pavanvidem/blockclust"
---

## Concepts

- **Tool Overview**: BlockClust clusters and classifies non-coding RNAs from RNA-seq data.
- **Core Function**: Identifies and categorizes ncRNA types using read profile clustering.
- **Input**: BAM file with aligned RNA-seq reads.
- **Output**: ncRNA clusters with functional classifications.
- **Features**: Supports various ncRNA types (tRNA, rRNA, snoRNA, etc.).
- **Installation**: Install via bioconda: `conda install -c bioconda blockclust`

## Pitfalls

- **BAM Input**: Requires aligned BAM file; ensure proper alignment to ncRNA loci.
- **Reference**: Requires ncRNA reference annotations for classification.
- **Coverage**: Low coverage may affect clustering accuracy.
- **Strand Specificity**: Strand-specific libraries improve classification accuracy.

## Examples

### Cluster ncRNAs from BAM
**Args:** `blockclust -i aligned.bam -o ncRNA_clusters.tsv`
**Explanation:** Clusters and classifies ncRNAs from aligned RNA-seq reads.

### Specify reference annotations
**Args:** `blockclust -i aligned.bam -r ncRNA.gff -o clusters.tsv`
**Explanation:** Uses reference annotations for improved classification.

### Set minimum cluster size
**Args:** `blockclust -i aligned.bam -m 10 -o clusters.tsv`
**Explanation:** Requires minimum 10 reads per cluster for calling.

### Display help
**Args:** `--help`
**Explanation:** Shows all available options and usage information.
