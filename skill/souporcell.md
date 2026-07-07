---
name: souporcell
category: single-cell
description: Souporcell - Clustering single-cell RNA-seq by genotypes
tags: [souporcell, single-cell, clustering, genotypes, demultiplexing]
author: oxo-call-community
source_url: "https://github.com/wheaton5/souporcell"
---

## Concepts

- **Tool Overview**: souporcell (v2.5) - A single-cell genotype clustering tool
- **Core Function**: Clusters single-cell RNA-seq by genotypes for demultiplexing
- **Input/Output**: Accepts BAM/VCF; outputs cluster assignments
- **Algorithm**: Uses variant information to cluster cells by genotype
- **Installation**: `conda install -c bioconda souporcell`
- **Key Features**: Cell clustering, genotype demultiplexing, single-cell analysis

## Pitfalls

- **Input Requirements**: Requires properly formatted BAM and VCF files
- **Reference Genome**: Requires reference genome for alignment
- **Variant Sites**: Requires known variant sites for clustering
- **Coverage**: Requires sufficient coverage for reliable clustering
- **Memory Usage**: Large single-cell datasets require significant memory
- **Cluster Number**: Number of clusters must be specified correctly

## Examples

### Display help
**Args:** `souporcell --help`
**Explanation:** Shows available options and usage information.

### Basic clustering
**Args:** `souporcell -i aligned.bam -r reference.fasta -v variants.vcf -k 2 -o clusters.tsv`
**Explanation:** Cluster cells by genotype.

### With known variants
**Args:** `souporcell -i aligned.bam -r reference.fasta -v known_variants.vcf -k 3 -o clusters.tsv`
**Explanation:** Use known variants for clustering.

### With barcodes
**Args:** `souporcell -i aligned.bam -r reference.fasta -v variants.vcf -k 2 -b barcodes.txt -o clusters.tsv`
**Explanation:** Use specific cell barcodes.

### With min coverage
**Args:** `souporcell -i aligned.bam -r reference.fasta -v variants.vcf -k 2 -c 10 -o clusters.tsv`
**Explanation:** Set minimum coverage threshold.

### Output statistics
**Args:** `souporcell -i aligned.bam -r reference.fasta -v variants.vcf -k 2 -o clusters.tsv --stats`
**Explanation:** Output clustering statistics.

### Generate report
**Args:** `souporcell -i aligned.bam -r reference.fasta -v variants.vcf -k 2 -o clusters.tsv --report`
**Explanation:** Generate clustering report.

### With threads
**Args:** `souporcell -i aligned.bam -r reference.fasta -v variants.vcf -k 2 -o clusters.tsv -p 8`
**Explanation:** Use multiple threads for clustering.