---
name: mango
category: utility
description: A scalable genomic visualization tool
tags: [mango, utility, visualization, genomic-data]
author: oxo-call-community
source_url: "https://github.com/bdgenomics/mango"
---

## Concepts

- **Tool Overview**: mango v0.0.5 - A scalable genomic visualization tool built on Apache Spark for processing large genomic datasets.
- **Core Function**: Provides interactive visualization of genomic data with support for large-scale datasets.
- **Input/Output**: Input: Genomic data files (BAM, VCF, BED); Output: Visualization plots, HTML reports.
- **Installation**: `conda install -c bioconda mango`
- **Spark-based**: Uses Apache Spark for distributed processing of large datasets.
- **Interactive Visualization**: Supports interactive exploration of genomic data.

## Pitfalls

- **Spark Configuration**: Requires proper Spark cluster configuration.
- **Memory Usage**: Large datasets require significant memory.
- **Network Latency**: Distributed processing may be affected by network performance.
- **Data Format**: Requires properly formatted input files.
- **Scalability**: Performance depends on cluster resources.
- **Dependency Versions**: Requires specific versions of Spark and dependencies.

## Examples

### Basic visualization
**Args:** `mango visualize -i data.vcf -o visualization.html`
**Explanation:** Creates visualization from VCF file.

### With BAM file
**Args:** `mango visualize -i alignments.bam -o visualization.html`
**Explanation:** Visualizes BAM alignment data.

### Region-specific visualization
**Args:** `mango visualize -i data.vcf -r chr1:1-1000000 -o visualization.html`
**Explanation:** Visualizes specific genomic region.

### Interactive mode
**Args:** `mango visualize -i data.vcf -o visualization.html --interactive`
**Explanation:** Creates interactive visualization.

### Batch processing
**Args:** `mango batch -i data/ -o results/`
**Explanation:** Processes multiple files in batch.

### Spark cluster mode
**Args:** `mango visualize -i data.vcf -o visualization.html --spark-cluster spark://master:7077`
**Explanation:** Uses Spark cluster for processing.